from subprocess import getoutput
from client.first_time import main as setup
from client.main import main as cl
from functions.configuration import Config
from config import warning, error, info, input, enter_prompt
from sys import argv, exit
from os import chdir
from subprocess import call, DEVNULL
from pathlib import Path


def first_time_check():
    """
    This just checks if you're in a git repo, and if not, launches functions.first_time.main()
    :return: Nothing
    """
    key = getoutput("git rev-parse --is-inside-work-tree")
    if key == "fatal: not a git repository (or any of the parent directories): .git":
        setup()


def config() -> [str, tuple[dict]]:
    """
    This parses the config.json file

    if `update_check_frequency` is not 0 (which is never update), and the number in count.txt is equal to the
    number specified in `update_check_frequency`, it checks for an update and if there is one, asks for confirmation.

    if there's a KeyError (which may occur if the client has the latest version and an outdated Config or no config at
    all or tampered), it'll rewrite the config.

    :return: The Default Directory (String) and the Aliases (Tuple of Dicts)
    """
    def update():
        """
        This function updates if the number in count.txt is equal to the specified number and there's an update available.
        :return: Nothing
        """
        number = ar['update_check_frequency']
        count = Path(str(conf.file)[:-11], "count.txt")
        try:
            with open(count, "r") as b:
                num = int(b.read())
                if num == number:
                    call("git fetch origin", shell=True, stdout=DEVNULL)
                    lines = getoutput("git status").splitlines()
                    if not lines[1].startswith("Your branch is behind"):
                        info("Program is up to date")
                        enter_prompt()
                    else:
                        up = input("\tUpdate Found, Would You Like To Update?", override="red", choices=["y", "n"],
                                   default="y")
                        if up:
                            call("git pull origin master", shell=True)
                    write(count, "1")
                else:
                    write(count, str(num + 1))
        except FileNotFoundError:
            with open(count, "w") as b:
                write(count, "1")

    def write(file: Path, contents: str):
        """
        This function writes to a file, flushes and closes
        :param file: A Path Object, which is the path to the file
        :param contents: The Contents To Write To The File
        :return: Nothing
        """
        fil = open(file, "w")
        fil.write(contents)
        fil.flush()
        fil.close()

    conf = Config()
    ar = conf.parse_config()
    try:
        if ar['update_check_frequency'] != 0:
            update()
        return ar['default_dir'], ar['aliases']
    except KeyError:
        error("There's been an unsatisfied option, rebuilding config")
        conf.write_config()


if __name__ == "__main__":
    default, aliases = config()
    directory = ""
    try:
        if len(argv) < 2:
            directory = default
            chdir(directory)
        else:
            for entry in aliases:
                if entry['Name'] == argv[1]:
                    directory = entry['Directory']
                    break
            else:
                directory = argv[1]
            chdir(directory)
    except FileNotFoundError:
        error(f"Directory '{directory}' Not Found!")
        exit(2)
    first_time_check()
    cl()
