from subprocess import call, CalledProcessError

from ..design.rich import error


def commit(files: list, message: str):
    code = call(f"git commit {' '.join(files)} -m '{message}'", shell=True)
    if code != 0:
        error("Error While Committing!")
