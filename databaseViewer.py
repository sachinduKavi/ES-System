import webbrowser
import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser

root = Tk()
root.geometry("445x700")
root.title("ESystem Viewer")
root.iconbitmap("img/es2022/es.ico")
root.resizable(width=False, height=False)
root.attributes('-alpha', 0.9)


def menu_page():
    forget_frames()
    menu_frame.pack(fill=BOTH, expand=True)
    # Place Background image
    Label(menu_frame, image=background_img).place(x=0, y=-10)
    Label(menu_frame, text=system_name, font=('Arial', 13), fg='#2b34ba', bg='white', relief=FLAT).place(x=30, y=650)

    menu_mini_frame = Frame(menu_frame, bg='white')
    menu_mini_frame.place(x=125, y=200)

    # View Button
    Button(menu_mini_frame, text='View Records', font=('Arial', 20), activebackground='white', cursor='hand2', command=view_Record).pack(pady=10)
    Button(menu_mini_frame, text='Estimates', font=('Arial', 20), padx=10, activebackground='white', cursor='hand2', command=estimate_file).pack(pady=10)
    Button(menu_mini_frame, text='Divisions', font=('Arial', 20), activebackground='white', cursor='hand2', command=division_file).pack(pady=10)
    Button(menu_mini_frame, text='Summary', font=('Arial', 20), activebackground='white', cursor='hand2', command=summary_file).pack(pady=10)

# Open estimate file
def estimate_file():
    print(system_name)
    try:
        os.startfile(f"EstimateDrop-{system_name[-4:]}")
    except:
        messagebox.showerror("Missing File", f"Change File name as: EstimateDrop-{system_name[-4:]}")
        webbrowser.open_new(f"http://192.168.1.3/{system_name}/EstimateDrop.html")


# Open Division File
def division_file():
    try:
        os.startfile(f"divisions-{system_name[-4:]}")
    except:
        messagebox.showerror("Missing File", f"Change File name as: divisions-{system_name[-4:]}")
        webbrowser.open_new(f"http://192.168.1.3/{system_name}/divisions.php")


# Open summary file
def summary_file():
    try:
        os.startfile(f"Summary-{system_name[-4:]}")
    except:
        messagebox.showerror("Missing File", f"Change File name as: Summary-{system_name[-4:]}")
        webbrowser.open_new(f"http://192.168.1.3/{system_name}/Summary.php")


# Display
def view_Record():
    try:
        os.startfile(f"Display-{system_name[-4:]}")
    except:
        messagebox.showerror("Missing File", f"Change File name as: Display-{system_name[-4:]}")
        webbrowser.open_new(f"http://192.168.1.3/{system_name}/Display.php")


def verification(event):
    if user_name.get() == 'admin' and user_psw.get() == 'root':
        if len(sys_year.get()) == 4:
            try:
                global system_name
                int(sys_year.get())
                system_name = "Esystem20_" + sys_year.get()
                menu_page()
            except:
                error_label.config(text='**Invalid Year Format')
        else:
            error_label.config(text='**Invalid Year Format')
    else:
        error_label.config(text='**Incorrect User Name or Password')


def welcome():
    global first, user_name, user_psw, sys_year, error_label
    forget_frames()
    first = True
    welcome_frame.pack(fill=BOTH, expand=True)
    # Place Background image
    Label(welcome_frame, image=background_img).place(x=0, y=-10)

    # User Name and Password Frame
    unp_f = Frame(welcome_frame, bg='white')
    unp_f.place(x=50, y=200)

    Label(unp_f, text='User Name :', font=('times', 20), bg='white').pack(pady=10, anchor=W)
    user_name = Entry(unp_f, font=('Arial', 15))
    user_name.pack()

    Label(unp_f, text='Password :', font=('times', 20), bg='white').pack(pady=10, anchor=W)
    user_psw = Entry(unp_f, font=('Arial', 15), relief=RAISED, show='\u25CF')
    user_psw.pack()

    error_label = Label(unp_f, text='', bg='white', fg='red', font=('times', 12))
    error_label.pack(pady=10, anchor=W)

    # Login Button and year Frame
    login_frame = Frame(welcome_frame, bg='white')
    login_frame.place(x=80, y=450)

    Label(login_frame, text='Year :', font=('times', 15), bg='white').grid(row=0, column=0)
    sys_year = Entry(login_frame, font=('Arial', 15), relief=RAISED, width=8, bg='white')
    sys_year.grid(row=0, column=1, padx=10)

    # Bind enter button
    root.bind("<Return>", verification)

    Button(login_frame, image=login_btn_img, borderwidth=0, bg='white', activebackground='white', command=lambda: verification("")).grid(row=0, column=2, padx=40)


first = False


# Forget Frames
def forget_frames():
    if(first):
        welcome_frame.forget()
        for child in welcome_frame.winfo_children():
            child.destroy()

    for child in menu_frame.winfo_children():
        child.destroy()
    menu_frame.forget()


# Defining Menu
main_menu = Menu(root)

# file menu
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Change Database', command=welcome)
file_menu.add_command(label='Exit', command=root.quit)

main_menu.add_cascade(label='File', menu=file_menu)

root.config(menu=main_menu)

# Welcome Frame
welcome_frame = Frame(root)
# Menu Frame
menu_frame = Frame(root)

# Importing background Image
background_img = ImageTk.PhotoImage(Image.open("img/es2022/back (5).jpg"))
login_btn_img = ImageTk.PhotoImage(Image.open("img/es2022/login.png").resize((100, 50), Image.ANTIALIAS))

welcome()

root.mainloop()