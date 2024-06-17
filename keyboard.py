from tkinter import *
from tkinter import Button

root = Tk()
root.title("Keybord binding")
root.geometry("400x400")
root.iconbitmap("img/p.ico")


def clicked(event):
    Label(root, text="hello "+event.keysym).pack()


b12 = Button(root, text='click me')
b12.bind("<m>", clicked)
b12.focus ()
b12.pack()

b13 = Button(root, text='click me')
b13.bind("<Key>", clicked)
b13.focus ()
b13.pack()



root.mainloop()
