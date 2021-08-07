import yaml
import os
from configuration.colours import bcolors


def append_codenames():
    with open("codenames.yml", "r") as stream:
        dictionary = yaml.load(stream, Loader=yaml.FullLoader)
        print(f"{bcolors.OKGREEN}[*] Current Codes:{bcolors.ENDC}")
        print(dictionary)
        print(f"{bcolors.OKBLUE}[!] Press \'Ctrl+C\' when done!{bcolors.ENDC}")
        while True:
            try:
                code = input("Code: ")
                path = input("Path: ")
                if code in dictionary.keys():
                    cont = input(f"{bcolors.WARNING}[!] Code Exists.. Would You Like To Overwrite? (y/n): "
                                 f"{bcolors.ENDC}")
                    if cont == "y":
                        dictionary[code] = path
                else:
                    dictionary[code] = path
            except KeyboardInterrupt:
                break
    with open("codenames.yml", "w") as stream:
        yaml.dump(dictionary, stream)
        print(f"\n{bcolors.OKGREEN}[$] Success!{bcolors.ENDC}")


def write_codenames():
    with open("codenames.yml", 'w+') as stream:
        print("[*] No Codename File Found..Creating...")
        print("[!] Press \'Ctrl+C\' when done!")
        dictionary = {"here": os.getcwd()}
        while True:
            try:
                code = input("Code: ")
                path = input("Path: ")
                dictionary[code] = path
            except KeyboardInterrupt:
                break
        yaml.dump(dictionary, stream)
        print("[$] Success!")
    return dictionary


def read_codenames():
    try:
        with open("codenames.yml", "r") as codefile:
            ya = yaml.load(codefile, Loader=yaml.FullLoader)
            return ya
    except FileNotFoundError:
        return write_codenames()
