class Display:
    def store_memory(self, value, memory_value, current_result):
        # Code to store the value in memory
        if value.lower() == "m+":
            memory_value = current_result
            print(f"Current memory value: {memory_value}")
        elif value.lower() == "mc":
            memory_value = 0
            print(f"Current memory value: {memory_value}")
        elif value.lower() == "mrc":
            print(f"Current memory value: {memory_value}")
        return memory_value

    def switch_display_mode(self, mode, switch):
    # Code to switch display mode
        if mode.lower() == "hexadecimal":
            print("Switched to hexadecimal display mode.")
            return mode.lower()
        elif mode.lower() == "binary":
            print("Switched to binary display mode.")
            return mode.lower()
        elif mode.lower() == "decimal":
            print("Switched to decimal display mode.")
            return mode.lower()
        elif mode.lower() == "octal":
            print("Switched to octal display mode.")
            return mode.lower()
        else:
            return switch.lower()  # Return the current display mode if no switch command is given