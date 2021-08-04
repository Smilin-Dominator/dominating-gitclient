import os
import sys
from colours import bcolors


def syner(er):
    return f"[*] Invalid Syntax: {er}"


def greeting():
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
    {bcolors.ENDC}""")


def interface():
    codenames = {
        "mysql": r"C:\Users\Devisha\Documents\GitHub\mysql-and-python-billing",
        "devios": r"C:\Users\Devisha\Documents\GitHub\DeviOS",
        "coding_projects": r"C:\Users\Devisha\Documents\GitHub\coding-projects",
        "devicoin": r"C:\Users\Devisha\Documents\GitHub\flask_project",
        "here": r"C:\Users\Devisha\Documents\GitHub\GitClient"
    }
    if len(sys.argv) < 2:
        print(syner("Not Enough Arguments."))
        return False
    else:
        if sys.argv[1] == "-h":
            print(f"Syntax: 'python3 gitclient <dir>'\n\nCode Names: {codenames}\n\nIf you do not want to use codenames"
                  f" you may enter the absolute path of the directory.")
            sys.exit(1)
        else:
            choice = sys.argv[1]
            try:
                path = os.path.join(codenames[choice])
                if os.path.exists(path):
                    return path
                else:
                    print(syner("Wrong Path"))
                    return False
            except:
                if os.path.exists(choice):
                    return os.path.join(choice)
                else:
                    print(syner("Wrong Path"))
                    return False


if __name__ == '__main__':
    proceed = interface()
    if proceed:
        import client
        greeting()
        print("[*] Successful!")
        client.main(proceed)
    else:
        sys.exit(2)
