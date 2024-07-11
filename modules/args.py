import argparse

from modules.getters import get_github_repo_name, get_commit_id
from modules.run import STR_TO_COMMAND


def get_argument_parser() -> argparse.ArgumentParser:
    description = """
    Push and pull dumped data from a Database on Docker.
    see: https://github.com/MDB-Inc/db-cli
    
    * example:
    db push <container_name>
    
    equivalent to: 
    db push <container_name> <git_commit_id> --project <github_repo_name>
    """
    # usage = "db <command> <container_name> <id> [options]"

    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('command', choices=STR_TO_COMMAND.keys())
    parser.add_argument('container_name', help='docker DB container name')
    parser.add_argument('id', nargs="?", help='s3 filename. default=<git_commit_id>', default=get_commit_id())
    parser.add_argument('-p', '--project', help='s3 bucket directory. default=<github_repo_name>', default=get_github_repo_name())
    parser.add_argument('--latest', help='(pull only) pull latest dump', action='store_true', default=False)
    return parser
