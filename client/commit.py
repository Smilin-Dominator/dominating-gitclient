from functions.get_files import *
from config import header, input


def set_header():
    sf, mf, nf, df = "", "", "", ""
    if staged_files():
        sf = f"[dark_turquoise][ Staged Files: {staged_files()} ][/dark_turquoise]"
    if modified_files():
        mf = f"[medium_spring_green][ Modified Files: {modified_files()} ][/medium_spring_green]"
    if new_files():
        nf = f"[steel_blue1][ New Files: {new_files()} ][/steel_blue1]"
    if deleted_files():
        df = f"[dark_magenta][ Deleted Files: {deleted_files()} ][/dark_magenta]"
    header(sf, mf, nf, df)


def main():
    while True:
        set_header()
        print(
            """
        1) Stage Files
        2) Commit
        3) Reset Changes
        4) Difference (Staged)
        ..
        99) Quit
            """
        )
        choice = int(input("\tChoice", choices=["1", "2", "3", "99"]))
        match choice:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 99:
                break
