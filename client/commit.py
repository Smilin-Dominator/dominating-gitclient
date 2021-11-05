from functions.get_files import *
from functions.commit import *
from config import header, input, print


def set_header(get=None):
    sf, mf, nf, df = "", "", "", ""
    if get is None:
        if staged_files():
            sf = f"[dark_turquoise][ Staged Files: {', '.join(staged_files())} ][/dark_turquoise]"
        if modified_files():
            mf = f"[medium_spring_green][ Modified Files: {', '.join(modified_files())} ][/medium_spring_green]"
        if new_files():
            nf = f"[steel_blue1][ New Files: {', '.join(new_files())} ][/steel_blue1]"
        if deleted_files():
            df = f"[dark_magenta][ Deleted Files: {', '.join(deleted_files())} ][/dark_magenta]"
        header(sf, mf, nf, df)
    else:
        return staged_files(), modified_files(), new_files(), deleted_files()


def main():
    while True:
        set_header()
        print(
            """
        1) Stage Files
        2) Commit
        3) Reset Changes
        4) Difference (Staged)
        5) Difference (All)
        ..
        99) Previous Menu
            """
        )
        try:
            choice = int(input("\tChoice", choices=["1", "2", "3", "4", "5", "99"]))
            match choice:
                case 1:
                    stage_files(set_header)
                case 2:
                    commit()
                case 3:
                    reset(set_header("get"))
                case 4:
                    diff_staged()
                case 5:
                    diff()
                case 99:
                    break
        except TypeError:
            pass
