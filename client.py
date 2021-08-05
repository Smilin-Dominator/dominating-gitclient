import os
import sys
from colours import bcolors, enterprompt, greeting
import subprocess

# importing the files
import origin
import commit
import branches
import create


def main(path):
    os.chdir(path)
    try:
        subprocess.check_output("git status", shell=True)
    except subprocess.CalledProcessError:
        create.main()
    choi = "1"
    while choi != "99":
        os.system("cls")
        greeting()
        print(f"\n1) {bcolors.OKGREEN}Push/Pull Related Options{bcolors.ENDC}\n"
              f"2) {bcolors.OKBLUE}Commit, Checkout And Stash{bcolors.ENDC}\n"
              f"3) {bcolors.OKCYAN}Show Differences{bcolors.ENDC}\n"
              f"4) {bcolors.HEADER}Branch Administration{bcolors.ENDC}\n"
              f"5) {bcolors.OKGREEN}Commit Log{bcolors.ENDC}\n"
              f"99) {bcolors.WARNING}Quit{bcolors.ENDC}")
        choi = input(": ")
        match choi:
            case "1":
                origin.main()
            case "2":
                commit.main()
            case "3":
                print(f"\n\n{bcolors.UNDERLINE}{bcolors.OKGREEN}Red = Removed\nGreen = Added\n"
                      f"Use The Up And Down Arrow To Go Up And Down\nType 'q' To Leave!{bcolors.ENDC}\n\n")
                enterprompt()
                a = subprocess.call("git diff", shell=True)
                print(a)
            case "4":
                branches.main()
            case "5":
                a = subprocess.call("git log --graph", shell=True)
                print(a)
                enterprompt()
            case "99":
                os.system("cls")
                sys.exit(0)
            case _:
                pass

