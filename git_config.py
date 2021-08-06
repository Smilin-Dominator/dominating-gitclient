import logging
import subprocess

from colours import bcolors, greeting, log_format
import os

logging.basicConfig(filename="log.txt", format=log_format, datefmt='[%Y-%m-%d] [%H:%M:%S]', level=logging.DEBUG)


def main():
    choice = "98.9"
    while choice != "99":
        os.system("cls")
        greeting()
        print(f"\n1) {bcolors.OKBLUE}Name And Email{bcolors.ENDC}\n"
              f"2) {bcolors.OKGREEN}Text Editor{bcolors.ENDC}\n"
              f"3) {bcolors.OKCYAN}Store Credentials{bcolors.ENDC}\n"
              f"99) {bcolors.WARNING}Main Menu{bcolors.ENDC}"
              )
        choice = input(": ")
        match choice:
            case "1":
                while True:
                    name = input("[*] Name: ")
                    email = input("[*] Email: ")
                    conf = input("[*] You Have Entered '%s' As Your Name And '%s' As Your Email\n"
                                 "Is This Alright? (y/n): " % (name, email))
                    if conf == "y":
                        try:
                            subprocess.call("git config --global user.name '%s'" % name)
                            subprocess.call("git config --global user.email  '%s'" % email)
                            print("[*] Success!")
                            break
                        except subprocess.CalledProcessError as e:
                            print("[*] Error!")
                            logging.exception("[ Error While Setting Userames: %s ]" % e)
            case "2":
                texteditor = input("[*] Text Editor: ")
                try:
                    subprocess.call('git config --global core.editor "%s --wait"' % texteditor)
                    print("[*] Success!")
                except subprocess.CalledProcessError as e:
                    print("[*] Error!")
                    logging.exception("[ Error While Setting Userames: %s ]" % e)
            case "3":
                try:
                    subprocess.call('git config --global credential.helper store')
                    print("[*] Initialized Credential Store Tool.. Test Pulling From Origin..")
                    subprocess.run(f"git pull origin {subprocess.getoutput('git rev-parse --abbrev-ref HEAD')}")
                    print("[*] Success!")
                except subprocess.CalledProcessError as e:
                    print("[*] Error!")
                    logging.exception("[ Error While Configuring Credential Storer: %s ]" % e)
