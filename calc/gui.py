from tkinter import Tk, Entry, Button, END, INSERT
from calc.calculator import Calc

root_win = Tk()
root_win.title("TinyCalc")

calc = Calc()

action_dict = {}


def insert_in_entry(event):
    global entry_can_be_cleared
    if entry_can_be_cleared is True:
        clear_entry()
        entry_can_be_cleared = False
    entry_field.insert(INSERT, event.widget['text'])


def clear_entry():
    entry_field.delete(0, END)


def reset_action_dict():
    global action_dict
    action_dict = {}
    clear_entry()


def get_validated_entry():
    entry = entry_field.get()
    if '.' in entry:
        return float(entry)
    else:
        return int(entry)


def x_2(event):
    try:
        num_1 = get_validated_entry()
        clear_entry()
        entry_field.insert(0, calc.square(num_1=num_1))
    except ValueError:
        return


def sqrt(event):
    try:
        num_1 = get_validated_entry()
        clear_entry()
        entry_field.insert(0, calc.square_root(num_1=num_1))
    except ValueError:
        return


def calculate_result():
    if action_dict["action"] == "+":
        result = calc.sum(action_dict["num_1"], action_dict["num_2"])
    elif action_dict["action"] == "-":
        result = calc.substraction(action_dict["num_1"], action_dict["num_2"])
    elif action_dict["action"] == "*":
        result = calc.multiplication(action_dict["num_1"], action_dict["num_2"])
    else:
        result = calc.devision(action_dict["num_1"], action_dict["num_2"])
    return result


def action(event):
    try:
        global action_dict
        global entry_can_be_cleared
        if len(action_dict) == 0:
            action_dict["num_1"] = get_validated_entry()
        else:
            action_dict["num_2"] = get_validated_entry()
            result_of_calculation = calculate_result()
            clear_entry()
            if result_of_calculation is None:
                entry_field.insert(0, "Devision by zero")
                entry_can_be_cleared = True
                return
            else:
                entry_field.insert(0, result_of_calculation)
                action_dict['num_1'] = result_of_calculation
        entry_can_be_cleared = True
        if event.widget["text"] != "=":
            action_dict["action"] = event.widget["text"]
        else:
            action_dict = {}
    except ValueError:
        return


entry_can_be_cleared = False

entry_field = Entry(root_win)
entry_field.grid(row=0, column=0, columnspan=4)

button_raise = Button(root_win, text='x2')
button_raise.grid(row=1, column=0)
button_raise.bind('<Button-1>', x_2)

button_sqrt = Button(root_win, text='√')
button_sqrt.grid(row=1, column=1)
button_sqrt.bind('<Button-1>', sqrt)

button_clear = Button(root_win, text='C', command=lambda : reset_action_dict())
button_clear.grid(row=1, column=2)

#Creating num buttons dynamicly
row = 2
column = 0
for i in [7, 4, 1, 0]:
    while column != 3:
        button_x = Button(root_win, text=i)
        button_x.grid(row=row, column=column)
        button_x.bind('<Button-1>', insert_in_entry)
        if i == 0:
            break
        i += 1
        column += 1
    row += 1
    column = 0

dot_button = Button(root_win, text=".")
dot_button.grid(row=5, column=1)
dot_button.bind('<Button-1>', insert_in_entry)

result_button = Button(root_win, text="=")
result_button.grid(row=5, column=2)
result_button.bind('<Button-1>', action)

#Creating action buttons dynamicly
row = 2
for i in ['+', '-', '*', '/']:
    action_button = Button(root_win, text=i)
    action_button.grid(row=row, column=3)
    action_button.bind('<Button-1>', action)
    row += 1

root_win.mainloop()