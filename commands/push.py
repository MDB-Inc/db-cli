from argparse import Namespace

import settings
from modules.abstracts.command import BasePushPullCommand
from modules.aws import get_s3_path


class Push(BasePushPullCommand):
    success_text = "Pushed: {container_name} > {s3_path}"
    fail_text = "Push Failed: {container_name} > {s3_path}"

    def get_s3_path_hook(self, args: Namespace):
        if len(args.id) < 4:
            raise Exception("git commit ID must be at least 4 characters long")
        return get_s3_path(settings.BUCKET_NAME, args.project, args.id)

    def get_command_hook(self, container_name: str, db: str, db_user: str, s3_path: str, aws_profile: str) -> str:
        return f"docker exec {container_name} pg_dump -d {db} -U {db_user} | aws s3 cp - {s3_path} --profile {aws_profile}"
