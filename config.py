from rich.console import Console
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.progress import track
from subprocess import getoutput
from os import getcwd, system
from platform import system as plat
import logging


log_format = '%(asctime)s (%(filename)s): %(message)s'
logging.basicConfig(filename="log.txt", format=log_format)

# ----------- Rich / Colour Related ----------------------------------- #
console = Console(color_system="256")
syntax = Syntax
track = track
platform = plat()


def print(prompt, override: str = None) -> None:
    """
    This replaces print with rich's console.print(), which allows styling with colours

    :param prompt: The Text To Display
    :param override: Style the text with this colour / effect
    """
    if override is not None:
        console.print(f"[{override}]{prompt}[/{override}]")
    else:
        console.print(f"{prompt}")


def error(msg: str, override: str = None) -> None:
    """
    This is the same as print but styles the text as white on a red background and logs msg as an error

    :param msg: The Text To Display
    :param override: Style the text with this colour / effect
    """
    if override is None:
        print(f"\t[white on red][@] {msg}[/white on red]")
    else:
        print(f"\t[{override}][@] {msg}[/{override}]")
    logging.error(f"{msg}\nLocals: {locals()}")


def warning(msg: str, override: str = None) -> None:
    """
    Same as print but styles it as white on a yellow and logs msg as a warning

    :param msg: The Text To Display
    :param override: Style the text with this colour / effect
    """
    if override is None:
        print(f"\t[white on yellow][!] {msg}[/white on yellow]")
    else:
        print(f"\t[{override}][!] {msg}[/{override}]")
    logging.warning(msg)


def info(msg: str, override: str = None) -> None:
    """
    Same as print but prefixes it with [?]

    :param msg:
    :param override:
    """
    if override is not None:
        print(f"\t[{override}][?] {msg}[/{override}]")
    else:
        print(f"\t[?] {msg}")


def input(prompt: str, override: str = None, default=None, password=False, choices=None) -> str:
    """
    This is a very advanced input prompt which uses rich's prompt function

    :param prompt: The Message To Display
    :param override: Colours To Surround The Prompt In
    :param default: The Default Value (Comes When You Hit Enter)
    :param password: If set to true, hides the input
    :param choices: The prompt will loop until one of these choices are entered
    :return:
    """
    if override is not None:
        return Prompt.ask(f"[{override}]{prompt}[/{override}]", default=default, password=password, choices=choices)
    else:
        return Prompt.ask(f"{prompt}", default=default, password=password, choices=choices)


def enter_prompt():
    """An Enter Prompt"""
    input("\t[*] Click (enter) to continue", override="tan")


# ---------------------- Other Functions ---------------------------------------
def last_commit() -> str:
    """
    Returns the last commit's subject

    :return: the last commit's subject
    """
    raw = getoutput('git log -1 --pretty=%B')
    new = raw.splitlines()[0]
    if raw.startswith("fatal"):
        return "None"
    else:
        return new


def get_branch() -> str:
    """
    Checks and returns the current branch

    :return: the current branch
    """
    raw = getoutput('git rev-parse --abbrev-ref HEAD')
    if raw.startswith("fatal"):
        return "None"
    else:
        return raw


def header(*modules: str):
    """
    Sets the header, by clearing the screen and drawing Smilin' Dominator and displaying modules

    :param modules: Modules to add (eg: '[red]Something[/red]')
    """
    modules = list(modules)
    for i in range(modules.count("")):
        modules.remove("")
    modules = "\n\t".join(modules)
    if platform == "Windows":
        system("cls")
    else:
        system("clear")
    print(f"""[pale_turquoise1]
             .oooooo..o                    o8o  oooo   o8o              o8o                                  
            d8P'    `Y8                    `"'  `888   `"'              `YP                                  
            Y88bo.      ooo. .oo.  .oo.   oooo   888  oooo  ooo. .oo.    '                                   
             `"Y8888o.  `888P"Y88bP"Y88b  `888   888  `888  `888P"Y88b                                       
                 `"Y88b  888   888   888   888   888   888   888   888                                       
            oo     .d8P  888   888   888   888   888   888   888   888                                       
            8""88888P'  o888o o888o o888o o888o o888o o888o o888o o888o                                      
            oooooooooo.                                o8o                            .                      
            `888'   `Y8b                               `"'                          .o8                      
             888      888  .ooooo.  ooo. .oo.  .oo.   oooo  ooo. .oo.    .oooo.   .o888oo  .ooooo.  oooo d8b 
             888      888 d88' `88b `888P"Y88bP"Y88b  `888  `888P"Y88b  `P  )88b    888   d88' `88b `888""8P 
             888      888 888   888  888   888   888   888   888   888   .oP"888    888   888   888  888     
             888     d88' 888   888  888   888   888   888   888   888  d8(  888    888 . 888   888  888     
            o888bood8P'   `Y8bod8P' o888o o888o o888o o888o o888o o888o `Y888""8o   "888" `Y8bod8P' d888b [/pale_turquoise1]
        
        [hot_pink2][ Directory: [bold]"{getcwd()}"[/bold] ][/hot_pink2]
        [khaki3][ Branch: [bold]"{get_branch()}"[/bold] ][/khaki3]
        [medium_purple1][ Last Commit: [bold]"{last_commit()}"[/bold] ][/medium_purple1]
        {modules}
        """)
