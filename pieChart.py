from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk, Image


def month_con(monthnum):
    return {
        '00': "ALL",
        '01': "January",
        '02': "February",
        '03': "March",
        '04': "April",
        '05': "May",
        '06': "June",
        '07': "July",
        '08': "August",
        '09': "September",
        '10': "October",
        '11': "November",
        '12': "December"
    }.get(monthnum, "Error")


def forget_frames():
    all_frame.forget()
    for child in all_frame.winfo_children():
        child.destroy()


# Creating main function of new window


def allPage(month1):
    global first, all_frame
    if first:
        forget_frames()
    first = True
    try:
        month = '{:0>2}'.format(int(month1.get()))
    except:
        messagebox.showerror("Unidentified Value", "Typo Error Try again", parent=pie_Win)
    month1.delete(0, END)
    print(month)
    all_frame = Frame(pie_Win)
    all_frame.pack()
    prog_label = Label(all_frame, text="Progress -  All", font=("Arial", 20))
    prog_label.pack(anchor=W)
    month_name = month_con(month)
    print(month_name)
    if month == '00':
        # Fetching number of all records
        cursor.execute("SELECT COUNT(*) from Complaints")
        all_result = cursor.fetchall()[0][0]

        # Fetching number of finished works
        cursor.execute("SELECT COUNT(*) FROM Complaints WHERE w_state=1")
        finished_results = cursor.fetchall()[0][0]
    else:
        prog_label.config(text=f"Progress -  {month_name}")
        # Fetching data Related to given month
        cursor.execute(f"SELECT COUNT(*) FROM Complaints WHERE dte LIKE '{year}-{month}-%'")
        all_result = cursor.fetchall()[0][0]

        # Fetching number of finished works
        cursor.execute(f"SELECT COUNT(*) FROM Complaints WHERE w_state=1 AND dte LIKE '{year}-{month}-%'")
        finished_results = cursor.fetchall()[0][0]

    # Reaming works
    remaining_result = all_result - finished_results

    # Count frame
    count_f = Frame(all_frame)
    count_f.pack()

    Label(count_f, text=f"All Complaints : {all_result}", font=("arial", 13), fg='white', bg='#050200', relief=GROOVE).pack(pady=2, side=LEFT, anchor=N, padx=3)
    Label(count_f, text=f"Completed : {finished_results}", font=("arial", 13), bg="green", fg='white', relief=GROOVE).pack(pady=2, side=LEFT, anchor=N, padx=3)
    Label(count_f, text=f"Remaining : {remaining_result}", font=("arial", 13), bg="red", fg='white', relief=GROOVE).pack(pady=2, side=LEFT, anchor=N, padx=3)

    if not(all_result) == 0:
        workto360 = 360*finished_results/all_result
        percentage = 100*finished_results/all_result

        canvas = Canvas(all_frame, height=400, width=400)
        canvas.pack()

        canvas.create_oval(10, 10, 390, 390, fill='#ff0a0e')
        if workto360 == 360:
            canvas.create_oval(10, 10, 390, 390, fill='#21de00')
            Label(all_frame, text=str("{:.2f}".format(percentage)) + "%", font=("Arial", 14), relief=RAISED, bg='white').place(x=250, y=230)
        else:
            canvas.create_arc(10, 10, 390, 390, fill='#21de00', start=0, extent=workto360)
            Label(all_frame, text=str("{:.2f}".format(percentage)) + "%", font=("Arial", 14), relief=RAISED, bg='white', fg='green').place(x=250, y=230)
            Label(all_frame, text=str("{:.2f}".format(100-percentage)) + "%", font=("Arial", 14), relief=RAISED, bg='white', fg='red').place(x=250, y=280)
    else:
        messagebox.showinfo("Empty List", "No match found in the database", parent=pie_Win)
    all_frame.mainloop()


def piemain(master, sys_name, turn):
    print(master)
    global pie_Win, year, first
    year = sys_name[-4:]
    first = turn
    # Creating slave window
    pie_Win = Toplevel(master)
    pie_Win.geometry("430x510")
    pie_Win.resizable(width=False, height=False)
    pie_Win.title(f"Progress - {year}")
    pie_Win.iconbitmap("img/es2022/complaint.ico")
    ip = open("ip.txt", "r").read()
    print(ip)
    global data_base
    try:
        data_base = mysql.connector.connect(
            host=ip,
            user='root',
            password='root',
            database=sys_name
        )
        print("Through Network")
        # Initializing cursor
        global cursor
        cursor = data_base.cursor()
        btn_frame = Frame(pie_Win)
        btn_frame.pack(anchor=W)
        month_e = Entry(btn_frame, font=('Arial', 12), width=4)
        month_e.pack(side=LEFT, padx=5)
        month_e.insert(END, 0)
        # Importing Image
        search_img = ImageTk.PhotoImage(Image.open("img/es2022/search.png").resize((80, 30), Image.ANTIALIAS))

        Button(btn_frame, image=search_img, font=('Arial', 12), borderwidth=0, command=lambda: allPage(month_e)).pack(side=LEFT, padx=5, pady=5)
        allPage(month_e)
    except():
        messagebox.showerror("Network Error", "Change IP address")


