import subprocess
from __main__ import greeting
from colours import bcolors, enterprompt
import os

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
                print(f"\n{subprocess.check_output('git branch').decode()}\n")
                enterprompt()
            case "2":
                a = subprocess.check_output("git branch").decode().splitlines()
                b = []
                for line in a:
                    b.append(line.replace(" ", "").replace("*", ""))
                print("Branches: \n")
                for i in range(len(b)):
                    print(f"{i+1}) {b[i]}")
                bra = int(input("\n[+] Which Branch Would You Like To Checkout?: "))
                try:
                    cmd = "git checkout " + b[bra - 1]
                    print(f"\n{subprocess.check_output(cmd).decode()}\n")
                except:
                    print("Invalid Value, Please Retry")
                enterprompt()