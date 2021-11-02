from config import input
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
                    create_branch()
                case 3:
                    merge()
                case 4:
                    pass
                case 99:
                    break
        except TypeError:
            pass
