logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


def calculate(f_number: float, s_number: float, operation: str):
    if operation == "+":
        return f_number + s_number
    elif operation == "-":
        return f_number - s_number
    elif operation == "*":
        return f_number * s_number
    elif operation == "/":
        return f"{(f_number / s_number):.2f}"


while True:
    f_number = float(input("What is the first number?: "))
    Continue = "y"
    while Continue == "y":
        operations = ["+", "-", "*", "/"]
        print(operations)
        operation = input("Pick an operation: ")
        s_number = float(input("What is the second number?: "))
        result = calculate(f_number, s_number, operation)
        print(f"{f_number} {operation} {s_number} = {result}")
        Continue = input(
            f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation: "
        )
        f_number = float(result) if Continue == "y" else f_number
