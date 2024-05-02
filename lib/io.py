"""
    Module used to manage input and outputs from the OS
"""
import colorama
from colorama import Fore
from colorama import Back
import os

colorama.just_fix_windows_console()
colorama.init(True)

colors = {
    "ERROR": Fore.RED,
    "NORMAL": Fore.WHITE,
    "INFO": Fore.YELLOW,
}

def clear_console() -> bool:
    try:
        os.system("cls")
        print("Python CLOS v0.0.1")
        return True
    except:
        return False

def print_info(txt: str) -> bool:
    try:
        print(colors["INFO"] + "info -> " + colors["NORMAL"] + txt + Fore.WHITE)
        return True
    except:
        return False

def print_error(txt: str) -> bool:
    try:
        print(colors["ERROR"] + "error -> " + colors["NORMAL"] + txt + Fore.WHITE)
        return True
    except:
        return False
    
def print_normal(txt: str) -> bool:
    try:
        print(colors["NORMAL"] + txt + Fore.WHITE)
        return True
    except:
        return False

def print_warning(txt: str) -> bool:
    try:
        print(colors["INFO"] + "warning -> " + colors["NORMAL"] + txt + Fore.WHITE)
        return True
    except:
        return False