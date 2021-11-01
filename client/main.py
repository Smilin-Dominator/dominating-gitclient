from sys import exit
from config import header, print, input, error, warning
from .commit import main as com


def main():
    header()
    print("""
        1) Commit Functions
        2) Branch Functions
        3) Remote Management
        4) Stash Management
        5) Commit Log
        ..
        99) Quit
    """)
    try:
        choice = int(input("\td"))
        match choice:
            case 1:
                com()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 99:
                exit(0)
            case _:
                warning("Number doesn't match")
    except ValueError:
        error("Didn't enter an integer during the main selection")
