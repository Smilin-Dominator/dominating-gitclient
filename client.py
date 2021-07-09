import os
from colours import bcolors
from __main__ import greeting


def main(path, syner):
    print(f"[+] Path: {path}")
    os.chdir(path)
    choi = "1"
    while choi != "5":
        os.system("cls")
        greeting()
        print("\nWhich Set Of Option Would You Like To See?\n"
              f"1) {bcolors.OKGREEN}Push/Pull Related Options{bcolors.ENDC}\n"
              f"99) {bcolors.WARNING}Quit{bcolors.ENDC}")
        choi = input(": ")
        match choi:
            case "1":
                import origin
                origin.main()
            case "99":
                os.system("cls")
                quit(0)
            case _:
                print(syner("Invalid Option"))