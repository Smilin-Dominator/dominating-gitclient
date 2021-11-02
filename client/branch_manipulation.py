from config import input, print
from functions.branch_manipulation import *


def main():
    while True:
        set_header()
        print("""
        1) Checkout Branch
        2) Create Branch
        3) Merge Branches
        4) Delete Branches
        ..
        99) Previous Menu
                """)
        try:
            choice = int(input("\tChoice", choices=["1", "2", "3", "4", "99"]))
            match choice:
                case 1:
                    checkout()
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
