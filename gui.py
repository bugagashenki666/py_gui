from tkinter import Tk, mainloop, Label, Button
from time import sleep


def click_me():
    print("I'm clicked")
    # sleep(10)


root = Tk()

button = Button(root, text="Click me", command=click_me, width=20, height=7)
button.place(x=0, y=30)
label = Label(button, text="Hello, World")
label.place(x=0, y=0)
mainloop()
