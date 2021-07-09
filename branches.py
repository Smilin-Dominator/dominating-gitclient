import subprocess
from __main__ import greeting
from colours import bcolors, enterprompt
import os


def get_branches():
    a = subprocess.check_output("git branch").decode().splitlines()
    b = []
    for line in a:
        b.append(line.replace(" ", "").replace("*", ""))
    print("\nBranches: \n")
    for i in range(len(b)):
        print(f"{i+1}) {b[i]}")
    print("\n")
    return b

def main():
    choice = "1"
    while choice != "99":
        os.system("cls")
        greeting()
        print(f"\n1) {bcolors.OKBLUE}View Branches{bcolors.ENDC}\n"
              f"2) {bcolors.OKGREEN}Checkout A Branch{bcolors.ENDC}\n"
              f"3) {bcolors.OKCYAN}Merge Branches{bcolors.ENDC}\n"
              f"4) {bcolors.FAIL}Delete A Branch{bcolors.ENDC}\n"
              f"99) {bcolors.WARNING}Main Menu{bcolors.ENDC}")
        choice = input(": ")
        match choice:
            case "1":
                get_branches()
                enterprompt()
            case "2":
                b = get_branches()
                bra = int(input("\n[+] Which Branch Would You Like To Checkout?: "))
                try:
                    cmd = "git checkout " + b[bra - 1]
                    print(f"\n{subprocess.check_output(cmd).decode()}\n")
                except:
                    print("[*] No Such Branch")
                enterprompt()
            case "3":
                b = get_branches()
                branch = int(input("[*] Which Branch Do You Want To Checkout?: "))
                branchtm = int(input(f"[*] Which Branch Do You Want To Merge Into?: "))
                cmd_c = f"git checkout {b[branch - 1]}"
                cmd_m = f"git merge {b[branchtm - 1]}"
                try:
                    print(f"\n{subprocess.call(cmd_c, shell=True)}\n")
                    print(f"\n{subprocess.call(cmd_m, shell=True)}\n")
                except:
                    print("[*] Invalid Command, Try Again..")
                enterprompt()
            case "4":
                b = get_branches()
                bra = int(input("[*] Which Branch Would You Like To Delete?: "))
                cmd = f"git branch -d {b[bra - 1]}"
                try:
                    print(f"\n{subprocess.call(cmd, shell=True)}\n")
                except:
                    print(f"[*] Invalid Branch")
                enterprompt()
