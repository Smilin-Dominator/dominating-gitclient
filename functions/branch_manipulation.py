from subprocess import call, getoutput, DEVNULL
from config import header, print, input, track
from .stashes import get_index
from time import sleep


def cloud_save(branch: str):
    call(f"git stash -m 'gc_temp'", shell=True, stdout=DEVNULL, stderr=DEVNULL)
    call(f"git checkout {branch}", shell=True, stdout=DEVNULL, stderr=DEVNULL)
    call(f"git stash pop {get_index('gc_temp')}")


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
            call(f"git checkout --track {branch}", shell=True, stdout=DEVNULL, stderr=DEVNULL)
        elif (branch in r) and (branch.strip("origin/") in l):
            call(f"git checkout {branch.strip('origin/')}", shell=True, stdout=DEVNULL, stderr=DEVNULL)
        else:
            call (f"git checkout {branch}", shell=True, stdout=DEVNULL, stderr=DEVNULL)
        input("")
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
                        sleep(0.02)
                input("\t[*] Success! Press (enter) to continue")
                break
        except KeyboardInterrupt:
            break
