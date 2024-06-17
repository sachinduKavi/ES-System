from tkinter import *

root = Tk()

def clickko():
        mylabel = Label(root, text='hello ' + e.get())
        mylabel.pack()

e = Entry(root)
e.pack()

button01 = Button(root, text='click Me', command=clickko)
button01.pack()

root.mainloop()