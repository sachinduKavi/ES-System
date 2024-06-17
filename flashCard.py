from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("SK")
root.iconbitmap("img/p.ico")
root.geometry("571x280")

f_welcome = Frame(root, bg='red')
f_welcome.pack(fill=BOTH, expand=1)
x_image = ImageTk.PhotoImage(Image.open("img/x.jpg").resize((74, 74)))
o_image = ImageTk.PhotoImage(Image.open("img/o.jpg").resize((74, 74)))
win_list = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [1, 5, 9], [7, 5, 3]]

welcome_img = ImageTk.PhotoImage(Image.open("img/welcome2.jpg"))
Label(f_welcome, image=welcome_img).pack()

def reset_Val():
    global final_val
    final_val = 0

# operarion value
operation = None
first = True
final_val = 0
refresh = False
state = False
num_triger = False


def calculation(symbol):
    global b7
    global operation
    global final_val
    global first
    info_display.insert(END, symbol)
    if(type(symbol) == str):
        print('string')
        if(operation == '+'):
            final_val += float(display.get())
        elif(operation == '-'):
            final_val = final_val - float(display.get())
        elif(operation == 'x'):
            final_val = final_val * float(display.get())
        elif(operation == '/'):
            final_val = final_val / float(display.get())
        else:
            final_val = float(display.get())


        if(symbol == '+'):
            operation = '+'
            if first:
                final_val = float(display.get())
                first = False
        elif(symbol == '-'):
            operation = '-'
            if first:
                final_val = float(display.get())
                first = False
        elif(symbol == 'x'):
            operation = 'x'
            if first:
                final_val = float(display.get())
                first = False
        elif(symbol == '/'):
            operation = '/'
            if first:
                final_val = float(display.get())
                first = False





        mini_display.delete(0, END)
        mini_display.insert(END, symbol)
        display.delete(0, END)
        display.insert(END, final_val)
        global refresh
        refresh = True

    else:
        print('int')
        if refresh:
            display.delete(0, END)
            refresh = False

        display.insert(END, symbol)

    print(final_val)
    if symbol == '=':
        info_display.insert(END, final_val)
        first = True



def clear():
    global final_val
    global first
# Reset values ..
    display.delete(0, END)
    mini_display.delete(0, END)
    info_display.delete(0, END)
    final_val = 0
    first = True

def cal():
    root.geometry("418x450")
    forget_frames()
    f_cal.pack(fill=BOTH, expand=1)

# display
    global mini_display
    mini_display = Entry(f_cal, font=('Arial', 30), bd=3, width=3)
    mini_display.grid(row=0, column=3)

    global display
    display = Entry(f_cal, font=('Arial', 27), bd=3, width=16)
    display.grid(row=0, column=0, columnspan=3, padx=4)

    global info_display
    info_display = Entry(f_cal, font=('Arial', 7), bd=3, width=62)
    info_display.grid(row=1, column=0, columnspan=3, padx=4, pady=5)

# Buttons ........
    b7= Button(f_cal, text='7', font=('Arial', 27), width=4, bg="#23d2fa", command=lambda :calculation(7))
    b7.grid(row=2, column=0, pady=10)
    Button(f_cal, text='8', font=('Arial', 27), width=4, bg="#23d2fa", command=lambda :calculation(8)).grid(row=2, column=1, pady=10)
    Button(f_cal, text='9', font=('Arial', 27), width=4, bg="#23d2fa", command=lambda :calculation(9)).grid(row=2, column=2, pady=10)

    Button(f_cal, text='4', font=('Arial', 27), width=4, bg="#23d2fa",  command=lambda :calculation(4)).grid(row=3, column=0, pady=10)
    Button(f_cal, text='5', font=('Arial', 27), width=4, bg="#23d2fa", command=lambda :calculation(5)).grid(row=3, column=1, pady=10)
    Button(f_cal, text='6', font=('Arial', 27), width=4, bg="#23d2fa", command=lambda :calculation(6)).grid(row=3, column=2, pady=10)

    Button(f_cal, text='1', font=('Arial', 27), width=4, bg="#23d2fa", command=lambda :calculation(1)).grid(row=4, column=0, pady=10)
    Button(f_cal, text='2', font=('Arial', 27), width=4, bg="#23d2fa", command=lambda :calculation(2)).grid(row=4, column=1, pady=10)
    Button(f_cal, text='3', font=('Arial', 27), width=4, bg="#23d2fa", command=lambda :calculation(3)).grid(row=4, column=2, pady=10)
    Button(f_cal, text='0', font=('Arial', 27), width=4, bg="#23d2fa", command=lambda :calculation(0)).grid(row=5, column=1, pady=10)


# Calculations Buttons .......

    Button(f_cal, text='+', font=('Arial', 27), width=3, bg="#ED9414", height=3, command=lambda :calculation('+')).grid(row=2, column=3, pady=10, rowspan=2)
    Button(f_cal, text='-', font=('Arial', 27), width=3, bg="#ED9414", command=lambda :calculation('-')).grid(row=4, column=3, pady=10)
    Button(f_cal, text='x', font=('Arial', 27), width=4, bg="#ED9414", command=lambda :calculation('x')).grid(row=5, column=0, pady=10)
    Button(f_cal, text='/', font=('Arial', 27), width=4, bg="#ED9414", command=lambda :calculation('/')).grid(row=5, column=2, pady=10)
    b_equal = Button(f_cal, text='=', font=('Arial', 27), width=3, bg="#2581C7", command=lambda :calculation('='))
    b_equal.grid(row=5, column=3, pady=10)


    Button(f_cal, text='Clear', width=9, command=clear).grid(row=1, column=3, pady=4)

def clicked(num):
    global turn

    global x_image, o_image
    b_list = (bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9)
    global win_list

    if turn:
        player1_list.append(num)
        b_list[num - 1]['image'] = x_image
        b_list[num - 1]['width'] = '74'
        b_list[num - 1]['height'] = '74'
        l_player_2['bg'] = '#B50303'
        l_player_1['bg'] = '#1ADBEB'
        l_player_2['fg'] = 'white'
        l_player_1['fg'] = 'black'
        for mini_list in win_list:
            count = 0
            for i in mini_list:
                if i in player1_list:
                    count += 1
                if count == 3:
                    print("player 1 wins")
                    val = messagebox.askyesno("WIn WIn", "Player : "+player_01+" wins Do you want to play again ?")
                    print(val)
                    if val:
                        l_player_1['bg'] = '#B50303'
                        player_name()
                        turn = True
                    else:
                        root.quit()


        turn = False
    else:
        player2_list.append(num)
        b_list[num - 1]['image'] = o_image
        b_list[num - 1]['width'] = '74'
        b_list[num - 1]['height'] = '74'
        l_player_2['bg'] = '#1ADBEB'
        l_player_1['bg'] = '#B50303'
        l_player_2['fg'] = 'black'
        l_player_1['fg'] = 'white'
        for mini_list in win_list:
            count = 0
            for i in mini_list:
                if i in player2_list:
                    count += 1
                if count == 3:
                    print("player 2 wins")
                    val = messagebox.askyesno("WIn WIn", "Player : " + player_02 + " wins Do you want to play again ?")
                    print(val)
                    if val:
                        turn = True
                        l_player_1['bg'] = '#B50303'
                        player_name()

                    else:
                        root.quit()

        turn = True
    print(player1_list, player2_list)





def flash():
    forget_frames()
    f_flashCard.pack(fill=BOTH, expand=1)


# Tik tak tok
def tiktak(play1, play2):
    forget_frames()
    f_tikTak.pack(fill=BOTH, expand=1)
    global bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9
    global l_player_1, l_player_2
# Getting players names
    global player_01, player_02
    player_01 = play1.get()
    player_02 = play2.get()
    if player_01 == "":
        player_01 = "User 01"
    if player_02 == "":
        player_02 = "User 02"

    root.geometry("360x520")

    l_player_1 = Label(f_tikTak, text='Player 1 : ' + player_01, font=('Palatino Linotype', 20), padx=15, bg='#1ADBEB', relief=SUNKEN, bd=8, fg='white')
    l_player_1.grid(row=0, column=0, columnspan=3, pady=10)
    l_player_2 = Label(f_tikTak, text='Player 2 : ' + player_02, font=('Palatino Linotype', 20), padx=15, bg='#1ADBEB', relief=SUNKEN, bd=8)
    l_player_2.grid(row=4, column=0, columnspan=3, pady=10)
    l_player_1['bg'] = '#B50303'



    bt7 = Button(f_tikTak, bg='#0D0C03', width=10, height=5, command=lambda :clicked(7))
    bt7.grid(row=1, column=0, pady=20, padx=20)
    bt8 = Button(f_tikTak, bg='#0D0C03', width=10, height=5, command=lambda :clicked(8))
    bt8.grid(row=1, column=1, pady=20, padx=20)
    bt9 = Button(f_tikTak, bg='#0D0C03', width=10, height=5, command=lambda :clicked(9))
    bt9.grid(row=1, column=2, pady=20, padx=20)

    bt4 = Button(f_tikTak, bg='#0D0C03', width=10, height=5, command=lambda :clicked(4))
    bt4.grid(row=2, column=0, pady=20, padx=20)
    bt5 = Button(f_tikTak, bg='#0D0C03', width=10, height=5, command=lambda :clicked(5))
    bt5.grid(row=2, column=1, pady=20, padx=20)
    bt6 = Button(f_tikTak, bg='#0D0C03', width=10, height=5, command=lambda :clicked(6))
    bt6.grid(row=2, column=2, pady=20, padx=20)

    bt1 = Button(f_tikTak, bg='#0D0C03', width=10, height=5, command=lambda :clicked(1))
    bt1.grid(row=3, column=0, pady=20, padx=20)
    bt2 = Button(f_tikTak, bg='#0D0C03', width=10, height=5, command=lambda :clicked(2))
    bt2.grid(row=3, column=1, pady=20, padx=20)
    bt3 = Button(f_tikTak, bg='#0D0C03', width=10, height=5, command=lambda :clicked(3))
    bt3.grid(row=3, column=2, pady=20, padx=20)

# define players
def player_name():
    forget_frames()
    f_player_name.pack(fill=BOTH, expand=1)
    root.geometry("300x430")

    global player1_list, player2_list
    player1_list = []
    player2_list = []

    global turn
    turn = True

    Label(f_player_name, text="Welcome", font=("Constantia", 40), bg='green').pack(pady=35)

    Label(f_player_name, text="Player_1 :", font=("Constantia", 20), bg='green').pack(pady=10)
    player_1 = Entry(f_player_name, width=30)
    player_1.pack()
    Label(f_player_name, text="Player_2 :", font=("Constantia", 20), bg='green').pack(pady=10)
    player_2 = Entry(f_player_name, width=30)
    player_2.pack()

    Button(f_player_name, text='Play', command=lambda :tiktak(player_1, player_2), width=20).pack(pady=30)




def forget_frames():
    f_cal.forget()
    f_flashCard.forget()
    f_tikTak.forget()
    f_player_name.forget()
    f_welcome.forget()


main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu)
main_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Exit', command=root.quit)

app_menu = Menu(main_menu)
main_menu.add_cascade(label='Application', menu=app_menu)
app_menu.add_command(label='XOX', command=player_name)
app_menu.add_command(label='Calculator', command=cal)
app_menu.add_command(label='Flash Cards', command=flash)

# Defining Frames .......
f_cal = Frame(root, height=400, bg='#f0081f', width=400)
f_tikTak = Frame(root, bg='#1ADBEB', height=400, width=400)
f_flashCard = Frame(root, bg='yellow', height=400, width=400)
f_player_name = Frame(root, bg='green', height=400, width=400)

root.mainloop()
