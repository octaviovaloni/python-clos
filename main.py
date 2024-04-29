import lib
import lib.io

lib.io.clear_console()

# Main loop
def main_loop():
    actual_input = input("-> ")
    
    if actual_input == "exit":
        exit()

while True:
    main_loop()