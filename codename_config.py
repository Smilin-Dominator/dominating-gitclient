import yaml
import os


def append_codenames():
    with open("codenames.txt", "a+") as stream:
        dictionary = yaml.load(stream, yaml.FullLoader)
        print("[!] Press \'Ctrl+C\' when done!")
        while True:
            try:
                code = input("Code: ")
                path = input("Path: ")
                if code in dictionary.keys():
                    print("[!] Code Exists.. Would You Like To Overwrite?")
                dictionary[code] = path
            except KeyboardInterrupt:
                break
        yaml.dump(dictionary, stream)
        print("[$] Success!")


def write_codenames():
    with open("codenames.txt", 'w+') as stream:
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
        with open("codenames.txt", "r") as codefile:
            ya = yaml.load(codefile, Loader=yaml.FullLoader)
            return ya
    except FileNotFoundError:
        return write_codenames()
