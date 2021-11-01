from rich import print
from os import getcwd
from subprocess import getoutput


def header(modules=None):
    print(f"""[cornsilk1]
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
        o888bood8P'   `Y8bod8P' o888o o888o o888o o888o o888o o888o `Y888""8o   "888" `Y8bod8P' d888b    [/cornsilk1]
        
    [blue][ Directory: [bold]"{getcwd()}"[/bold] ][/blue]
    [green][ Branch: [bold]"{getoutput('git rev-parse --abbrev-ref HEAD')}"[/bold] ][/green]
    [cyan][ Last Commit Message: [bold]"{getoutput('git log -1 --pretty=%B')[:-1]}"[/bold] ][/cyan]
    {modules}
    """)
