from subprocess import getoutput


def staged():
    return getoutput("git diff --name-only --staged")


def modified():
    return getoutput("git ls-files -m")


def deleted():
    return getoutput("git ls-files -d")


def untracked():
    return getoutput("git ls-files -o")
