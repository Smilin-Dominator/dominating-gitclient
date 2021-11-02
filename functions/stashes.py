from subprocess import getoutput


def get_index(message: str) -> int:
    stash = getoutput("git stash list").splitlines()
    for line in stash:
        line = line.split(": ")
        if line[2] == message:
            return int(line[1].strip("stash@{}"))