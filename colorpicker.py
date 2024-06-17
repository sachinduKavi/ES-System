from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("sk")
root.geometry("400x400")
root.iconbitmap("img/p.ico")


def color():
    m_color = colorchooser.askcolor()
    Label(root, text="Sachiya", bg=m_color[1], font=(50)).pack()



b01 = Button(root, text='Color', command=color).pack()
    


root.mainloop()