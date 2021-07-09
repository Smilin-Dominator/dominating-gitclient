from colours import bcolors, enterprompt
from __main__ import greeting
import os
import subprocess


def main():
    choice = "1"
    while choice != "99":
        os.system("cls")
        greeting()
        print(f"\n1) {bcolors.OKCYAN}Commit Files{bcolors.ENDC}\n"
              f"2) {bcolors.OKGREEN}Checkout Branch{bcolors.ENDC}\n"
              f"3) {bcolors.OKBLUE}Stash{bcolors.ENDC}\n"
              f"99) {bcolors.WARNING}Main Menu{bcolors.ENDC}")
        choice = input(": ")
        match choice:
            case "1":
                mfilelist = []
                nfilelist = []
                dfilelist = []
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
                    elif supposed_file.startswith("\tdeleted: "):
                        name = supposed_file.replace(" ", "").replace("deleted:", '')
                        string = "\tDeleted File: " + name
                        dfilelist.append(string)
                if len(nfilelist) > 0:
                    print("\nNew Files: \n")
                    for file in nfilelist:
                        print(file)
                if len(mfilelist) > 0:
                    print("\nModified Files: \n")
                    for file in mfilelist:
                        print(file)
                if len(dfilelist) > 0:
                    print("\nDeleted Files: \n")
                    for file in dfilelist:
                        print(file)
                print("\n\n[*] Which Files Would You Like To Commit? (all / [enter the files sep. by spaces]")
                comlist = input("[*] ")
                if comlist == "all":
                    print(f"\n{subprocess.check_output('git commit *').decode()}\n")
                else:
                    try:
                        comlist = comlist.split(" ")
                        cmd = f"git commit {' '.join(comlist)}"
                        print(f"""\n{subprocess.check_output(cmd).decode()}\n""")
                    except:
                        print("[*] Invalid Filename, Please Try Again")
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
                cmd = "git checkout " + b[bra - 1]
                print(f"\n{subprocess.check_output(cmd).decode()}\n")
                enterprompt()
            case "3":
                choice2 = '1'
                while choice2 != "99":
                    os.system("cls")
                    greeting()
                    print(f"\n1) {bcolors.HEADER}Stash{bcolors.ENDC}\n"
                          f"2) {bcolors.OKBLUE}View Stashes{bcolors.ENDC}\n"
                          f"3) {bcolors.OKGREEN}Apply Stash{bcolors.ENDC}\n"
                          f"4) {bcolors.OKCYAN}Remove Stash{bcolors.ENDC}\n"
                          f"99) {bcolors.WARNING}Previous Menu{bcolors.ENDC}")
                    choice2 = input(": ")
                    match choice2:
                        case "1":
                            msg = input("\n[*] Message: ")
                            string = f'git stash save "{msg}"'
                            print(f"\n{subprocess.check_output(string).decode()}\n")
                            enterprompt()
                        case "2":
                            print(f"\n{subprocess.check_output('git stash list').decode()}\n")
                            enterprompt()
                        case "3":
                            slist = subprocess.check_output('git stash list').decode().splitlines()
                            print("\nStashes: \n")
                            for i in range(len(slist)):
                                print(f"{i+1}) {slist[i]}")
                            cho = int(input("\n[+] Which Stash Would You Like To Apply?: "))
                            try:
                                stash = slist[cho - 1].split(':')[0]
                                string = f"git stash apply {stash}"
                                print(f"\n{subprocess.check_output(string).decode()}\n")
                            except:
                                print("[*] No Such Stash")
                            enterprompt()
                        case "4":
                            slist = subprocess.check_output('git stash list').decode().splitlines()
                            print("\nStashes: \n")
                            for i in range(len(slist)):
                                print(f"{i + 1}) {slist[i]}")
                            cho = int(input("\n[+] Which Stash Would You Like To Drop?: "))
                            try:
                                stash = slist[cho - 1].split(':')[0]
                                string = f"git stash drop {stash}"
                                print(f"\n{subprocess.check_output(string).decode()}\n")
                            except:
                                print("[*] No Such Stash")
                            enterprompt()



