from tkinter import *

root = Tk()

side_choice = IntVar()

title_label = Label(root , text="dice roller")
title_label.grid(row=1, column=1)

four_side = Radiobutton(root, text="4 side", variable=side_choice, value=4)
four_side.grid(row=2, column=1)

six_side = Radiobutton(root, text="6 side", variable=side_choice, value=6)
six_side.grid(row=3, column=1)

eight_side = Radiobutton(root, text="8 side", variable=side_choice, value=8)
eight_side.grid(row=4, column=1)

root.mainloop()