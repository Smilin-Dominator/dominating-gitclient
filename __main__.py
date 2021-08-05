import os
import sys
import client
import yaml


def syner(er):
    return f"[*] Invalid Syntax: {er}"


def read_codenames():
    try:
        with open("codenames.txt", "r") as codefile:
            ya = yaml.load(codefile, Loader=yaml.FullLoader)
            return ya
    except FileNotFoundError:
        print("[*] No Codename File Found..Creating...")
        print("[!] Type \'done\' when it asks for code, to finish!")
        dictionary = {}
        while True:
            code = input("Code: ")
            if code == "done":
                break
            else:
                path = input("Path: ")
                dictionary[code] = dictionary[path]
        yaml.dump(dictionary, open("codenames.txt", 'w'))
        print("Success!")


def interface():
    codenames = read_codenames()
    if len(sys.argv) < 2:
        print(syner("Not Enough Arguments."))
        return False
    else:
        exe = 0
        for file in os.listdir('.'):
            if file.endswith(".exe"):
                exe = 1
                break
        if sys.argv[1] == "-h" and exe == 0:
            print(f"Syntax: 'python3 gitclient <dir>'\n\nCode Names: {codenames}\n\nIf you do not want to use codenames"
                  f" you may enter the absolute path of the directory.")
            sys.exit(1)
        elif sys.argv[1] == "-h" and exe == 1:
            print(f"Syntax: './__main__.exe <dir>'\n\nCode Names: {codenames}\n\nIf you do not want to use codenames"
                  f" you may enter the absolute path of the directory.")
        else:
            choice = sys.argv[1]
            try:
                path = os.path.join(codenames[choice])
                if os.path.exists(path):
                    return path
                else:
                    print(syner("Wrong Path"))
                    return False
            except os.error:
                if os.path.exists(choice):
                    return os.path.join(choice)
                else:
                    print(syner("Wrong Path"))
                    return False


if __name__ == '__main__':
    proceed = interface()
    if proceed:
        client.main(proceed)
    else:
        sys.exit(2)
