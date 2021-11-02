from subprocess import call, getoutput
from config import header, print, input


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
            call(f"git checkout --track {branch}")
        elif (branch in r) and (branch.strip("origin/") in l):
            call(f"git checkout {branch.strip('origin/')}")
        else:
            call (f"git checkout {branch}")
        input("")
    except KeyboardInterrupt:
        pass
