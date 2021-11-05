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
                    stash()
                case 2:
                    apply_stash(False)
                case 3:
                    apply_stash(True)
                case 4:
                    drop_stash()
                case 5:
                    branch_from_stash()
                case 99:
                    break
        except TypeError:
            pass
