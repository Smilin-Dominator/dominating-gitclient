import subprocess
import os
from colours import bcolors
from __main__ import greeting


def main(syner):
    os.system("cls")
    greeting()
    print(f"1 For {bcolors.OKCYAN}Pull From Origin{bcolors.ENDC}")
    choice = input(": ")
    match choice:
        case "1":
            print(f"\n{subprocess.getoutput('git pull origin')}\n")
        case "2":
            print(f"\n{subprocess.getoutput('git push origin')}\n")
        case "3":
            print(f"\n{subprocess.getoutput('git status')}\n")
        case "4":
            print(f"\n{subprocess.getoutput('git fetch origin')}\n")
        case "5":
            quit(0)
        case _:
            print(syner("Wrong Command."))