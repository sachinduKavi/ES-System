from tkinter import *
from PIL import Imag, ImageTk

root = Tk()
root.iconbitmap('img/p.ico')
root.title('Image')
#IMAGE LIST
I_list = ['p (2).jpg', 'p (3).jpg', 'p (4).jpg', 'p (1).jpg']

#next image function...
val = 0
def next_I(increment):
    global val
    global my_img
    global m_label
    global status
    print(val, len(I_list))
    if(val == len(I_list)-2):
        button_forward = Button(root, text='>>', command=lambda: next_I(1), state='disable')
        button_forward.grid(row=1, column=2)


    status = Label(root, text=str(val+2)+' of ' + str(len(I_list)), bd=2, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


    button_back = Button(root, text='<<', command=lambda: back_I(1))
    button_back.grid(row=1, column=0)
    val += increment

    my_img = ImageTk.PhotoImage(Image.open('img/'+I_list[val]))
    m_label = Label(image=my_img)
    m_label.grid(row=0, column=0, columnspan=3)

#back image function.......
def back_I(decrement):
    global val
    global my_img
    global m_label
    global status
    print(val)

    if val == 1:
        button_back = Button(root, text='<<', state='disable')
        button_back.grid(row=1, column=0)

    status.grid_forget()
    status = Label(root, text=str(val) + ' of ' + str(len(I_list)), bd=2, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    button_forward = Button(root, text='>>', command=lambda: next_I(1))
    button_forward.grid(row=1, column=2)
    val -= decrement
    m_label.grid_forget()
    my_img = ImageTk.PhotoImage(Image.open('img/'+I_list[val]))
    m_label = Label(image=my_img)
    m_label.grid(row=0, column=0, columnspan=3)

my_img = ImageTk.PhotoImage(Image.open('img/p (2).jpg'))
m_label = Label(image=my_img)
m_label.grid(row=0, column=0, columnspan=3)


#status
status = Label(root, text='1 of '+str(len(I_list)), bd=2, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text='<<', command=lambda :back_I(1), state='disable')
button_back.grid(row=1, column=0)

button_exit = Button(root, text='Exit', command=root.quit)
button_exit.grid(row=1, column=1)

button_forward = Button(root, text='>>', command=lambda :next_I(1))
button_forward.grid(row=1, column=2)

root.mainloop()
