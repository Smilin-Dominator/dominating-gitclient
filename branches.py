import subprocess
from colours import bcolors, enterprompt, greeting, log_format
import os
import logging

logging.basicConfig(filename="log.txt", format=log_format, datefmt='[%Y-%m-%d] [%H:%M:%S]', level=logging.DEBUG)


def get_branches():
    a = subprocess.check_output("git branch").decode().splitlines()
    b = []
    for line in a:
        b.append(line.replace(" ", "").replace("*", ""))
    print("\nBranches: \n")
    for i in range(len(b)):
        print(f"{i + 1}) {b[i]}")
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
              f"5) {bcolors.HEADER}Create A Branch{bcolors.ENDC}\n"
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
                except IndexError as e:
                    print("[*] No Such Branch Exists In This Universe...")
                    logging.exception("[ Error While Checking Out Branch: %s ]" % e)
                enterprompt()
            case "3":
                b = get_branches()
                if len(b) > 1:
                    try:
                        branch = int(input("[*] Which Branch Do You Want To Checkout? (Ctrl+C to Abort): "))
                        branchtm = int(input(f"[*] Which Branch Do You Want To Merge Into? (Ctrl+C to Abort): "))
                        cmd_c = f"git checkout {b[branch - 1]}"
                        cmd_m = f"git merge {b[branchtm - 1]}"
                        print(f"\n{subprocess.call(cmd_c, shell=True)}\n")
                        print(f"\n{subprocess.call(cmd_m, shell=True)}\n")
                    except KeyboardInterrupt:
                        print("\n[*] Aborted.. ")
                    except subprocess.CalledProcessError as e:
                        print("\n[*] Command Failed, Try Again..")
                        logging.exception("[ Error while Merging Branch: %s ]" % e)
                    except IndexError as e:
                        print("\n[!] Enter A Number Included In The List!")
                        logging.exception("[ Error while Merging Branch: %s ]" % e)
                    except ValueError as e:
                        print("\n[!] Not An Integer!")
                        logging.exception("[ Error while Merging Branch: %s ]" % e)
                else:
                    print("[*] Not Enough Branches To Perform A Merge")
                enterprompt()
            case "4":
                b = get_branches()
                if len(b) > 1:
                    try:
                        bra = int(input("[*] Which Branch Would You Like To Delete? (Ctrl+C to Cancel): "))
                        cmd = f"git branch -d {b[bra - 1]}"
                        print(f"\n{subprocess.call(cmd, shell=True)}\n")
                    except KeyboardInterrupt:
                        print("\n[*] Aborted..")
                    except subprocess.CalledProcessError as e:
                        print(f"\n[*] Branch Wasn't Deleted")
                        logging.exception("[ Error While Deleting Branch: %s ]" % e)
                    except ValueError as e:
                        print(f"\n[*] Not An Integer!")
                        logging.exception("[ Error While Deleting Branch: %s ]" % e)
                    except IndexError as e:
                        print(f"\n[*] Enter A Number Included In The List!")
                        logging.exception("[ Error While Deleting Branch: %s ]" % e)
                else:
                    print("[*] Only One Branch Remains, And You Can't Delete That.")
                enterprompt()
