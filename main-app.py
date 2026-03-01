from calculator import Calculator
from Display_functions import Display

def getTwoNumbers():
    a = float(input("\nfirst number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    a = float(input("\nnumber? "))
    return a

def displayResult(x: float, mode: str):
    if mode == "hexadecimal":
        print(hex(int(x))[2:], end="")  # [2:] to remove the '0x' prefix from the hexadecimal representation
    elif mode == "binary":
        print(bin(int(x))[2:], end="")  # [2:] to remove the '0b' prefix from the binary representation
    elif mode == "decimal":
        print(x, end="")
    elif mode == "octal":
        print(oct(int(x))[2:], end="")  # [2:] to remove the '0o' prefix from the octal representation
    else:
        print(x, "\n")


def performCalcLoop(calc, dis):
    result = 0
    memory = 0
    switch = "decimal"  # Default display mode
    print("\nWelcome to the Scientific Calculator!", end="")
    
    while True:
        print("\n")
        choice = input("Type help for a list of operations or enter an operation \noperation: ")
        
        switch = dis.switch_display_mode(choice, switch)    # Switch display mode if the user input is a display mode command
        memory = dis.store_memory(choice, memory, result)  # Store the user's choice in memory
        
        # Display operations and quit command
        if choice == 'q':
            while True:
                final_choice = input("\nAre you sure you want to quit? (y/n) ")
                if final_choice.lower() == 'y':
                    return  # user types q to quit calculator.
                elif final_choice.lower() == 'n':
                    dis.display_quitcancel()  # user cancels quit command, return to previous state.
                    break  # user chooses not to quit, continue with calculator.
                else:
                    print("\nCommand not recognized. Rerunning user_interface.exe, please try again.")
    
        elif choice == 'help':
            print("\nAvailable operations: add, sub, mult, div, sqr, root2, exp, inv, neg, sin, cos, tan, isin, icos, itan, deg, rad, fac")
            print("Memory operations: M+ (store current result in memory), MC (clear memory), MRC (recall memory)")
            print("Display mode operations: hexadecimal, binary, decimal, octal")
            print("Other operations: clear (clears the display), q (quit the calculator)")
            continue
        elif choice == 'clear':
            dis.display_clear(choice)
            continue

        # Implementing calculator operations
        elif choice == 'add':
            a, b = getTwoNumbers()
            result = calc.add(a, b)

        # Passes or invalid imput
        elif choice.lower() == "m+" or choice.lower() == "mc" or choice.lower() == "mrc" \
            or choice.lower() == "hexadecimal" or choice.lower() == "binary" or choice.lower() == "decimal" or choice.lower() == "octal": 
            continue
        else:
            print("\nThat is not a valid input. Please try again.", end="")
            continue

        print(f"\nCurrent decimal memory value: {memory}")
        print(f"Current display mode: {switch}\n")
        print("Result: ", end="")
        displayResult(result, switch)
        

# main start
def main():
    calc = Calculator()
    dis = Display()
    dis.display_clear("clear")
    performCalcLoop(calc, dis)
    print("\nDone Calculating.\n")
    dis.self_destruct()


if __name__ == '__main__':
    main()
