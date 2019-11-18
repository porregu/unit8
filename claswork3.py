from tkinter import *
import random

def roll_dice():
    pop = (hello.get()-32)*5%9
    temp.set(pop)

root = Tk()

hello = IntVar()

temp = IntVar()
roll_result = Label(root, text = "degrees in F")
roll_result.grid(row=1, column=1)

title_label =  Entry(root, textvariable = hello )
title_label.grid(row=1, column=2)

celsius = Label(root, text = "degrees in C")
celsius.grid(row=2, column=1)

roll_button = Button(root, text="convert", command=roll_dice)
roll_button.grid(row=7, column=1)

convert = Label(root, textvariable=temp )
convert.grid(row=8, column=2)

root.mainloop()