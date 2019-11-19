from tkinter import *
import random


root = Tk()

side_choice = IntVar()
rolld_result = IntVar()
side_choice.set(20)
title_label = Entry(root, font = "Helvetica 24")
title_label.grid(row=0, column=1, sticky = "W", columnspan = 3)


clear = Button(root, text="clear", font = "Helvetica 24")
clear.grid(row=5, column=3, sticky = "W")

coma = Button(root, text=",", font = "Helvetica 24")
coma.grid(row=5, column=1, sticky = "W")

cero = Button(root, text="0", font = "Helvetica 24")
cero.grid(row=5, column=2, sticky = "W")

one = Button(root, text="1", font = "Helvetica 24")
one.grid(row=4, column=1, sticky = "W")

two = Button(root, text="2", font = "Helvetica 24")
two.grid(row=4, column=2, sticky = "W")

three = Button(root, text="3", font = "Helvetica 24")
three.grid(row=4, column=3, sticky = "W")

four = Button(root, text = "4", font = "Helvetica 24")
four.grid(row=3, column=1, sticky = "W")

five = Button(root, text = "5", font = "Helvetica 24")
five.grid(row=3, column=2, sticky = "W")

six = Button(root, text = "6", font = "Helvetica 24")
six.grid(row=3, column=3, sticky = "W")

seven = Button(root, text = "7", font = "Helvetica 24")
seven.grid(row=2, column=1, sticky = "W")

eight = Button(root, text = "8", font = "Helvetica 24")
eight.grid(row=2, column=2, sticky = "W")

nine = Button(root, text = "9", font = "Helvetica 24")
nine.grid(row=2, column=3, sticky = "W")

root.mainloop()