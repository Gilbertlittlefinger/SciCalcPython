import time

class Display:
    def store_memory(self, value, memory_value, current_result):
        # Code to store the value in memory
        if value.lower() == "m+":
            memory_value = current_result
            print(f"\nCurrent memory value: {memory_value}", end="")
        elif value.lower() == "mc":
            memory_value = 0
            print(f"\nCurrent memory value: {memory_value}", end="")
        elif value.lower() == "mrc":
            print(f"\nCurrent memory value: {memory_value}", end="")
        return memory_value

    def switch_display_mode(self, mode, switch):
    # Code to switch display mode
        if mode.lower() == "hexadecimal":
            print("\nSwitched to hexadecimal display mode.", end="")
            return mode.lower()
        elif mode.lower() == "binary":
            print("\nSwitched to binary display mode.", end="")
            return mode.lower()
        elif mode.lower() == "decimal":
            print("\nSwitched to decimal display mode.", end="")
            return mode.lower()
        elif mode.lower() == "octal":
            print("\nSwitched to octal display mode.", end="")
            return mode.lower()
        else:
            return switch.lower()  # Return the current display mode if no switch command is given
        
    def self_destruct(self):
        # Code to simulate self destruct sequence and exit the program
        time.sleep(0.5)
        print("Self destruct sequence initiated. \n Loading self_destruct.exe... \n initating count down sequence...")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("\033[2J\033[H", end="")
        print("\nBOOM! \n Error: self_destruct.exe has caused a fatal error \n Initiating backup restoration and kill command...")
        
        for i in range(3):
            time.sleep(2) 
            print("\nLoading...", end="") 
            
        print("\033[2J\033[H", end="")
        print("\n\nBackup restoration complete. \n Kill command successful. \n Exiting program...")
        print("Have a nice day")
        exit()

    def display_clear(self, value):
        # Code to clear the display
        if value.lower() == "clear":
            print("\033[2J\033[H", end="")  # ANSI escape codes to clear the terminal screen
    
    def display_quitcancel(self):
        # Code to display quit cancel message and return to previous state
        print("\nReturning to previous state. Please wait...")
        time.sleep(1)
