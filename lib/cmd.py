"""
    Module used to parse and execute commands
"""
import lib.cmd
import lib.cmd_dict
import lib.io

# error function (is returned if the cmd doesn't exist)
def _error_func(raw_cmd: str, parsed_cmd):
    lib.io.print_error(f"Command named {parsed_cmd[0]} does not exist...")

def cmd_exists(cmd_name: str):
    for cmd in lib.cmd_dict.cmds:
        if cmd == cmd_name:
            return lib.cmd_dict.cmds[cmd]
    return False

def parse(raw: str):
    raw = raw.strip()
    splitted = raw.split(" ")
    cmd = cmd_exists(splitted[0])

    if cmd != False:
        return cmd.function
    else:
        return _error_func