import os
import subprocess


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def enterprompt():
    input(f"\n{bcolors.FAIL}(enter) to continue..{bcolors.ENDC}\n")


def commitmsg():
    com = subprocess.getoutput('git log -1 --pretty=%B')
    spl = com.split("\n")
    if len(spl) == 2 and spl[1] == "":
        return spl[0]  # prevents redundant new line
    else:
        for text in spl:
            if text == "":
                spl.remove(text)
        return "\n".join(spl)


def greeting(*modules: str):
    modules = list(modules)
    for i in range(modules.count("")):
        modules.remove("")
    modules = "\n    ".join(modules)
    print(f"""{bcolors.HEADER}
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
        o888bood8P'   `Y8bod8P' o888o o888o o888o o888o o888o o888o `Y888""8o   "888" `Y8bod8P' d888b    
    {bcolors.ENDC}
    {bcolors.OKBLUE}[ Directory: {bcolors.BOLD}"{os.getcwd()}" ]{bcolors.ENDC}
    {bcolors.OKGREEN}[ Branch: {bcolors.BOLD}"{subprocess.getoutput('git rev-parse --abbrev-ref HEAD')}" ]{bcolors.ENDC}
    {bcolors.OKCYAN}[ Last Commit Message: "{commitmsg()}" ]{bcolors.ENDC}
    {modules}
    """)


log_format = '%(asctime)s (%(filename)s): %(message)s'
