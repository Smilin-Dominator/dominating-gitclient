from subprocess import getoutput, call, DEVNULL
from config import header, input


def get_stashes():
    return getoutput("git stash list").splitlines()


def set_header():
    stashes = get_stashes()
    stash_messages = [line.split(": ")[2] for line in stashes]
    header(
        f"[tan][ Stashes: '{', '.join(stash_messages)}' ][/tan]"
    )


def get_index(message: str) -> int:
    stashes = get_stashes()
    for line in stashes:
        line = line.split(": ")
        if line[2].strip("'") == message:
            return int(line[0].strip("stash@{}"))


def stash(message: str = None):
    if message is not None:
        message = message
    else:
        message = input("Message")
    call(f"git stash -m '{message}'", shell=True, stderr=DEVNULL, stdout=DEVNULL)