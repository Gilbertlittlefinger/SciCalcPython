from calculator import Calculator
from Display_functions import Display

def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def displayResult(x: float, mode: str):
    if mode == "hexadecimal":
        print(hex(int(x)))
    elif mode == "binary":
        print(bin(int(x))[2:])
    elif mode == "decimal":
        print(x)
    elif mode == "octal":
        print(oct(int(x)))
    else:
        print(x, "\n")


def performCalcLoop(calc, dis):
    result = 0
    memory = 0
    switch = "decimal"  # Default display mode
    while True:
        choice = input("Operation? ")
        switch = dis.switch_display_mode(choice, switch)
        memory = dis.store_memory(choice, memory, result)  # Store the user's choice in memory
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a, b = getTwoNumbers()
            result = calc.add(a, b)
        elif choice.lower() == "m+" or choice.lower() == "mc" or choice.lower() == "mrc" \
            or choice.lower() == "hexadecimal" or choice.lower() == "binary" or choice.lower() == "decimal" or choice.lower() == "octal": 
            continue
        else:
            print("That is not a valid input.")
        displayResult(result, switch)
        print(switch)

# main start
def main():
    calc = Calculator()
    dis = Display()
    performCalcLoop(calc, dis)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
