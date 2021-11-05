from functions.patch import *
from config import input, print


def main():
    while True:
        set_header()
        print(
            """
        1) Create Patch from Unstaged Changes
        2) Create Patch from Staged Changes
        3) Create Patch from Branch
        4) Apply Patch From File
        ..
        99) Previous Menu
            """
        )
        try:
            choice = int(input("\tChoice", choices=["1", "2", "3", "4", "99"]))
            match choice:
                case 1:
                    unstaged()
                case 2:
                    set_header()
                case 3:
                    branch()
                case 4:
                    apply_from_file()
                case 99:
                    break
        except TypeError:
            pass
