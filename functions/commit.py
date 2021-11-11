from config import input, print, console, syntax
from sys import stdout
from subprocess import call, DEVNULL, getoutput


def stage_files(get_files):
    """
    Prints a list of modified, new, deleted and staged files and allows you to change their status

    :param get_files: The function get_files()
    :return:
    """
    while True:
        files = get_files("g")
        staged = files[0]
        modified = files[1]
        new = files[2]
        deleted = files[3]
        mega = list(staged + modified + new + deleted)
        mega.sort()
        num = 0
        print("\n")
        for index, file in enumerate(mega):
            if (bool(file in staged and modified)) and (mega.count(file) == 2):
                print(f"\t{index}) SM: {file}")
                mega.reverse()
                mega.remove(file)
                mega.reverse()
            elif file in staged:
                print(f"\t{index}) S: {file}")
            else:
                if file in new:
                    print(f"\t{index}) N: {file}")
                elif file in modified:
                    print(f"\t{index}) M: {file}")
                elif file in deleted:
                    print(f"\t{index}) D: {file}")
            num += 1
        try:
            print("\n\t")
            choice = int(input("\tIndex (Ctrl+C to Stop)", choices=[str(i) for i in range(num)]))
            file = mega[choice]
            if file in staged:
                if file in modified:
                    call(f"git stage \"{file}\"", shell=True, stdout=DEVNULL)
                else:
                    call(f"git restore --staged \"{file}\"", shell=True, stdout=DEVNULL)
            else:
                call(f"git stage \"{file}\"", shell=True, stdout=DEVNULL)
            for i in range(3 + 2 + num):
                stdout.write('\x1b[1A')
                stdout.write('\x1b[2K')
        except KeyboardInterrupt:
            break


def reset(files):
    """
    Resets a file to HEAD

    :param files: The list of files
    """
    staged = files[0]
    modified = files[1]
    new = files[2]
    deleted = files[3]
    mega = list(staged + modified + new + deleted)
    mega.sort()
    num = 0
    print("\n")
    for index, file in enumerate(mega):
        if (bool(file in staged and modified)) and (mega.count(file) == 2):
            print(f"\t{index}) SM: {file}")
            mega.reverse()
            mega.remove(file)
            mega.reverse()
        elif file in staged:
            print(f"\t{index}) S: {file}")
        else:
            if file in new:
                print(f"\t{index}) N: {file}")
            elif file in modified:
                print(f"\t{index}) M: {file}")
            elif file in deleted:
                print(f"\t{index}) D: {file}")
        num += 1
    try:
        print("\n\t")
        choice = int(input("\tIndex (Ctrl+C to Abort)", choices=[str(i) for i in range(num)]))
        file = mega[choice]
        call(f"git checkout HEAD -- \"{file}\"", shell=True)
    except KeyboardInterrupt:
        pass


def commit():
    """Commits the staged files"""
    call("git commit", shell=True, stdout=DEVNULL, stderr=DEVNULL)


def diff_staged():
    """Pages the difference of staged files"""
    with console.pager(styles=True):
        out = syntax(getoutput("git diff --staged"), background_color="default", lexer_name="diff")
        console.print(out)
    input("(enter to continue)", override="red")


def diff():
    """Pages the difference of all files"""
    with console.pager(styles=True):
        out = syntax(getoutput("git diff"), background_color="default", lexer_name="diff")
        console.print(out)
    input("(enter to continue)", override="red")
