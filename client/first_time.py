from config import info, input, error
from subprocess import call
from sys import exit


def main():
    info("There's no git repository in the specified path")
    choice = input("Create One?", override="navajo_white3", default="y", choices=["y", "n"])
    match choice:
        case "y":
            code = call("git init", shell=True)
            if code != 0:
                error("Error While Running Git Init")
            else:
                info("Success!")
        case "n":
            exit(0)
