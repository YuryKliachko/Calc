from calc.calculator import Calc

calc = Calc()

def calculation():
    num_1 = input("Enter the first number:\n").strip()
    if "." in num_1:
        num_1 = float(num_1)
    else:
        num_1 = int(num_1)
    action = input("Enter action:\n").strip()
    if action in ["+", "-", "*", "/"]:
        num_2 = input("Enter the second number:\n").strip()
        print('Result of calculation:')
        if "." in num_2:
            num_2 = float(num_2)
        else:
            num_2 = int(num_2)
        if action == "+":
            print(calc.sum(num_1, num_2))
        elif action == "-":
            print(calc.substraction(num_1, num_2))
        elif action == "*":
            print(calc.multiplication(num_1, num_2))
        else:
            print(calc.devision(num_1, num_2))
    elif action == "sqrt":
        print('Result of calculation:')
        print(calc.square_root(num_1))
    elif action == 'raise':
        print('Result of calculation:')
        print(calc.square(num_1))
    print("Proceed? (y / n)")
    choice = input()
    if choice == "y":
        calculation()
    else:
        return

calculation()


