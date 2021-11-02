from subprocess import getoutput


def get_index(message: str) -> int:
    stash = getoutput("git stash list").splitlines()
    for line in stash:
        line = line.split(": ")
        if line[2].strip("'") == message:
            return int(line[0].strip("stash@{}"))