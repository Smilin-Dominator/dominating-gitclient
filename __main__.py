import os
import sys
import client
from codename_config import read_codenames, write_codenames


def syntax_error(er):
    return f"[*] Invalid Syntax: {er}"


def interface():
    if os.path.exists("codenames.yml"):
        codenames = read_codenames()
    else:
        codenames = write_codenames()
    if len(sys.argv) < 2:
        print(syntax_error("Not Enough Arguments."))
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
                    print(syntax_error("Wrong Path"))
                    return False
            except KeyError:
                if os.path.exists(choice):
                    return os.path.join(choice)
                else:
                    print(syntax_error("Wrong Path"))
                    return False


if __name__ == '__main__':
    proceed = interface()
    if proceed:
        client.main(proceed)
    else:
        sys.exit(2)
