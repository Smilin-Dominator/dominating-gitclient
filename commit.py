from colours import bcolors, enterprompt
from __main__ import greeting
import os
import subprocess


def main():
    choice = "1"
    while choice != "99":
        os.system("cls")
        greeting()
        print(f"1) {bcolors.BOLD}Commit Files{bcolors.ENDC}\n"
              f"2) {bcolors.OKBLUE}Checkout Branch{bcolors.ENDC}\n"
              f"3) {bcolors.OKGREEN}Stash{bcolors.ENDC}\n"
              f"99) {bcolors.WARNING}Main Menu{bcolors.ENDC}")
        choice = input(": ")
        match choice:
            case "1":
                mfilelist = []
                nfilelist = []
                a = subprocess.check_output("git status").decode().splitlines()
                for supposed_file in a:
                    if supposed_file.startswith("\tnew file:"):
                        name = supposed_file.replace(" ", "").replace("newfile:", '')
                        string = "\tNew File: " + name
                        nfilelist.append(string)
                    elif supposed_file.startswith("\tmodified: "):
                        name = supposed_file.replace(" ", "").replace("modified:", '')
                        string = "\tModified File: " + name
                        mfilelist.append(string)
                print("\nNew Files: \n")
                for file in nfilelist:
                    print(file)
                print("\nModified Files: \n")
                for file in mfilelist:
                    print(file)
                enterprompt()
