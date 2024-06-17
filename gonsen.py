from tkinter import *

root = Tk()
root.title("Gonsen")
root.geometry("400x50")


def clicked():
    for i in range(10):
        sub = Tk()
        sub.title("Gonsen")
        sub.geometry("600x800")

        sub.mainloop()







b_01 = Button(root, text="click", padx=40, font=(40), command=clicked)
b_01.pack()



root.mainloop()

