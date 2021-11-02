import time
from subprocess import call, getoutput, DEVNULL
from config import header, print, input, track, get_branch, syntax, console
from .stashes import get_index, stash
from time import sleep


def cloud_save(branch: str, options=None):
    call(f"git stash -m 'gc_temp'", shell=True, stdout=DEVNULL, stderr=DEVNULL)
    if options is not None:
        call(["git", "checkout", options, branch], shell=True, stdout=DEVNULL, stderr=DEVNULL)
    else:
        call(["git", "checkout", branch], shell=True, stdout=DEVNULL, stderr=DEVNULL)
    call(f"git stash pop {get_index('gc_temp')}", shell=True, stdout=DEVNULL, stderr=DEVNULL)


def set_header(get=None):
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

    def merge_func(branch: str):
        log = getoutput(f"git merge {branch}")
        with console.pager(styles=True):
            out = syntax(log, background_color="default", lexer_name="diff")
            console.print(out)
        return log

    try:
        conf = input("\t[*] Do You Want To Merge Into This Branch or Checkout Another?", choices=["this", "checkout"])
        if conf == "checkout":
            checkout()
        local, _ = set_header("f")
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
