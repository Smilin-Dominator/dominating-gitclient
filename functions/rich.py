import rich

console = rich.Console(color_system="256")

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