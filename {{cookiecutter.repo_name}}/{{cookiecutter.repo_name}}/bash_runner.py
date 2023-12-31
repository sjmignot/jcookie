import os
import subprocess

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def _run(bash_script):
    return subprocess.call(bash_script, shell=True)


def docker_run():
    return _run(os.path.join(os.path.dirname(DIR_PATH), "scripts", "docker_run.sh"))


def upload_cache():
    return _run(os.path.join(os.path.dirname(DIR_PATH), "scripts", "upload_cache.sh"))


def download_cache():
    return _run(os.path.join(os.path.dirname(DIR_PATH), "scripts", "download_cache.sh"))
