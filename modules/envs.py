import subprocess

def get_env(container_name: str, env_name: str) -> str:
    """
    container 에서 해당 env 를 echo 하여 가져옴.
    :param container_name:
    :param env_name:
    :return:
    """
    return subprocess.run([f"docker exec {container_name} sh -c 'echo ${env_name}'"], shell=True, check=True, text=True, capture_output=True).stdout.strip()
