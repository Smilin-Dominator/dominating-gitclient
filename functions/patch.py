from config import print, header, input
from subprocess import call, DEVNULL, getoutput


def set_header():
    header()


def patch_message() -> str:
    return input("\tPatch Message", override="medium_purple3").replace(" ", "_")


def unstaged():
    msg = patch_message()
    call(f"git diff > {msg}.patch", shell=True, stdout=DEVNULL, stderr=DEVNULL)


def staged():
    msg = patch_message()
    call(f"git diff --staged > {msg}.patch", shell=True, stdout=DEVNULL, stderr=DEVNULL)


def branch():
    msg = patch_message()
    branches = getoutput("git for-each-ref --format='%(refname:short)' refs/heads").splitlines()
    branch = input("Which branch do you want to create a patch of?", override="pale_turquoise4", choices=branches)
    call(f"git diff {branch} > {msg}.patch")
