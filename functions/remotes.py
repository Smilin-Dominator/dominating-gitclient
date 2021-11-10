from config import header, warning, input, print, get_branch, enter_prompt, info
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
                call(f"git remote add {name} '{location}'", shell=True)
                enter_prompt()
                break
            except KeyboardInterrupt:
                break

    def rename_remote():
        while True:
            try:
                name = input("\tName Of The Remote You Want To Rename?", choices=set_header("g"), override="cornsilk1")
                new = input("\tNew Name", override="misty_rose3")
                if " " in new:
                    warning("You Cannot Have Spaces In A Remote Name!")
                    continue
                call(f"git remote rename {name} {new}", shell=True)
                break
            except KeyboardInterrupt:
                break

    def change_remote_url():
        while True:
            try:
                remote = input("\tName Of The Remote?", choices=set_header("g"), override="indian_red1")
                new = input("\tNew URL", override="deep_pink2")
                if " " in new:
                    warning("You Cannot Have Spaces In A Remote URL!")
                    continue
                call(f"git remote set-url {remote} '{new}'")
                break
            except KeyboardInterrupt:
                break

    def delete_remote():
        try:
            remote = input("\tName Of The Remote?", choices=set_header("g"), override="indian_red1")
            call(f"git remote remove {remote}")
        except KeyboardInterrupt:
            pass

    def describe_remote():
        try:
            remote = input("\tName Of The Remote?", choices=set_header("g"), override="indian_red1")
            branches = getoutput(f"git ls-remote --heads {remote}").splitlines()
            info(f"Remote Name: [khaki3]{remote}[/khaki3]")
            info(f"Remote URL: {getoutput(f'git remote get-url {remote}')}")
            branch_list = []
            for branch in branches:
                branch_list.append(branch.split("\t")[1][11:])
            info(f"Branches: '{', '.join(branch_list)}'")
            enter_prompt()
        except KeyboardInterrupt:
            pass

    print(
        """
        1) Add A Remote
        2) Rename A Remote
        3) Change A Remote's URL
        4) Delete A Remote
        5) Describe A Remote
        """
    )
    try:
        choice = int(input("\tChoice", override="light_steel_blue1", choices=["1", "2", "3", "4", "5"]))
        match choice:
            case 1:
                add_remote()
            case 2:
                rename_remote()
            case 3:
                change_remote_url()
            case 4:
                delete_remote()
            case 5:
                describe_remote()
    except TypeError:
        pass
    except KeyboardInterrupt:
        pass


def fetch():
    call(["git", "fetch", "--all"], shell=True, stdout=DEVNULL, stderr=DEVNULL)


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
            if log.startswith(f"fatal: The current branch {get_branch()} has no upstream branch"):
                warning("Your branch doesn't have an upstream branch")
                conf = input("\tWould you like to set it upstream?", choices=["y", "n"])
                if conf == "y":
                    set_branch_upstream(get_branch(), remotes[0])
            else:
                print(log)
        else:
            remote = input("Which Remote Do You Want To Pull From?", choices=remotes, override="dark_orange")
            call(f"git pull {remote} {get_branch()}")
        enter_prompt()
    except KeyboardInterrupt:
        pass
