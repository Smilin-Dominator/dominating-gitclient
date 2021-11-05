from config import header, input, warning, enter_prompt
from os import path
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
    branches = [a.strip("'") for a in getoutput("git for-each-ref --format='%(refname:short)' refs/heads").splitlines()]
    bra = input("\tWhich branch do you want to create a patch of?", override="pale_turquoise4", choices=branches)
    call(f"git diff {bra} > {msg}.patch", shell=True)
    enter_prompt()


def apply_from_file():
    while True:
        try:
            p = input("\tAbsolute Path Of The Patch File", override="tan")
            if not path.exists(p):
                warning("Path Doesn't Exist!")
                continue
            call(f"git apply {p}", shell=True)
            enter_prompt()
            break
        except KeyboardInterrupt:
            break
