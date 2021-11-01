from subprocess import getoutput
from client.first_time import main as setup
from client.main import main as cl


def first_time_check():
    key = bool(getoutput("git rev-parse --is-inside-work-tree"))
    if not key:
        setup()


if __name__ == "__main__":
    first_time_check()
    cl()


