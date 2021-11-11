import time
from subprocess import call, getoutput, DEVNULL
from time import sleep

from config import header, print, input, track, get_branch, syntax, console
from .stashes import get_index, stash


def cloud_save(branch: str, options=None):
    """
    Stashes Current Working Directory, Checks Out Branch and Pops The Stash

    :param branch: The branch to checkout
    :param options: options in the command, such as '--track'
    """
    call(f"git stash -m 'gc_temp'", shell=True, stdout=DEVNULL, stderr=DEVNULL)
    if options is not None:
        call(["git", "checkout", options, branch], shell=True, stdout=DEVNULL, stderr=DEVNULL)
    else:
        call(["git", "checkout", branch], shell=True, stdout=DEVNULL, stderr=DEVNULL)
    call(f"git stash pop {get_index('gc_temp')}", shell=True, stdout=DEVNULL, stderr=DEVNULL)


def set_header(get=None):
    """
    Sets the header or returns the branch list

    :param get: If this is None, it sets the header
    :return: If get is not None, it returns the list of local and remote branches
    """
    local = getoutput("git for-each-ref --format='%(refname:short)' refs/heads").splitlines()
    remote = getoutput("git for-each-ref --format='%(refname:short)' refs/remotes").splitlines()
    if get is None:
        header(
            f"[honeydew2][ Local Branches: [bold]{', '.join(local)}[/bold] ][/honeydew2]",
            f"[light_cyan1][ Remote Branches: [bold]{', '.join(remote)}[/bold] ][/light_cyan1]"
        )
    else:
        return local, remote


def display_branches() -> tuple[list[str], list[str]]:
    """
    This prints the branch list in order and returns a tuple, so the displayed index is the real index of the tuple

    :return: Local and Remote Branch Lists respectively
    """
    local, remote = set_header("get")
    print("\n\tLocal Branches:", override="spring_green2")
    index = 0
    for branch in local:
        print(f"\t\t{index}) {branch}", override="dark_turquoise")
        index += 1
    print("\n\tRemote Branches:", override="spring_green2")
    for branch in remote:
        print(f"\t\t{index}) {branch}", override="dark_turquoise")
        index += 1
    return local, remote


def checkout():
    """
    Checks out a branch using cloudsave() and tracks the branch if its a remote branch which
    doesn't have a local branch.
    """
    l, r = display_branches()
    all = l + r
    length = len(all)
    try:
        choice = int(input("\n\tChoice (Ctrl+C to Abort): ", choices=[str(i) for i in range(length)]))
        branch = all[choice].strip("'")
        if (branch in r) and (branch.strip("origin/") not in l):
            cloud_save(branch, "--track")
        elif (branch in r) and (branch.strip("origin/") in l):
            cloud_save(branch.strip("origin/"))
        else:
            cloud_save(branch)
    except KeyboardInterrupt:
        pass


def create_branch():
    """
    Creates a branch and resets the process if it detects that there's a space in the name
    """
    while True:
        try:
            name = input("\tName of New Branch (Ctrl+C To Abort)", override="green1")
            if " " in name:
                print("\t[!] Name With Space Not Allowed!", override="tan")
            else:
                print(f"\t[*] Making branch '{name}'")
                conf = input("\t[*] Proceed?", choices=["y", "n"])
                if conf == "n":
                    break
                conf = input("\t[*] Would you like to checkout the branch?", choices=["y", "n"])
                if conf == "y":
                    rg = 100
                else:
                    rg = 50
                for n in track(range(rg), description="\tSetting Up Branch"):
                    if n == 25:
                        call(f"git branch {name}", shell=True, stdout=DEVNULL, stderr=DEVNULL)
                    elif n == 30 and conf == "y":
                        cloud_save(name)
                    elif n == 40:
                        call("git fetch")
                    else:
                        sleep(0.002)
                input("\t[*] Success! Press (enter) to continue")
                break
        except KeyboardInterrupt:
            break


def merge():
    """
    Merges two branches and prompts to stash if there are local changes
    """
    def merge_func(branch: str):
        log = getoutput(f"git merge {branch}")
        with console.pager(styles=True):
            out = syntax(log, background_color="default", lexer_name="diff")
            console.print(out)
        return log

    try:
        local, _ = set_header("f")
        if len(local) < 2:
            print("\t[*] Less Than Two Branches, Cannot Merge", override="yellow")
        else:
            conf = input("\t[*] Do You Want To Merge Into This Branch or Checkout Another?",
                         choices=["this", "checkout"])
            if conf == "checkout":
                checkout()
            local = [a.strip("'") for a in local]
            local.remove(get_branch())
            bra = input("\t[*] Which Branch Do You Want To Merge?", choices=local)
            log = merge_func(bra)
            if log.startswith("error:"):
                if log.startswith("error: Your local changes to the following files would be overwritten by merge:"):
                    choice = input("[*] Would You Like To Stash?", choices=["y", "n"])
                    if choice == "y":
                        stash(f"gitclient_merge_{get_branch()}_{bra}_{time.time()}")
                        merge_func(bra)
        input("\t[*] Click (enter) To Continue", override="tan")
    except KeyboardInterrupt:
        pass


def delete():
    """
    Deletes a branch
    """
    local, _ = set_header("get")
    local = [a.strip("'") for a in local]
    if len(local) < 2:
        print("\t[!] You cannot delete a branch when there's less than 2", override="yellow")
    else:
        local.remove(get_branch())
        branch = input("\tWhich Branch Do You Want To Delete?", choices=local)
        call(f"git branch -D {branch}", shell=True, stdout=DEVNULL, stdin=DEVNULL)
    input("\t[*] Click (enter) To Continue", override="tan")
