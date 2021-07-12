import subprocess
import os
from colours import bcolors, enterprompt
from __main__ import greeting


def main():
    choice = 1
    while choice != 99:
        os.system("cls")
        greeting()
        print(f"\n1) {bcolors.OKCYAN}Pull From Origin{bcolors.ENDC}\n"
              f"2) {bcolors.OKBLUE}Push To Origin{bcolors.ENDC}\n"
              f"3) {bcolors.OKGREEN}Git Status{bcolors.ENDC}\n"
              f"4) {bcolors.HEADER}Fetch From Origin{bcolors.ENDC}\n"
              f"99) {bcolors.WARNING}Return To Main Menu{bcolors.ENDC}")
        choice = input(": ")
        match choice:
            case "1":
                print(f"\n{subprocess.getoutput('git pull origin')}\n")
                enterprompt()
            case "2":
                a = subprocess.getoutput('git push origin').splitlines()
                if "has no upstream branch." in a[0]:
                    a = a[0].split(" ")
                    branch = a[4]
                    b = subprocess.getoutput(f'git push --set-upstream origin {branch}')
                    print(f'\n{b}\n')
                else:
                    print(f"\n{''.join(a)}\n")
                enterprompt()
            case "3":
                print(f"\n{subprocess.getoutput('git status')}\n")
                enterprompt()
            case "4":
                print(f"\n{subprocess.getoutput('git fetch origin')}\n")
                enterprompt()
            case "99":
                break
            case _:
                pass
