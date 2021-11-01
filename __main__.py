from subprocess import getoutput
from client.first_time import main as setup
from client.main import main as cl
from config import warning
from sys import argv, exit
from os import chdir


def first_time_check():
    key = getoutput("git rev-parse --is-inside-work-tree")
    if key == "fatal: not a git repository (or any of the parent directories): .git":
        setup()


if __name__ == "__main__":
    if len(argv) < 2:
        warning("Not Enough Arguments")
        exit(1)
    chdir(argv[1])
    first_time_check()
    cl()


