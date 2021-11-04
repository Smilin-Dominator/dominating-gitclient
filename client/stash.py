from functions.stashes import *
from config import print, input


def main():
    while True:
        try:
            set_header()
            print("""
        1) Stash Your Changes
        2) Apply A Stash
        3) Pop A Stash
        4) Remove A Stash
        5) Create A Branch From A Stash
        ..
        99) Previous Menu
            """)
            choice = int(input("\tChoice", choices=["1", "2", "3", "4", "5", "99"]))
            match choice:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 99:
                    break
        except TypeError:
            pass
