from tkinter import *
import random


root = Tk()

def add_number0():
    new_result = display_result.get()
    new_result += "0"
    display_result.set(new_result)

def add_number1():
    new_result = display_result.get()
    new_result += "1"
    display_result.set(new_result)

def add_number2():
    new_result = display_result.get()
    new_result += "2"
    display_result.set(new_result)

def add_number3():
    new_result = display_result.get()
    new_result += "3"
    display_result.set(new_result)

def add_number4():
    new_result = display_result.get()
    new_result += "4"
    display_result.set(new_result)

def add_number5():
    new_result = display_result.get()
    new_result += "5"
    display_result.set(new_result)

def add_number6():
    new_result = display_result.get()
    new_result += "6"
    display_result.set(new_result)

def add_number7():
    new_result = display_result.get()
    new_result += "7"
    display_result.set(new_result)

def add_number8():
    new_result = display_result.get()
    new_result += "8"
    display_result.set(new_result)

def add_number9():
    new_result = display_result.get()
    new_result += "9"
    display_result.set(new_result)

def clculation1():
    new_result = display_result.get()
    new_result += "/"
    display_result.set(new_result)

def clculation2():
    new_result = display_result.get()
    new_result += "+"
    display_result.set(new_result)

def clculation3():
    new_result = display_result.get()
    new_result += "-"
    display_result.set(new_result)

def clculation4():
    new_result = display_result.get()
    new_result += "*"
    display_result.set(new_result)

def clculation5():
    new_result = display_result.get()
    new_result = float(new_result)**0.5
    display_result.set(new_result)

def coma():
    new_result = display_result.get()
    new_result += "."
    display_result.set(new_result)

def clear():
    display_result.set("")

def equal():
    new_result = display_result.get()
    new_result = eval(new_result)
    display_result.set(new_result)



display_result = StringVar()
side_choice = IntVar()
rolld_result = IntVar()
side_choice.set(20)
title_label = Entry(root, font = "Helvetica 24", textvariable = display_result, justify = "right")
title_label.grid(row=0, column=1, sticky = "W", columnspan = 3)

square_root = Button(root, text="√", font = "Helvetica 24", command = clculation5)
square_root.grid(row=6, column=4, sticky = "W")

sum = Button(root, text="+", font = "Helvetica 24", command = clculation2)
sum.grid(row=2, column=4, sticky = "W")

minus = Button(root, text="−", font = "Helvetica 24", command = clculation3)
minus.grid(row=3, column=4, sticky = "W")

multiply = Button(root, text="*", font = "Helvetica 24", command = clculation4)
multiply.grid(row=4, column=4, sticky = "W")

division = Button(root, text="/", font = "Helvetica 24", command = clculation1)
division.grid(row=5, column=4, sticky = "W")

clear = Button(root, text="clear", font = "Helvetica 24", command = clear)
clear.grid(row=5, column=3, sticky = "W")

coma = Button(root, text=".", font = "Helvetica 24", command = coma)
coma.grid(row=5, column=1, sticky = "W")

cero = Button(root, text="0", font = "Helvetica 24", command = add_number0)
cero.grid(row=5, column=2, sticky = "W")

one = Button(root, text="1", font = "Helvetica 24", command = add_number1)
one.grid(row=4, column=1, sticky = "W")

two = Button(root, text="2", font = "Helvetica 24", command = add_number2)
two.grid(row=4, column=2, sticky = "W")

three = Button(root, text="3", font = "Helvetica 24", command = add_number3)
three.grid(row=4, column=3, sticky = "W")

four = Button(root, text = "4", font = "Helvetica 24", command = add_number4)
four.grid(row=3, column=1, sticky = "W")

five = Button(root, text = "5", font = "Helvetica 24", command = add_number5)
five.grid(row=3, column=2, sticky = "W")

six = Button(root, text = "6", font = "Helvetica 24", command = add_number6)
six.grid(row=3, column=3, sticky = "W")

seven = Button(root, text = "7", font = "Helvetica 24", command = add_number7)
seven.grid(row=2, column=1, sticky = "W")

eight = Button(root, text = "8", font = "Helvetica 24", command = add_number8)
eight.grid(row=2, column=2, sticky = "W")

nine = Button(root, text = "9", font = "Helvetica 24", command = add_number9)
nine.grid(row=2, column=3, sticky = "W")

equal_btm = Button(root, text="=", font = "Helvetica 24", command = equal)
equal_btm.grid(row=6, column=3, sticky = "W")

root.mainloop()