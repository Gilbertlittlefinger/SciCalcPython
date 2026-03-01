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
    
    def trig_display(self, mode, switch):
        # Code to display trigonometric results in the correct mode
        if mode.lower() == "deg":
            print("\nDisplaying result in degree mode.", end="")
            return mode.lower()
        elif mode.lower() == "rad":
            print("\nDisplaying result in radian mode.", end="")
            return mode.lower()
        else:
            return switch.lower()  # Return the current display mode if no switch command is given
        
    def auto_trig_display(self, switch):
        # Code to automatically switch trigonometric display mode based on the current mode
        if switch == "deg":
            print("\nDisplaying result in radian mode.", end="")
            return "rad"
        elif switch == "rad":
            print("\nDisplaying result in degree mode.", end="")
            return "deg"
        else:
            return switch  # Return the current display mode if no auto switch is defined

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
        
    def auto_display_mode(self, switch):
        # Code to automatically switch display mode based on the result
        if switch == "hexadecimal":
            print("\nDisplaying result in binary display mode.", end="")
            return "binary"
        elif switch == "binary":
            print("\nDisplaying result in octal display mode.", end="")
            return "octal"
        elif switch == "octal":
            print("\nDisplaying result in decimal display mode.", end="")
            return "decimal"
        elif switch == "decimal":
            print("\nDisplaying result in hexadecimal display mode.", end="")
            return "hexadecimal"
        
        else:
            return switch  # Return the current display mode if no auto switch is defined
        

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
