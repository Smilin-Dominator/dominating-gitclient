from itertools import chain
from config import input, print
from sys import stdout
from subprocess import call, DEVNULL


def stage_files(get_files):
    while True:
        files = get_files("g")
        staged = files[0]
        modified = files[1]
        new = files[2]
        deleted = files[3]
        mega = list(chain(staged, modified, new, deleted))
        mega.sort()
        num = 0
        print("\n")
        for index, file in enumerate(mega):
            if file in staged:
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
            print("\n")
            choice = int(input("\tIndex (Ctrl+C to Stop)", choices=[str(i) for i in range(num)]))
            file = mega[choice]
            if file in staged:
                call(f"git reset {file}", shell=True, stdout=DEVNULL)
            else:
                call(f"git stage {file}", shell=True, stdout=DEVNULL)
            for i in range(3 + 2 + num):
                stdout.write('\x1b[1A')
                stdout.write('\x1b[2K')
        except KeyboardInterrupt:
            break


def commit():
    call("git commit", shell=True, stdout=DEVNULL, stderr=DEVNULL)
