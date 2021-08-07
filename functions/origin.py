import subprocess
import os
from configuration.colours import bcolors, enterprompt, greeting, log_format
import logging


logging.basicConfig(filename="log.txt", format=log_format, datefmt='[%Y-%m-%d] [%H:%M:%S]', level=logging.DEBUG)


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
                b = subprocess.getoutput('git push origin')
                a = b.splitlines()
                if "has no upstream branch." in a[0]:
                    a = a[0].split(" ")
                    branch = a[4]
                    b = subprocess.getoutput(f'git push --set-upstream origin {branch}')
                    print(f'\n{b}\n')
                    logging.info("Set Branch %s Upstream To Origin" % branch)
                else:
                    print(f"\n{b}\n")
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
                logging.warning("Invalid Choice %d" % choice)
                pass
