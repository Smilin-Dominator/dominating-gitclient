from config import header, warning, input, print, get_branch, enter_prompt
from subprocess import getoutput, call, DEVNULL


def set_header(get=None):
    remotes = getoutput('git remote').splitlines()
    if get is None:
        header(
            f"[light_steel_blue1][ Remotes: '{', '.join(remotes)}' ][/light_steel_blue1]"
        )
    else:
        return remotes


def set_branch_upstream(branch=None, remote=None):
    if branch and remote is None:
        pass
    else:
        call(f"git push --set-upstream {remote} {branch}", shell=True)


def manage_remotes():

    def add_remote():
        while True:
            try:
                name = input("\tThe Name Of The New Remote", override="plum2")
                if " " in name:
                    warning("You cannot have spaces in a remote name!")
                    continue
                location = input("\tThe Address (Link)", override="orange1")
                if " " in location:
                    warning("You cannot have spaces in a link!")
                    continue
                call(f"git remote add {name} {location}", shell=True)
                break
            except KeyboardInterrupt:
                break

    while True:
        print(
            """
        1) Add A Remote
        2) Rename A Remote
        3) Change A Remote's URL
        4) Delete A Remote
        ..
        99) Previous Menu
            """
        )
        try:
            choice = int(input("\tChoice", override="light_steel_blue1", choices=["1", "2", "3", "4", "99"]))
            match choice:
                case 1:
                    add_remote()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 99:
                    break
        except TypeError:
            pass
        except KeyboardInterrupt:
            break


def fetch():
    call(["git", "fetch"], shell=True, stdout=DEVNULL, stderr=DEVNULL)


def pull():
    try:
        remotes = set_header("get")
        if len(remotes) == 0:
            warning("You Don't Have A Remote!")
            conf = input("Would you like to setup one?", choices=["y", "n"])
            if conf == "y":
                manage_remotes()
        elif len(remotes) == 1:
            log = getoutput(f"git pull")
            print(log)
            if log.startswith("fatal: couldn't find remote ref"):
                warning("Your branch doesn't have an upstream branch")
                conf = input("Would you like to set it upstream?", choices=["y", "n"])
                if conf == "y":
                    set_branch_upstream(get_branch(), remotes[0])
        else:
            remote = input("Which Remote Do You Want To Pull From?", choices=remotes, override="dark_orange")
            call(f"git pull {remote} {get_branch()}")
        enter_prompt()
    except KeyboardInterrupt:
        pass


def push():
    try:
        remotes = set_header("get")
        if len(remotes) == 0:
            warning("You Don't Have A Remote!")
            conf = input("Would you like to setup one?", choices=["y", "n"])
            if conf == "y":
                manage_remotes()
        elif len(remotes) == 1:
            log = getoutput(f"git push")
            print(log)
            if log.startswith("fatal: couldn't find remote ref"):
                warning("Your branch doesn't have an upstream branch")
                conf = input("Would you like to set it upstream?", choices=["y", "n"])
                if conf == "y":
                    set_branch_upstream(get_branch(), remotes[0])
        else:
            remote = input("Which Remote Do You Want To Pull From?", choices=remotes, override="dark_orange")
            call(f"git pull {remote} {get_branch()}")
        enter_prompt()
    except KeyboardInterrupt:
        pass
