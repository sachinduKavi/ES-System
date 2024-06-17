from tkinter import *

root = Tk()
root.title('price List')
root.iconbitmap('img/p.ico')


def click(value):

    global label01


    label01 = Label(root, text=value).pack()



val = IntVar()

Radiobutton(root, text='pizza', variable=val, value=500, command=lambda :click(val.get())).pack()
Radiobutton(root, text='macoroni', variable=val, value=800, command=lambda :click(val.get())).pack()
Radiobutton(root, text='lasnaga', variable=val, value=900, command=lambda :click(val.get())).pack()
Radiobutton(root, text='noodles', variable=val, value=1000, command=lambda :click(val.get())).pack()

label01 = Label(root,text='Rs 0').pack()

root.mainloop()