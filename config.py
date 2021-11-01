from rich.console import Console
from rich.prompt import Prompt
from subprocess import getoutput
from os import getcwd
import logging

log_format = '%(asctime)s (%(filename)s): %(message)s'
logging.basicConfig(filename="log.txt", format=log_format)

# ----------- Rich / Colour Related ----------------------------------- #
console = Console(color_system="256")


def print(prompt, override: str = None) -> None:
    if override is not None:
        console.print(f"[{override}]{prompt}[/{override}]")
    else:
        console.print(f"{prompt}")


def error(msg: str, override: str = None) -> None:
    if override is None:
        print(f"[white on red][@] {msg}[/white on red]")
    else:
        print(f"[{override}][@] {msg}[/{override}]")
    logging.error(f"{msg}\nLocals: {locals()}")


def warning(msg: str, override: str = None) -> None:
    if override is None:
        print(f"[white on yellow][!] {msg}[/white on yellow]")
    else:
        print(f"[{override}][!] {msg}[/{override}]")
    logging.warning(msg)


def info(msg: str, override: str = None) -> None:
    if override is not None:
        print(f"[{override}][?] {msg}[/{override}]")
    else:
        print(f"[?] {msg}")


def input(prompt: str, override: str = None, default=None, password=False) -> str:
    if default is None:
        if override is not None:
            return Prompt.ask(f"[{override}]{prompt}[/{override}]", password=password)
        else:
            return Prompt.ask(f"{prompt}", password=password)
    else:
        if override is not None:
            return Prompt.ask(f"[{override}]{prompt}[/{override}]", default=default, password=password)
        else:
            return Prompt.ask(f"{prompt}", default=default, password=password)


# ---------------------- Other Functions ---------------------------------------
def last_commit() -> str:
    raw = getoutput('git log -1 --pretty=%B')
    return raw.strip("\n")


def header(*modules: str):
    modules = list(modules)
    for i in range(modules.count("")):
        modules.remove("")
    modules = "\n    ".join(modules)
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
        [khaki3][ Branch: [bold]"{getoutput('git rev-parse --abbrev-ref HEAD')}"[/bold] ][/khaki3]
        [medium_purple1][ Last Commit: [bold]"{last_commit()}"[/bold] ][/medium_purple1]
        {modules}
        """)
