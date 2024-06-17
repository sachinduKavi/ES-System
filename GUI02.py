from tkinter import *

root = Tk()

def myClick():
    Mylabel01 = Label(root, text='look i click a button')
    Mylabel01.pack()

button01 = Button(root, text='click me', padx=40, pady=20, command=myClick)

button01.pack()

root.mainloop()