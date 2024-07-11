import subprocess

import settings
from modules.envs import get_env


def get_commit_id():
    return subprocess.run(["git", "rev-parse", "HEAD"], check=True, text=True, capture_output=True).stdout.strip()

def get_github_repo_name():
    return subprocess.run(["git", "rev-parse", "--show-toplevel"], check=True, text=True, capture_output=True).stdout.strip().split("/")[-1]

def get_db(container_name: str) -> str:
    return get_env(container_name, settings.ENV_DB)

def get_db_user(container_name: str) -> str:
    return get_env(container_name, settings.ENV_DB_USER)
