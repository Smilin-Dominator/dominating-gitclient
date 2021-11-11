from subprocess import getoutput, call, DEVNULL
from config import header, input, warning, enter_prompt


def get_stashes():
    """Returns the stash list"""
    return getoutput("git stash list").splitlines()


def set_header():
    """Sets the header with the stash list"""
    stashes = get_stashes()
    stash_messages = [line.split(": ")[2].strip("'") for line in stashes]
    header(
        f"[tan][ Stashes: '{', '.join(stash_messages)}' ][/tan]"
    )


def get_index(message: str) -> int:
    """
    Finds the index of the stash with a message

    :param message: the message of the stash
    :return: The index
    """
    stashes = get_stashes()
    for line in stashes:
        line = line.split(": ")
        if line[2].strip("'") == message:
            return int(line[0].strip("stash@{}"))


def stash(message: str = None):
    """Stashes Your Changes"""
    if message is not None:
        message = message
    else:
        message = input("\tMessage", override="red")
    call(f"git stash -m '{message}'", shell=True, stderr=DEVNULL, stdout=DEVNULL)


def apply_stash(pop: bool):
    """Applies or Pops A Stash"""
    stashes = get_stashes()
    if len(stashes) == 0:
        warning("You Have No Stashes")
    else:
        stashes = [line.split(": ")[2].strip("'") for line in stashes]
        try:
            st = input("\tWhich Stash Would You Like To Apply?", choices=stashes, override="orange1")
            if pop:
                call(f"git stash pop {get_index(st)}", shell=True)
            else:
                call(f"git stash apply {get_index(st)}", shell=True)
        except KeyboardInterrupt:
            pass
    enter_prompt()


def drop_stash():
    """Removes a stash permanently"""
    stashes = [line.split(": ")[2].strip("'") for line in get_stashes()]
    if len(stashes) == 0:
        warning("You Have No Stashes")
    else:
        try:
            st = input("\tWhich Stash Do You Want To Drop?", choices=stashes, override="orange1")
            call(f"git stash drop {get_index(st)}", shell=True)
        except KeyboardInterrupt:
            pass
    enter_prompt()


def branch_from_stash():
    """Creates a branch from a stash"""
    while True:
        stashes = [line.split(": ")[2].strip("'") for line in get_stashes()]
        if len(stashes) == 0:
            warning("You Have No Stashes")
        else:
            try:
                name = input("\tName Of New Branch", override="grey84")
                if " " in name:
                    warning("Cannot have spaces in a branch name")
                    continue
                st = input("\tWhich Stash Do You Want To Use? (warning: will get deleted)", override="tan", choices=stashes)
                call(f"git stash branch {name} {get_index(st)}")
                break
            except KeyboardInterrupt:
                pass
