from subprocess import getoutput
from client.first_time import main as setup
from client.main import main as cl
from functions.configuration import Config
from config import warning, error, info, input, enter_prompt
from sys import argv, exit
from os import chdir
from subprocess import call, DEVNULL
from pathlib import Path


def first_time_check():
    key = getoutput("git rev-parse --is-inside-work-tree")
    if key == "fatal: not a git repository (or any of the parent directories): .git":
        setup()


def config():

    def write(file: Path, contents: str):
        fil = open(file, "w")
        fil.write(contents)
        fil.flush()
        fil.close()

    conf = Config()
    ar = conf.parse_config()
    if ar['update_check_frequency'] != 0:
        number = ar['update_check_frequency']
        count = Path(str(conf.file)[:-11], "count.txt")
        try:
            with open(count, "r") as b:
                num = int(b.read())
                if num == number:
                    call("git fetch origin", shell=True, stdout=DEVNULL)
                    lines = getoutput("git status").splitlines()
                    if not lines[1].startswith("Your branch is behind"):
                        info("Program is up to date")
                        enter_prompt()
                    else:
                        up = input("\tUpdate Found, Would You Like To Update?", override="red", choices=["y", "n"], default="y")
                        if up:
                            call("git pull origin master", shell=True)
                    write(count, "1")
                else:
                    write(count, str(num + 1))
        except FileNotFoundError:
            with open(count, "w") as b:
                write(count, "1")


if __name__ == "__main__":
    config()
    if len(argv) < 2:
        warning("Not Enough Arguments")
        exit(1)
    try:
        chdir(argv[1])
    except FileNotFoundError:
        error("Specified Directory Not Found!")
        exit(2)
    first_time_check()
    cl()


