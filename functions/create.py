import os
import sys
import subprocess
import logging
from configuration.colours import log_format

logging.basicConfig(filename="../log.txt", format=log_format, datefmt='[%Y-%m-%d] [%H:%M:%S]', level=logging.DEBUG)


def main():
    proceed = input("[+] Initialize Repository? (y/n): ")
    if proceed == "n":
        os.system('cls')
        sys.exit(0)
    else:
        print("[*] Initializing Repository")
        logging.info("Initializing Git Repository In \"%s\"" % os.getcwd())
        subprocess.call("git init", shell=True)
