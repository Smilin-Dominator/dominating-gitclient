import subprocess

def main():
    proceed = input("[+] Initializ Repository? (y/n): ")
    if proceed == "n":
        quit(0)
    else:
        print("[*] Initializing Repository")
        subprocess.call("git init", shell=True)