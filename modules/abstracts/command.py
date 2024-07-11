import subprocess
from abc import ABC, abstractmethod
from argparse import Namespace
from typing import TypedDict

import settings
from modules.getters import get_db, get_db_user


class DefaultsType(TypedDict):
    """
    get_defaults 의 반환 타입
    """
    container_name: str
    db: str
    db_user: str
    aws_profile: str
    s3_path: str


class AbstractCommand(ABC):
    def print_result(self, return_code: int, sucess_text: str, fail_text: str) -> None:
        if return_code == 0:
            print(sucess_text)
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(fail_text)
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @abstractmethod
    def execute(self, args: Namespace):
        pass


class BasePushPullCommand(AbstractCommand):
    success_text: str
    fail_text: str

    @abstractmethod
    def get_s3_path_hook(self, args: Namespace) -> str:
        pass

    @abstractmethod
    def get_command_hook(self, container_name: str, db: str, db_user: str, s3_path: str, aws_profile: str) -> str:
        pass

    def execute(self, args: Namespace):
        container_name = args.container_name
        db = get_db(container_name)
        db_user = get_db_user(container_name)
        aws_profile = settings.AWS_PROFILE

        # AWS S3 파일 경로
        s3_path = self.get_s3_path_hook(args)

        # Docker를 통해 Postgres 데이터베이스 덤프를 생성하고 S3로 직접 스트리밍
        command = self.get_command_hook(container_name, db, db_user, s3_path, aws_profile)
        result = subprocess.run(command, shell=True, check=True)
        return_code = result.returncode
        # 결과 출력
        self.print_result(return_code, self.success_text.format(s3_path=s3_path, container_name=container_name), self.fail_text.format(s3_path=s3_path, container_name=container_name))
