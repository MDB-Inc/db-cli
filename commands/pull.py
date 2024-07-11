from argparse import Namespace

import settings
from modules.abstracts.command import BasePushPullCommand
from modules.aws import get_s3_path_startswith, get_s3_path_latest


class Pull(BasePushPullCommand):
    success_text = "Pulled: {s3_path} > {container_name}"
    fail_text = "Pull Failed: {s3_path} > {container_name}"

    def get_s3_path_hook(self, args: Namespace):
        if args.latest:
            return get_s3_path_latest(settings.BUCKET_NAME, args.project)

        if len(args.id) < 4:
            raise Exception("git commit ID must be at least 4 characters long")
        return get_s3_path_startswith(settings.BUCKET_NAME, args.project, args.id)

    def get_command_hook(self, container_name: str, db: str, db_user: str, s3_path: str, aws_profile: str) -> str:
        return f"aws s3 cp {s3_path} - --profile {aws_profile} | docker exec -i {container_name} psql -d {db} -U {db_user}"
