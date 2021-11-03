from functions.remotes import *
from config import print


def main():
    while True:
        set_header()
        print("""
        1) Push
        2) Pull
        3) Fetch
        4) Manage Remotes
        ..
        99) Previous Menu
            """)
        try:
            choice = int(input("\tChoice", choices=["1", "2", "3", "4", "5", "99"]))
            match choice:
                case 1:
                    push()
                case 2:
                    pull()
                case 3:
                    pass
                case 4:
                    pass
                case 99:
                    break
        except TypeError:
            pass
