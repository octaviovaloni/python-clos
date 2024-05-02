"""
    Module used to save info about existing commands
"""
import lib.cmd_dict
import lib.io
import lib.cmd

# cmd_obj(args, desc: str, func: function(raw_cmd: str, parsed_cmd))
class cmd_obj():
    arguments = {}
    description = ""
    function = None
    
    def __init__(self, args, desc, func):
        self.function = func
        self.description = desc
        self.arguments = args
        

cmds = {}

cmds.clear()

# cmd function              array of strings
def echo_func(raw_cmd: str, parsed_cmd) :
    # echo hola como andas
    lib.io.print_normal(raw_cmd[4:])

#   cmd name
cmds['echo'] = cmd_obj(
    {
        # arg number  arg description
        '1': "[string] string containing the desired output."
    },
    "prints text in the console", # description
    echo_func
)

def clear_func(raw_cmd: str, parsed_cmd):
    lib.io.clear_console()

cmds['clear'] = cmd_obj(
    {},
    "clears the console",
    clear_func
)

def help_func(raw_cmd: str, parsed_cmd):
    print(len(parsed_cmd))
    if len(parsed_cmd) != 1:
        cmd = parsed_cmd[1]
        cmd_info = lib.cmd.cmd_exists(cmd)
        if cmd_info != False:
            lib.io.print_info(f"Command: {cmd}")
            lib.io.print_info(f"    Description: {cmd_info.description}")
            lib.io.print_info(f"    Arguments:")
            a = {}
            for arg_number in cmd_info.arguments:
                lib.io.print_info(f"        [{arg_number}]: {cmd_info.arguments[arg_number]}")
        else:
            lib.io.print_error(f"Command named [{cmd}] does not exist...")
    else:
        lib.io.print_info(f"Commands:")
        for cmd in cmds:
            lib.io.print_info(f"    {cmd}: {cmds[cmd].description}")

cmds['help'] = cmd_obj(
    {
        '1': "[string | optional] name of a specific command"
    },
    "displays a list with every command and their information",
    help_func
)