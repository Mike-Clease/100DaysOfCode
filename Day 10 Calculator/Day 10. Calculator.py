from clear import clear
from CalcArt import logo

# Calculator funcs
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operation_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

def calculator():
    print(logo)
    rerun = True

    num1 = float(input("What is the first number? "))
        
    while rerun:    

        operation = input("Pick an operation: ")

        num2 = float(input("What is the next number? "))

        func = operation_dict[operation]
        answer = func(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        cont = input(f"Enter 'y' to continue calculating with {answer} or 'n' to start again. ")

        if cont == 'y':
            num1 = answer
        elif cont == 'n':
            rerun = False
            calculator()
        
calculator()