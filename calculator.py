from __future__ import division
from tkinter import *


def numAdd(num):
    e.insert(END,num)

def clear():
    e.delete(0,END)

def equals():
    elist =e.get()
    print(elist)
    slist = elist.split(' ')
    print(slist)
    pList = []
    nList = []
    indexV = len(slist)-1
#division
    while (True):
        for i in range(indexV + 1):
            if (slist[i] == '/'):
                print(slist[i])
                multiValue = float(slist[i - 1]) / float(slist[i + 1])

                slist.remove(slist[i + 1])
                slist.remove(slist[i])
                slist.remove(slist[i - 1])

                slist.insert(i - 1, str(multiValue))
                indexV = len(slist) - 1
                print(slist)
                break
        if (slist.count('/') == 0):
            break

#multiply
    while(True):
        for i in range(indexV+1):
            if(slist[i] == 'X'):
                print(slist[i])
                multiValue = float(slist[i-1])*float(slist[i+1])

                slist.remove(slist[i+1])
                slist.remove(slist[i])
                slist.remove(slist[i-1])

                slist.insert(i-1, str(multiValue))
                indexV = len(slist)-1
                print(slist)
                break


        if(slist.count('X') == 0):
            break

 #addition
    while (True):
        for i in range(indexV + 1):
            if (slist[i] == '+'):
                print(slist[i])
                multiValue = float(slist[i - 1]) + float(slist[i + 1])

                slist.remove(slist[i + 1])
                slist.remove(slist[i])
                slist.remove(slist[i - 1])

                slist.insert(i - 1, str(multiValue))
                indexV = len(slist) - 1
                print(slist)
                break
        if (slist.count('+') == 0):
            break
 #subtraction
    while (True):
        for i in range(indexV + 1):
            if (slist[i] == '+'):
                print(slist[i])
                multiValue = float(slist[i - 1]) + float(slist[i + 1])

                slist.remove(slist[i + 1])
                slist.remove(slist[i])
                slist.remove(slist[i - 1])

                slist.insert(i - 1, str(multiValue))
                indexV = len(slist) - 1
                print(slist)
                break
        if (slist.count('+') == 0):
            break

    print('loop end')

    val = slist[0]
    print(slist)

    e.delete(0,END)
    e.insert(0,val)







root = Tk()
root.title('Calculator(Sk)')

e = Entry(root, width=50)
e.grid(column=0, row=0, columnspan=4)

#buttons.........

button_1 = Button(root, text='1', padx=30, pady=30,bg='#d3fffb', command=lambda :numAdd(1))
button_2 = Button(root, text='2',padx=30, pady=30,bg='#d3fffb', command=lambda :numAdd(2))
button_3 = Button(root, text='3',padx=30, pady=30,bg='#d3fffb', command=lambda :numAdd(3))
button_4 = Button(root, text='4',padx=30, pady=30,bg='#d3fffb', command=lambda :numAdd(4))
button_5 = Button(root, text='5',padx=30, pady=30,bg='#d3fffb', command=lambda :numAdd(5))
button_6 = Button(root, text='6',padx=30, pady=30,bg='#d3fffb', command=lambda :numAdd(6))
button_7 = Button(root, text='7',padx=30, pady=30,bg='#d3fffb', command=lambda :numAdd(7))
button_8 = Button(root, text='8',padx=30, pady=30,bg='#d3fffb', command=lambda :numAdd(8))
button_9 = Button(root, text='9',padx=30, pady=30,bg='#d3fffb', command=lambda :numAdd(9))
button_0 = Button(root, text='0',padx=30, pady=30,bg='#d3fffb', command=lambda :numAdd(0))

button_add = Button(root,text='+',padx=30, pady=30,bg='#08a7d7',fg='white',command=lambda :numAdd(' + '))
button_sub = Button(root,text='-',padx=30, pady=30,bg='#08a7d7',fg='white',command=lambda :numAdd(' - '))
button_div = Button(root,text='/',padx=30, pady=30,bg='#08a7d7',fg='white',command=lambda :numAdd(' / '))
button_multi = Button(root,text='X',padx=30, pady=30,bg='#08a7d7',fg='white',command=lambda :numAdd(' X '))
button_equal = Button(root,text='=',padx=30, pady=30, bg='#e80000',fg='white',command=equals)
button_clear = Button(root,text='C',padx=30, pady=30, command=clear)

button_1.grid(column=0, row=3)
button_2.grid(column=1, row=3)
button_3.grid(column=2, row=3)

button_4.grid(column=0, row=2)
button_5.grid(column=1, row=2)
button_6.grid(column=2, row=2)

button_7.grid(column=0, row=1)
button_8.grid(column=1, row=1)
button_9.grid(column=2, row=1)

button_0.grid(column=1, row=4)

#addition, sub, multi, division

button_add.grid(column=3, row=1)
button_sub.grid(column=3, row=2)
button_multi.grid(column=3, row=3)
button_div.grid(column=3, row=4)
button_equal.grid(column=2, row=4)
button_clear.grid(column=0, row=4)


root.mainloop()