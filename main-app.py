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

def displayTrigResult(x: float, mode: str):
    if mode == "degree":
        print(f"{Calculator.deg(x,x)} degrees", end="")
        return Calculator.deg(x,x)
    elif mode == "radian":
        print(f"{x} radians", end="")
        return x
    else:
        print(x, "\n")


def performCalcLoop(calc, dis):
    result = 0
    result_format = ""
    memory = 0
    switch = "decimal"  # Default display mode
    trig_switch = "degree"  # Default trigonometric display mode
    print("\nWelcome to the Scientific Calculator!", end="")
    
    while True:
        print("\n")
        choice = input("Type help for a list of operations or enter an operation \noperation: ")
        
        switch = dis.switch_display_mode(choice, switch)    # Switch display mode if the user input is a display mode command
        memory = dis.store_memory(choice, memory, result)  # Store the user's choice in memory
        trig_switch = dis.trig_display(choice, trig_switch)          # Switch trigonometric display mode if the user input is a trig display mode command

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
            print("\nAvailable operations: add, sub, mult, div, sqr, root2, exp, inv, neg, sin, cos, tan, isin, icos, itan, deg, rad, fac, log, log10, natlog, in_natlog, finite, abs_val")
            print("Memory operations: M+ (store current result in memory), MC (clear memory), MRC (recall memory)")
            print("Display mode operations: hexadecimal, binary, decimal, octal, switch (automatically switch display mode), trig (automatically switch trigonometric display mode), degree (switch to degree mode), radian (switch to radian mode)")
            print("Other operations: clear (clears the display), q (quit the calculator)")
            continue
        elif choice == 'clear':
            dis.display_clear(choice)
            continue

        elif choice.lower() == "switch":
            switch = dis.auto_display_mode(switch)
            continue
        elif choice.lower() == "trig":
            trig_switch = dis.auto_trig_display(trig_switch)
            continue

        # Implementing calculator operations
        elif choice == 'add':
            print("\nFormat: [number1] + [number2]")
            a, b = getTwoNumbers()
            result = calc.add(a, b)
            result_format = f"{a} + {b} = {result}"

        elif choice == 'sub':
            print("\nFormat: [number1] - [number2]")
            a, b = getTwoNumbers()
            result = calc.sub(a, b)
            result_format = f"{a} - {b} = {result}"

        elif choice == 'mult':
            print("\nFormat: [number1] * [number2]")
            a, b = getTwoNumbers()
            result = calc.mult(a, b)
            result_format = f"{a} * {b} = {result}"

        elif choice == 'div':
            print("\nFormat: [number1] / [number2]")
            a, b = getTwoNumbers()
            result = calc.div(a, b)
            result_format = f"{a} / {b} = {result}"

        elif choice == 'sqr':
            print("\nFormat: [number] ^ 2")
            a = getOneNumber()
            result = calc.sqr(a)
            result_format = f"{a} ^ 2 = {result}"

        elif choice == 'root2':
            print("\nFormat: sqrt([number])")
            a = getOneNumber()
            result = calc.root2(a)
            result_format = f"sqrt({a}) = {result}"

        elif choice == 'exp':
            print("\nFormat: [number1] ^ [number2]")
            a, b = getTwoNumbers()
            result = calc.exp(a, b)
            result_format = f"{a} ^ {b} = {result}"

        elif choice == 'inv':
            print("\nFormat: 1 / [number]")
            a = getOneNumber()
            result = calc.inv(a)
            result_format = f"1 / {a} = {result}"

        elif choice == 'neg':
            print("\nFormat: -[number]")
            a = getOneNumber()
            result = calc.neg(a)
            result_format = f"-{a} = {result}"

        elif choice == 'sin':
            print(f"\nCurrent trigonometric input mode: {trig_switch}")
            print("\nFormat: sin([number])")
            a = getOneNumber()
            a = calc.rad(a) if trig_switch == "degree" else a  # Convert input to radians if in degree mode
            result = calc.sin(a)
            result_format = f"sin({a}) = {result}"

        elif choice == 'cos':
            print(f"\nCurrent trigonometric input mode: {trig_switch}")
            print("\nFormat: cos([number])")
            a = getOneNumber()
            result = calc.cos(a)
            result_format = f"cos({a}) = {result}"

        elif choice == 'tan':
            print(f"\nCurrent trigonometric input mode: {trig_switch}")
            print("\nFormat: tan([number])")
            a = getOneNumber()
            result = calc.tan(a)
            result_format = f"tan({a}) = {result}"

        elif choice == 'isin':
            print(f"\nCurrent trigonometric input mode: {trig_switch}")
            print("\nFormat: arcsin([number])")
            a = getOneNumber()
            result = calc.isin(a)
            result_format = f"arcsin({a}) = {result}"

        elif choice == 'icos':
            print(f"\nCurrent trigonometric input mode: {trig_switch}")
            print("\nFormat: arccos([number])")
            a = getOneNumber()
            result = calc.icos(a)
            result_format = f"arccos({a}) = {result}"

        elif choice == 'itan':
            print(f"\nCurrent trigonometric input mode: {trig_switch}")
            print("\nFormat: arctan([number])")
            a = getOneNumber()
            result = calc.itan(a)
            result_format = f"arctan({a}) = {result}"

        elif choice == 'deg':
            print("\nFormat: deg([number])")
            a = getOneNumber()
            result = calc.deg(a)
            result_format = f"deg({a}) = {result}"

        elif choice == 'rad':
            print("\nFormat: rad([number])")
            a = getOneNumber()
            result = calc.rad(a)
            result_format = f"rad({a}) = {result}"

        elif choice == 'fac':
            print("\nFormat: [number]!")
            a = getOneNumber()
            result = calc.fac(a)
            result_format = f"{a}! = {result}"

        elif choice == 'log':
            print("\nFormat: log([number])")
            a = getOneNumber()
            result = calc.log(a)
            result_format = f"log({a}) = {result}"

        elif choice == 'log10':
            print("\nFormat: log10([number])")
            a = getOneNumber()
            result = calc.log10(a)
            result_format = f"log10({a}) = {result}"

        elif choice == 'natlog':
            print("\nFormat: ln([number])")
            a = getOneNumber()
            result = calc.natlog(a)
            result_format = f"ln({a}) = {result}"

        elif choice == 'in_natlog':
            print("\nFormat: in_ln([number])")
            a = getOneNumber()
            result = calc.in_natlog(a)
            result_format = f"in_ln({a}) = {result}"

        elif choice == 'finite':
            print("\nFormat: finite([number])")
            a = getOneNumber()
            result = calc.infinity(a)
            result_format = f"is finite({a}) = {result}"

        elif choice == 'abs_val':
            print("\nFormat: abs([number])")
            a = getOneNumber()
            result = calc.abs_val(a)
            result_format = f"abs({a}) = {result}"

        # Passes or invalid imput
        elif choice.lower() == "m+" or choice.lower() == "mc" or choice.lower() == "mrc" \
            or choice.lower() == "hexadecimal" or choice.lower() == "binary" or choice.lower() == "decimal" or choice.lower() == "octal" \
                or choice.lower() == "degree" or choice.lower() == "radian" or choice.lower() == "switch" or choice.lower() == "trig": 
            continue
        else:
            print("\nThat is not a valid input. Please try again.", end="")
            continue

        print(f"\nCurrent decimal memory value: {memory}")
        print(f"Current display mode: {switch}\n")
        if choice in ['sin', 'cos', 'tan', 'isin', 'icos', 'itan']:
            print(f"Current trigonometric display mode: {trig_switch}\n")
            print(f"{result_format}")
            displayTrigResult(result, trig_switch)
        else:
            print(f"{result_format}")
            print("Displaying result in current display mode: ", end="")
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
