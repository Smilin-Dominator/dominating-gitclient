import os
import sys
import subprocess


def main():
    proceed = input("[+] Initialize Repository? (y/n): ")
    if proceed == "n":
        os.system('cls')
        sys.exit(0)
    else:
        print("[*] Initializing Repository")
        subprocess.call("git init", shell=True)
