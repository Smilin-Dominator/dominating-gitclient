from subprocess import getoutput


def modified_files():
    return getoutput("git ls-files -m").splitlines()


def new_files():
    return getoutput("git ls-files -o --exclude-standard").splitlines()


def deleted_files():
    return getoutput("git ls-files -d").splitlines()


def staged_files():
    return getoutput("git diff --name-only --cached").splitlines()
