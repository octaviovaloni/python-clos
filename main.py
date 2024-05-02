import lib.io
import lib.cmd

lib.io.clear_console()

# Main loop
def main_loop():
    actual_input = input("-> ").strip()
    
    if actual_input == "exit":
        lib.io.clear_console()
        exit()
    
    parsed_func = lib.cmd.parse(actual_input)
    parsed_func(actual_input, actual_input.split(" "))

while True:
    main_loop()