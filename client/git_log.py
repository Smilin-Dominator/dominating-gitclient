from config import console
from subprocess import Popen, PIPE


def main():
    with console.pager():
        process = Popen(["git", "log", "--graph"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        while process.stdout.readable():
            line = process.stdout.readline()
            if not line:
                break
            console.print(line.strip())
