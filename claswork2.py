from tkinter import *
import random

def roll_dice():
    p = hello.get()
    name.set("hello "+p+" nice to meet you ")

root = Tk()

hello = StringVar()

name = StringVar()
title_label = Entry(root, textvariable = hello )
title_label.grid(row=1, column=1)


roll_button = Button(root, text="say hello", command=roll_dice)
roll_button.grid(row=7, column=1)

roll_result = Label(root, textvariable=name)
roll_result.grid(row=8, column=1)

root.mainloop()