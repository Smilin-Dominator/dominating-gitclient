from sys import exit
from config import header, print, input, error, warning
from .commit import main as com
from .git_log import main as lg
from .remote import main as r
from .branch_manipulation import main as br


def main():
    while True:
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
            choice = int(input("\tChoice", choices=["1", "2", "3", "4", "5", "99"]))
            match choice:
                case 1:
                    com()
                case 2:
                    br()
                case 3:
                    r()
                case 4:
                    pass
                case 5:
                    lg()
                case 99:
                    exit(0)
        except TypeError:
            pass