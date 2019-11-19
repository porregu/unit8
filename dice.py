from tkinter import *
import random

def roll_dice():
    max = side_choice.get()
    roll = random.randint(1,max)
    rolld_result.set(roll)

root = Tk()

side_choice = IntVar()
rolld_result = IntVar()
side_choice.set(20)
title_label = Label(root , text="dice roller", font = "Helvetica 24")
title_label.grid(row=1, column=1, sticky = "W")

four_side = Radiobutton(root, text="4 side", variable=side_choice, value=4)
four_side.grid(row=2, column=1, sticky = "W")

six_side = Radiobutton(root, text="6 side", variable=side_choice, value=6)
six_side.grid(row=3, column=1, sticky = "W")

eight_side = Radiobutton(root, text="8 side", variable=side_choice, value=8)
eight_side.grid(row=4, column=1, sticky = "W")

ten_side = Radiobutton(root, text = "10 side", variable=side_choice,value=10)
ten_side.grid(row=5, column=1, sticky = "W")

twenty_side = Radiobutton(root, text = "20 side", variable=side_choice,value=20)
twenty_side.grid(row=6, column=1, sticky = "W")

roll_button = Button(root, text="roll dice", command=roll_dice)
roll_button.grid(row=7, column=1, sticky = "W")

roll_result = Label(root, textvariable=rolld_result, font = "Helvetica 32")
roll_result.grid(row=8, column=1, sticky = "W")

root.mainloop()