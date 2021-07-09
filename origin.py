import subprocess


def main(syner):
    choice = input(": ")
    match choice:
        case "1":
            print(f"\n{subprocess.getoutput('git pull origin')}\n")
        case "2":
            print(f"\n{subprocess.getoutput('git push origin')}\n")
        case "3":
            print(f"\n{subprocess.getoutput('git status')}\n")
        case "4":
            print(f"\n{subprocess.getoutput('git fetch origin')}\n")
        case "5":
            quit(0)
        case _:
            print(syner("Wrong Command."))