from config import console, input
from subprocess import getoutput


def main():
    with console.pager(styles=True):
        console.print(getoutput("git log"))
    input("(enter to continue)", "red")
