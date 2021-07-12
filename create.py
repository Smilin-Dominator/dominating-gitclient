import os
import subprocess

def main():
    proceed = input("[+] Initialize Repository? (y/n): ")
    if proceed == "n":
        os.system('cls')
        quit(0)
    else:
        print("[*] Initializing Repository")
        subprocess.call("git init", shell=True)