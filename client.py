import os
import subprocess


def main(path, syner):
    print(f"[+] Path: {path}")
    os.chdir(path)
    choi = "1"
    while choi != "5":
        print("\nWhich Set Of Option Would You Like To See?\n"
              "1 For Push/Pull Related Options")
        choi = input(": ")
        match choi:
            case "1":
                import origin
                origin.main(syner)
            case _:
                print(syner("Invalid Option"))