from tkinter import *
import time

class bubble:
    def __init__(self, master, cvas, x, y):
        self.babel = cvas.create_oval(x-25, y-25, x+25, y+25, fill='red')
        self.fall(cvas, y, x)

    def fall(self, obj, y, x):
        while True:
            obj.delete(self.babel)
            y += 10
            self.babel = obj.create_oval(x-25, y-25, x+25, y+25, fill='red')
            time.sleep(1)



def motion(event):
    global x,y
    x, y = event.x, event.y
    print(x, y)


def clicked(event):
    global root
    bubble(root, canvas, x, y)

root = Tk()

canvas = Canvas(root, height=500, width=500)
canvas.pack()

canvas.bind("<Motion>", motion)
canvas.bind("<Button-1>", clicked)

root.mainloop()
