import os
import sys
import client


def syner(er):
    return f"[*] Invalid Syntax: {er}"


def interface():
    codenames = {
        "mysql": r"C:\Users\Devisha\Documents\GitHub\mysql-and-python-billing",
        "devios": r"C:\Users\Devisha\Documents\GitHub\DeviOS",
        "coding_projects": r"C:\Users\Devisha\Documents\GitHub\coding-projects",
        "devicoin": r"C:\Users\Devisha\Documents\GitHub\flask_project",
        "here": r"C:\Users\Devisha\Documents\GitHub\GitClient"
    }
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
