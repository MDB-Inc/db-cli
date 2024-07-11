import json
import subprocess

import settings


def get_s3_dir(bucket_name: str, project: str) -> str:
    return f"s3://{bucket_name}/{project}/"

def get_s3_path(bucket_name: str, project: str, id_: str) -> str:
    return f"{get_s3_dir(bucket_name, project)}{id_}"


def get_s3_path_startswith(bucket_name: str, project: str, id_: str) -> str:
    """
    S3 에서 특정 prefix 로 시작하는 파일 목록을 가져옴.
    :return:
    """
    aws_profile = settings.AWS_PROFILE

    s3_dir = get_s3_dir(bucket_name, project)
    s3_path = get_s3_path(bucket_name, project, id_)
    # command = f"aws s3 ls {s3_path} --profile {aws_profile}"
    search_results = subprocess.run(["aws", "s3", "ls", s3_path, "--profile", aws_profile ], check=True, text=True, capture_output=True).stdout.strip().split("\n")

    if len(search_results) == 0:
        raise Exception(f"No files found in {s3_path}")

    if len(search_results) > 1:
        raise Exception(f"Multiple files found in {s3_path}")

    file_name = search_results[0].split(" ")[-1]
    return f"{s3_dir}{file_name}"


def get_s3_path_latest(bucket_name: str, project: str) -> str:
    """
    S3 에서 가장 최신을 가져옴.
    :return:
    """
    aws_profile = settings.AWS_PROFILE

    s3_dir = get_s3_dir(bucket_name, project)
    # command = f"aws s3 ls {s3_path} --profile {aws_profile}"
    result = subprocess.run(["aws", "s3api", "list-objects",
                                     "--bucket", bucket_name,
                                     "--query", 'reverse(sort_by(Contents,&LastModified))',
                                     "--prefix", f"{project}",
                                     "--profile", aws_profile],
                                    stdout=subprocess.PIPE, check=True, text=True)

    json_result = json.loads(result.stdout)
    file_name = json_result[0]["Key"].split("/")[-1]
    return f"{s3_dir}{file_name}"
