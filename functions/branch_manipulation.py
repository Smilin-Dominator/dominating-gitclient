from subprocess import call, getoutput
from config import header


def set_header():
    local = getoutput("git for-each-ref --format='%(refname:short)' refs/heads").splitlines()
    remote = getoutput("git for-each-ref --format='%(refname:short)' refs/remotes").splitlines()
    header(
        f"[honeydew2][ Local Branches: [bold]{', '.join(local)}[/bold] ][/honeydew2]",
        f"[light_cyan1][ Remote Branches: [bold]{', '.join(remote)}[/bold] ][/light_cyan1]"
    )


def checkout():
    call("git checkout {branch}", shell=True)

