import os
from tkinter import *
from PIL import ImageTk, Image
import ttkwidgets.autocomplete
from time import *
import mysql.connector
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import font as tkfont
import webbrowser
# Importing Rate price updater
from ratepriceUpdater import rateUpdater
from complainsdatabase import complaints_database
from ipConfig import caller_ip


# Connecting my sql database
ip = open("ip.txt", "r").read()
print(ip)
# try:
data_base = mysql.connector.connect(
    host=ip,
    user='root',
    password='root'
)
print("Through Network")
# except:
#     messagebox.showerror("Error", "Unknown Error")
#     asd = messagebox.askyesno("Ip Config", "Do you want to change host IP ?")
#     if asd:
#         caller_ip()
#         ip = open("ip.txt", "r").read()
#         print(ip)


# Initializing cursor
cursor = data_base.cursor()

root = Tk()
root.geometry("990x650")
root.title("Esystem")
root.resizable(width=False, height=False)
root.iconbitmap("img/es2022/es.ico")


# Update record from sql database
def sql_updater():
    print(mname.get(), id_num_e.get())
    # Updating Record
    # calculating cost
    # Fetching prices
    price_list = []
    cursor.execute("SELECT * FROM  item_rates")
    result = cursor.fetchall()
    for record in result:
        price_list.append(int(record[1]))

    print(price_list)
    cost = int(led40_e.get()) * price_list[0] + int(set40_e.get()) * price_list[1] + int(led100_e.get()) * price_list[
        2] + int(led200_e.get()) * price_list[3] + int(bulb250_e.get()) * price_list[4] + int(choke250_e.get()) * \
           price_list[5] + int(ignitor250_e.get()) * price_list[6] + int(holder125_e.get()) * price_list[7] + int(
        switch5a_e.get()) * price_list[8] + int(toff_e.get()) * price_list[9] + int(wire1_e.get()) * price_list[
               10] + int(wire7_e.get()) * price_list[11]
    print(cost)

    # Fetching last updated index number
    cursor.execute(f"SELECT index_num FROM {mname.get()}")
    result_index = cursor.fetchall()
    num_list = []
    for record in result_index:
        print(record[0])
        num_list.append(int(record[0]))

    last_id = max(num_list)
    print("record no", last_id)

    print("Data Inserted successfully")

    # Deleting previous record
    cursor.execute(F"DELETE FROM {mname_2.get()} WHERE index_num={id_num_e.get()}")
    data_base.commit()

    # Inserting data to the database
    cursor.execute(F"""INSERT INTO {mname.get()} (dte, ename, division, led40, set40, set100, led200, holder125, bulb250, choke250, ignitor250, switch5a, toff, wire1, wire7, oname1, oval1, oname2, oval2, rowcost) VALUES\
             ('{date_e.get()}',\
             '{ename.get()}',\
             '{division_val.get()}',\
             '{led40_e.get()}',\
             '{set40_e.get()}',\
             '{led100_e.get()}',\
             '{led200_e.get()}',\
             '{holder125_e.get()}',\
             '{bulb250_e.get()}',\
             '{choke250_e.get()}',\
             '{ignitor250_e.get()}',\
             '{switch5a_e.get()}',\
             '{toff_e.get()}',\
             '{wire1_e.get()}',\
             '{wire7_e.get()}',\
             '{oname1_e.get()}',\
             '{oval1_e.get()}',\
             '{oname2_e.get()}',\
             '{oval2_e.get()}',\
             '{cost}'\
             )""")
    data_base.commit()

    # Fetching last updated index number
    cursor.execute(f"SELECT index_num FROM {mname.get()}")
    result_index = cursor.fetchall()
    num_list = []
    for record in result_index:
        print(record[0])
        num_list.append(int(record[0]))
    print(len(num_list))
    try:
        last_id = max(num_list)
    except:
        last_id = 1

    # Updating candidates name
    if mname.get() == 'Candidates':
        cursor.execute(f"UPDATE Candidates SET cname='{cname.get()}' WHERE index_num='{last_id}'")
        print("CNAME Updated")
        print(cname.get())
    data_base.commit()

    messagebox.showinfo("Record Updated Successfully", f"Record Updated Successfully as ES{last_id}")
    refresh_page()


sech = True


def sql_delete_record():
    # Deleting Record from sql
    global sech
    confirm = messagebox.askokcancel("Delete Record", "Click Ok to Delete Record Permanently")
    if confirm:
        cursor.execute(F"DELETE FROM {mname_2.get()} WHERE index_num={id_num_e.get()}")
        data_base.commit()
        id_num_e.delete(0, END)
        mini_label_uf.forget()
        mini_label_df.forget()
        button_frame.forget()
        sech = True
        print("Record Deleted Successfully")


def search_record():
    global sech, button_frame, mini_label_uf, mini_label_df
    mini_label_uf = Frame(delete_f, borderwidth=5)
    mini_label_df = Frame(delete_f)
    button_frame = Frame(delete_f)

    print(id_num_e.get(), mname_2.get())
    try:
        # Selecting related record
        cursor.execute(f"SELECT * FROM {mname_2.get()} WHERE index_num={id_num_e.get()}")
        result = cursor.fetchall()
        print(result[0])
        record = result[0]

        # Skipping a Column value when its not candidate table
        if mname_2.get() == "Candidates":
            incri = 0
        else:
            incri = 1
        print(incri)

        if sech:
            sech = False
            # Packing Mini Frames
            mini_label_uf.pack(pady=10)
            mini_label_df.pack(pady=10)
            button_frame.pack(pady=10, padx=200, anchor=E)

            # Labels for display
            global date_e, ename, minister_name_e
            Label(mini_label_uf, text='Date ', font=('Arial', 12)).grid(row=0, column=0, padx=35, sticky=W)
            date_e = DateEntry(mini_label_uf, date_pattern="yyyy-mm-dd", sticky=W)
            date_e.grid(row=0, column=1)
            date_e.delete(0, END)
            date_e.insert(END, str(record[1]))

            # Electrician Variable
            global ename
            ename = StringVar()
            ename_tupple = [
                'Madushanka',
                'Lenard',
                'Samansiri',
                'Priyantha',
                'Indika',
                'Tharindu',
                'Ajith',
                'Rameesh'
            ]
            # Minister list
            minister_list = [
                'Candidates'
            ]
            # Defining Divisions List
            division_list = [
                'Null',
                'Kammalthuraya',
                'Kochchikade',
                'Pallansena South',
                'Poruthota',
                'Daluwakotuwa East',
                'Palangathure',
                'Eththukala',
                'Kattuwa',
                'Dalupotha',
                'Dalupotha East',
                'Kudapaduwa',
                'Kudapaduwa North',
                'Wellaweediya North',
                'Wellaweediya South',
                'Periyamulla',
                'Hunupitiya',
                'Agurukaramulla',
                'Udayarthoppuwa',
                'Munnakkaraya',
                'Pitipana North',
                'Duwa',
                'Kadol Uyana',
                'Bolawalana',
                'Kurana',
                'Siriwardene Place',
                'South Pitipana East',
                'South Pitipana West',
                'Thalahena Dungalpitiya',
                'Kepungoda'
            ]
            cursor.execute("SELECT mname FROM minister_division_rev")
            result = cursor.fetchall()
            for name in result:
                minister_list.append(name[0])

            print(minister_list)

            Label(mini_label_uf, text='Electrician Name ', font=('Arial', 12)).grid(row=0, column=2)
            ename_e = OptionMenu(mini_label_uf, ename, *ename_tupple)
            ename_e.grid(row=0, column=3)

            global mname
            mname = StringVar()

            # Option Menu for minister
            Label(mini_label_uf, text='Name of the Minister ', font=('Arial', 12)).grid(row=1, column=0, padx=35)
            minister_name_e = OptionMenu(mini_label_uf, mname, *minister_list)
            minister_name_e.grid(row=1, column=1, padx=40, sticky=W)

            global division_val
            division_val = StringVar()
            print(record[4 - incri])

            # Option Menu for Division
            Label(mini_label_uf, text='Division', font=('Arial', 12)).grid(row=1, column=2, sticky=W)
            division_e = OptionMenu(mini_label_uf, division_val, *division_list)
            division_e.grid(row=1, column=3, padx=40)
            division_val.set(record[4 - incri])

            ename.set(record[2])

            # Setting interface for candidates
            mname.set(mname_2.get())

            if mname_2.get() == "Candidates":
                global cname
                # Entry for candidate
                lb1 = Label(mini_label_uf, text='Candidate Name', font=('Arial', 12))
                lb1.grid(row=2, column=0, sticky=W, padx=35)
                cname = Entry(mini_label_uf, font=('Arial', 12))
                cname.delete(0, END)
                cname.insert(END, str(record[3]))
                cname.grid(row=2, column=1, columnspan=2, sticky=W, padx=40)

            # globalization
            global led40_e, set40_e, led100_e, led200_e, bulb250_e, choke250_e, ignitor250_e, holder125_e, switch5a_e, toff_e, wire1_e, wire7_e, oname1_e, oval1_e, oname2_e, oval2_e

            Label(mini_label_df, text='40W LED Screw Bulb', font=('Arial', 12)).grid(row=0, column=0, pady=5, sticky=W)
            led40_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            led40_e.grid(row=0, column=1, padx=20)
            led40_e.insert(END, record[5 - incri])
            Label(mini_label_df, text='40W LED Complete Set', font=('Arial', 12)).grid(row=1, column=0, pady=5, sticky=W)
            set40_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            set40_e.grid(row=1, column=1, padx=20)
            set40_e.insert(END, record[6 - incri])
            Label(mini_label_df, text='100W LED Complete Set', font=('Arial', 12)).grid(row=2, column=0, pady=5, sticky=W)
            led100_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            led100_e.grid(row=2, column=1, padx=20)
            led100_e.insert(END, record[7 - incri])
            Label(mini_label_df, text='200W LED Flash Light', font=('Arial', 12)).grid(row=3, column=0, pady=5, sticky=W)
            led200_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            led200_e.grid(row=3, column=1, padx=20)
            led200_e.insert(END, record[8 - incri])
            Label(mini_label_df, text='250W Bulb', font=('Arial', 12)).grid(row=5, column=0, pady=5, sticky=W)
            bulb250_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            bulb250_e.grid(row=5, column=1, padx=20)
            bulb250_e.insert(END, record[10 - incri])
            Label(mini_label_df, text='125W Screw Holder', font=('Arial', 12)).grid(row=4, column=0, pady=5, sticky=W)
            holder125_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            holder125_e.grid(row=4, column=1, padx=20)
            holder125_e.insert(END, record[9 - incri])
            oname1_e = Entry(mini_label_df, font=('Arial', 12), width=20)
            oname1_e.grid(row=6, column=0)
            oname1_e.insert(END, record[17 - incri])
            oval1_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            oval1_e.grid(row=6, column=1)
            oval1_e.insert(END, record[18 - incri])

            Label(mini_label_df, text='250W SV Choke', font=('Arial', 12)).grid(row=0, column=2, pady=5, sticky=W)
            choke250_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            choke250_e.grid(row=0, column=3, padx=20)
            choke250_e.insert(END, record[11 - incri])
            Label(mini_label_df, text='250W Ignitor', font=('Arial', 12)).grid(row=1, column=2, pady=5, sticky=W)
            ignitor250_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            ignitor250_e.grid(row=1, column=3, padx=20)
            ignitor250_e.insert(END, record[12 - incri])
            Label(mini_label_df, text='5A Switch', font=('Arial', 12)).grid(row=2, column=2, pady=5, sticky=W)
            switch5a_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            switch5a_e.grid(row=2, column=3, padx=20)
            switch5a_e.insert(END, record[13 - incri])
            Label(mini_label_df, text='T-OFF', font=('Arial', 12)).grid(row=3, column=2, pady=5, sticky=W)
            toff_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            toff_e.grid(row=3, column=3, padx=20)
            toff_e.insert(END, record[14 - incri])
            Label(mini_label_df, text='1/1.13 Wire', font=('Arial', 12)).grid(row=4, column=2, pady=5, sticky=W)
            wire1_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            wire1_e.grid(row=4, column=3, padx=20)
            wire1_e.insert(END, record[15 - incri])
            Label(mini_label_df, text='7/0.53 Wire', font=('Arial', 12)).grid(row=5, column=2, pady=5, sticky=W)
            wire7_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            wire7_e.grid(row=5, column=3, padx=20)
            wire7_e.insert(END, record[16 - incri])
            oname2_e = Entry(mini_label_df, font=('Arial', 12), width=20)
            oname2_e.grid(row=6, column=2)
            oname2_e.insert(END, record[19 - incri])
            oval2_e = Entry(mini_label_df, font=('Arial', 12), width=8)
            oval2_e.grid(row=6, column=3)
            oval2_e.insert(END, record[20 - incri])

            Button(button_frame, image=delete_rec_img, borderwidth=0, command=sql_delete_record).grid(row=0, column=0, padx=10)
            Button(button_frame, image=update_img, borderwidth=0, command=sql_updater).grid(row=0, column=1, padx=10)
        else:
            # Updating Records
            date_e.delete(0, END)
            date_e.insert(END, str(record[1]))
            ename.set(record[2])
            division_val.set(record[4])
            cname.delete(0, END)
            print(record[3])
            cname.insert(END, str(record[3]))
            mname.set(mname_2.get())

            led40_e.delete(0, END)
            led40_e.insert(END, record[5])
            set40_e.delete(0, END)
            set40_e.insert(END, record[6])
            led100_e.delete(0, END)
            led100_e.insert(END, record[7])
            led200_e.delete(0, END)
            led200_e.insert(END, record[8])
            bulb250_e.delete(0, END)
            bulb250_e.insert(END, record[10])
            holder125_e.delete(0, END)
            holder125_e.insert(END, record[9])
            oname1_e.delete(0, END)
            oname1_e.insert(END, record[17])
            oval1_e.delete(0, END)
            oval1_e.insert(END, record[18])
            choke250_e.delete(0, END)
            choke250_e.insert(END, record[11])
            ignitor250_e.delete(0, END)
            ignitor250_e.insert(END, record[12])
            switch5a_e.delete(0, END)
            switch5a_e.insert(END, record[13])
            toff_e.delete(0, END)
            toff_e.insert(END, record[14])
            wire1_e.delete(0, END)
            wire1_e.insert(END, record[15])
            wire7_e.delete(0, END)
            wire7_e.insert(END, record[16])
            oname2_e.delete(0, END)
            oname2_e.insert(END, record[19])
            oval2_e.delete(0, END)
            oval2_e.insert(END, record[20])
    except:
        messagebox.showerror("No Record Found", "Searched index is out of range Try again")

# Refresh delete Record Function
def refresh_page():
    global sech
    sech = True
    delete_record()

# Delete Frame
def delete_record():
    forget_frame()
    delete_f.pack(fill=BOTH, expand=True)

    cursor.execute("SELECT mname FROM minister_division_rev")
    result = cursor.fetchall()
    minister_list = ['Candidates']
    for record in result:
        minister_list.append(record[0])

    # Add title Label
    Label(delete_f, text='Delete Record', font=('Arial', 25)).pack(pady=10, padx=5, anchor=W)
    # Creating Mini Frame
    mini03_f = Frame(delete_f)
    mini03_f.pack(anchor=W, padx=10)

    # Declaring Option Menu
    global mname_2
    mname_2 = StringVar()
    mname_2.set("Candidates")
    OptionMenu(mini03_f, mname_2, *minister_list).grid(column=0, row=1)

    global id_num_e
    Label(mini03_f, text='Search By Index :', font=('Arial', 18)).grid(column=0, row=0, pady=10, sticky=W, columnspan=2)
    # Add ID Number
    Label(mini03_f, text='ES ', font=('Arial', 18)).grid(column=1, row=1, sticky=E)
    id_num_e = Entry(mini03_f, font=('Arial', 18), width=5)
    id_num_e.grid(column=2, row=1, sticky=W)

    # Search Button
    Button(mini03_f, image=search_img, borderwidth=0, command=search_record).grid(row=1, column=3, padx=30)

    # Frame for home and refresh Buttons
    btn_frame = Frame(mini03_f)
    btn_frame.grid(row=1, column=4, padx=300)
    # Home and Refresh Button
    Button(btn_frame, image=refresh_img, borderwidth=0, command=refresh_page).grid(row=0, column=0, padx=10)
    Button(btn_frame, image=homebtn_img, borderwidth=0, command=menu_records).grid(row=0, column=1, padx=10)


def dataSubmit():
    print(led40_e.get(), set40_e.get(), led100_e.get(), led200_e.get(), bulb250_e.get(), choke250_e.get(), ignitor250_e.get(), holder125_e.get(), switch5a_e.get(), toff_e.get(), wire1_e.get(), wire7_e.get(), oname1_e.get(), oval1_e.get(), oname2_e.get(), oval2_e.get())
    print(date_e.get())
    print(division_val.get(), minister_name_e.get(), ename.get())
    # calculating cost
    # Fetching prices
    price_list = []
    cursor.execute("SELECT * FROM  item_rates")
    result = cursor.fetchall()
    for record in result:
        price_list.append(int(record[1]))

    print(price_list)
    try:
        cost = int(led40_e.get())*price_list[0] + int(set40_e.get())*price_list[1] + int(led100_e.get())*price_list[2] + int(led200_e.get())*price_list[3] + int(bulb250_e.get())*price_list[4] + int(choke250_e.get())*price_list[5] + int(ignitor250_e.get())*price_list[6] + int(holder125_e.get())*price_list[7] + int(switch5a_e.get())*price_list[8] + int(toff_e.get())*price_list[9] + int(wire1_e.get())*price_list[10] + int(wire7_e.get())*price_list[11]
        print(cost)
    except:
        messagebox.showerror("Invalid Number Format", "ValueError: invalid literal for int() with base 10")

    try:
        # Inserting data to the database
        cursor.execute(F"""INSERT INTO {minister_name_e.get().replace(" ", "_")} (dte, ename, division, led40, set40, set100, led200, holder125, bulb250, choke250, ignitor250, switch5a, toff, wire1, wire7, oname1, oval1, oname2, oval2, rowcost) VALUES\
        ('{date_e.get()}',\
        '{ename.get()}',\
        '{division_val.get()}',\
        '{led40_e.get()}',\
        '{set40_e.get()}',\
        '{led100_e.get()}',\
        '{led200_e.get()}',\
        '{holder125_e.get()}',\
        '{bulb250_e.get()}',\
        '{choke250_e.get()}',\
        '{ignitor250_e.get()}',\
        '{switch5a_e.get()}',\
        '{toff_e.get()}',\
        '{wire1_e.get()}',\
        '{wire7_e.get()}',\
        '{oname1_e.get()}',\
        '{oval1_e.get()}',\
        '{oname2_e.get()}',\
        '{oval2_e.get()}',\
        '{cost}'\
        )""")
        data_base.commit()
        cursor.execute(f"SELECT index_num FROM {minister_name_e.get().replace(' ', '_')}")
        result_index = cursor.fetchall()
        num_list = []
        for record in result_index:
            print(record[0])
            num_list.append(int(record[0]))

        last_id = max(num_list)
        print("record no", last_id)
        print(cname.get())
        # Updating candidates name
        if minister_name_e.get() == 'Candidates':
            cursor.execute(f"UPDATE Candidates SET cname='{cname.get()}' WHERE index_num='{last_id}'")
            print("CNAME Updated")


        print("Data Inserted successfully")

        data_base.commit()

        # Resetting Entries
        # Delete current values
        oval2_e.delete(0, END)
        oname2_e.delete(0, END)
        oval1_e.delete(0, END)
        oname1_e.delete(0, END)
        wire7_e.delete(0, END)
        wire1_e.delete(0, END)
        toff_e.delete(0, END)
        switch5a_e.delete(0, END)
        holder125_e.delete(0, END)
        ignitor250_e.delete(0, END)
        choke250_e.delete(0, END)
        bulb250_e.delete(0, END)
        led200_e.delete(0, END)
        led100_e.delete(0, END)
        set40_e.delete(0, END)
        led40_e.delete(0, END)

        # Resetting to reset value
        oval2_e.insert(END, "0")
        oval1_e.insert(END, "0")
        wire7_e.insert(END, "0")
        wire1_e.insert(END, "0")
        toff_e.insert(END, "0")
        switch5a_e.insert(END, "0")
        holder125_e.insert(END, "0")
        ignitor250_e.insert(END, "0")
        choke250_e.insert(END, "0")
        bulb250_e.insert(END, "0")
        led200_e.insert(END, "0")
        led100_e.insert(END, "0")
        set40_e.insert(END, "0")
        led40_e.insert(END, "0")

        minister_name_e.delete(0, END)

        # Setting for default values
        ename.set("Null")
        division_val.set("Null")

        # Ask user for add another record or not
        user_option = messagebox.askyesno("Record Created Successfully", "Do you want to create another Record ?")
        print(user_option)
        if not (user_option):
            user_option01 = messagebox.askyesno("Record Created Successfully", "Do you want to Manipulate Data ?")
            if user_option01:
                menu_records()
            else:
                root.quit()
    except:
        messagebox.showerror("Invalid Entry", "mysql.connector.errors.ProgrammingError: 1146 (42S02): Table 'esystem20_2024.sds' doesn't exist")


def add_record():
    forget_frame()
    data_addition_f.pack(fill=BOTH, expand=True)

    Label(data_addition_f, image=addnewR_img, font=('Modern No. 20', 50), fg='#4a91e8').pack(pady=30)
    mini1 = Frame(data_addition_f, pady=10)
    mini1.pack(pady=5)
    # Electric Items
    # Mini Display
    mini2 = Frame(data_addition_f, padx=20)
    mini2.pack(pady=10)

    global date_e, ename, minister_name_e
    Label(mini1, text='Date ', font=('Arial', 12)).grid(row=0, column=0, padx=35, sticky=W)
    date_e = DateEntry(mini1, date_pattern="yyyy-mm-dd", sticky=W, font=('Arial', 12), width=13)
    date_e.grid(row=0, column=1)

    # Electrician Variable
    global ename
    ename = StringVar()
    ename.set('Null')
    ename_tupple = [
        'Madushanka',
        'Lenard',
        'Samansiri',
        'Priyantha',
        'Indika',
        'Tharindu',
        'Ajith',
        'Rameesh'
    ]
    # Minister list
    minister_list =[
        'Candidates'
    ]
    # Defining Divisions List
    division_list = [
        'Null',
        'Kammalthuraya',
        'Kochchikade',
        'Pallansena South',
        'Poruthota',
        'Daluwakotuwa East',
        'Palangathure',
        'Eththukala',
        'Kattuwa',
        'Dalupotha',
        'Dalupotha East',
        'Kudapaduwa',
        'Kudapaduwa North',
        'Wellaweediya North',
        'Wellaweediya South',
        'Periyamulla',
        'Hunupitiya',
        'Agurukaramulla',
        'Udayarthoppuwa',
        'Munnakkaraya',
        'Pitipana North',
        'Duwa',
        'Kadol Uyana',
        'Bolawalana',
        'Kurana',
        'Siriwardene Place',
        'South Pitipana East',
        'South Pitipana West',
        'Thalahena Dungalpitiya',
        'Kepungoda'
    ]
    cursor.execute("SELECT mname FROM minister_division_rev")
    result = cursor.fetchall()
    for name in result:
        minister_list.append(name[0].replace("_", " "))

    print(minister_list)

    Label(mini1, text='Electrician Name ', font=('Arial', 12)).grid(row=0, column=2)
    ename_e = OptionMenu(mini1, ename, *ename_tupple)
    ename_e.grid(row=0, column=3)

    # Option Menu for minister
    Label(mini1, text='Name of the Minister ', font=('Arial', 12)).grid(row=1, column=0, padx=35)
    minister_name_e = ttkwidgets.autocomplete.AutocompleteCombobox(mini1, completevalues=minister_list)
    minister_name_e.grid(row=1, column=1, padx=40, sticky=W)

    global division_val
    division_val = StringVar()
    division_val.set("Null")
    # Option Menu for Division
    Label(mini1, text='Division', font=('Arial', 12)).grid(row=1, column=2, sticky=W)
    division_e = OptionMenu(mini1, division_val, *division_list)
    division_e.grid(row=1, column=3, padx=40)

    global cname
    # Entry for candidate
    Label(mini1, text='Candidate Name', font=('Arial', 12)).grid(row=2, column=0, sticky=W, padx=35)
    cname = Entry(mini1, font=('Arial', 12))
    cname.grid(row=2, column=1, columnspan=2, sticky=W, padx=40)
    cname.insert(END, "Communal")

    # globalization
    global led40_e, set40_e, led100_e, led200_e, bulb250_e, choke250_e, ignitor250_e, holder125_e, switch5a_e, toff_e, wire1_e, wire7_e, oname1_e, oval1_e, oname2_e, oval2_e

    Label(mini2, text='40W LED Screw Bulb', font=('Arial', 12)).grid(row=0, column=0, pady=5, sticky=W)
    led40_e = Entry(mini2, font=('Arial', 12), width=8)
    led40_e.grid(row=0, column=1, padx=20)
    led40_e.insert(END, '0')
    Label(mini2, text='40W LED Complete Set', font=('Arial', 12)).grid(row=1, column=0, pady=5, sticky=W)
    set40_e = Entry(mini2, font=('Arial', 12), width=8)
    set40_e.grid(row=1, column=1, padx=20)
    set40_e.insert(END, '0')
    Label(mini2, text='100W LED Complete Set', font=('Arial', 12)).grid(row=2, column=0, pady=5, sticky=W)
    led100_e = Entry(mini2, font=('Arial', 12), width=8)
    led100_e.grid(row=2, column=1, padx=20)
    led100_e.insert(END, '0')
    Label(mini2, text='200W LED Flash Light', font=('Arial', 12)).grid(row=3, column=0, pady=5, sticky=W)
    led200_e = Entry(mini2, font=('Arial', 12), width=8)
    led200_e.grid(row=3, column=1, padx=20)
    led200_e.insert(END, '0')
    Label(mini2, text='125W Screw Holder', font=('Arial', 12)).grid(row=4, column=0, pady=5, sticky=W)
    holder125_e = Entry(mini2, font=('Arial', 12), width=8)
    holder125_e.grid(row=4, column=1, padx=20)
    holder125_e.insert(END, '0')
    Label(mini2, text='250W Bulb', font=('Arial', 12)).grid(row=5, column=0, pady=5, sticky=W)
    bulb250_e = Entry(mini2, font=('Arial', 12), width=8)
    bulb250_e.grid(row=5, column=1, padx=20)
    bulb250_e.insert(END, '0')
    oname1_e = Entry(mini2, font=('Arial', 12), width=20)
    oname1_e.grid(row=6, column=0)
    oval1_e = Entry(mini2, font=('Arial', 12), width=8)
    oval1_e.grid(row=6, column=1)
    oval1_e.insert(END, '0')

    Label(mini2, text='250W SV Choke', font=('Arial', 12)).grid(row=0, column=2, pady=5, sticky=W)
    choke250_e = Entry(mini2, font=('Arial', 12), width=8)
    choke250_e.grid(row=0, column=3, padx=20)
    choke250_e.insert(END, '0')
    Label(mini2, text='250W Ignitor', font=('Arial', 12)).grid(row=1, column=2, pady=5, sticky=W)
    ignitor250_e = Entry(mini2, font=('Arial', 12), width=8)
    ignitor250_e.grid(row=1, column=3, padx=20)
    ignitor250_e.insert(END, '0')
    Label(mini2, text='5A Switch', font=('Arial', 12)).grid(row=2, column=2, pady=5, sticky=W)
    switch5a_e = Entry(mini2, font=('Arial', 12), width=8)
    switch5a_e.grid(row=2, column=3, padx=20)
    switch5a_e.insert(END, '0')
    Label(mini2, text='T-OFF', font=('Arial', 12)).grid(row=3, column=2, pady=5, sticky=W)
    toff_e = Entry(mini2, font=('Arial', 12), width=8)
    toff_e.grid(row=3, column=3, padx=20)
    toff_e.insert(END, '0')
    Label(mini2, text='1/1.13 Wire', font=('Arial', 12)).grid(row=4, column=2, pady=5, sticky=W)
    wire1_e = Entry(mini2, font=('Arial', 12), width=8)
    wire1_e.grid(row=4, column=3, padx=20)
    wire1_e.insert(END, '0')
    Label(mini2, text='7/0.53 Wire', font=('Arial', 12)).grid(row=5, column=2, pady=5, sticky=W)
    wire7_e = Entry(mini2, font=('Arial', 12), width=8)
    wire7_e.grid(row=5, column=3, padx=20)
    wire7_e.insert(END, '0')
    oname2_e = Entry(mini2, font=('Arial', 12), width=20)
    oname2_e.grid(row=6, column=2)
    oval2_e = Entry(mini2, font=('Arial', 12), width=8)
    oval2_e.grid(row=6, column=3)
    oval2_e.insert(END, '0')

    # Mini Frame for buttons
    mini4 = Frame(data_addition_f)
    mini4.pack(pady=30)

    # Submit Button
    Button(mini4, image=homebtn_img, borderwidth=0, command=menu_records).grid(row=0, column=0, padx=20)
    Button(mini4, image=submit_img, borderwidth=0, command=dataSubmit).grid(row=0, column=1, padx=20)


# Open estimate file
def estimate_file():
    try:
        os.startfile(f"EstimateDrop-{database[-4:]}")
    except:
        messagebox.showerror("Missing File", f"Change File name as: EstimateDrop-{database[-4:]}")
        webbrowser.open_new(f"http://{ip}/{database}/EstimateDrop.html")


# Open Division File
def division_file():
    try:
        os.startfile(f"divisions-{database[-4:]}")
    except:
        messagebox.showerror("Missing File", f"Change File name as: divisions-{database[-4:]}")
        webbrowser.open_new(f"http://{ip}/{database}/divisions.php")


# Open summary file
def summary_file():
    try:
        os.startfile(f"Summary-{database[-4:]}")
    except:
        messagebox.showerror("Missing File", f"Change File name as: Summary-{database[-4:]}")
        webbrowser.open_new(f"http://{ip}/{database}/Summary.php")


def view_Record():
    try:
        os.startfile(f"Display-{database[-4:]}")
    except:
        messagebox.showerror("Missing File", f"Change File name as: Display-{database[-4:]}")
        webbrowser.open_new(f"http://{ip}/{database}/Display.php")


def menu_records():
    global sech, database
    sech = True
    forget_frame()
    print(database)
    menu_home_f.pack(fill=BOTH, expand=True)
    Label(menu_home_f, text=database, font=('Arial', 12)).pack(pady=5, padx=10, anchor=W)
    Label(menu_home_f, image=mainMenu_img).pack(pady=15)

    mini_frame = Frame(menu_home_f)
    mini_frame.pack(pady=10)

    mini1_frame = Frame(mini_frame)
    mini2_frame = Frame(mini_frame)
    mini1_frame.grid(row=0, column=0, padx=30)
    mini2_frame.grid(row=0, column=1, padx=30)

    # Creating Menu Buttons
    Button(mini1_frame, text='Add Record', font=('Franklin Gothic', 20), borderwidth=8, cursor='hand2', command=add_record).pack(pady=10)
    Button(mini2_frame, text='View Records', font=('Franklin Gothic', 20), borderwidth=8, cursor='hand2', command=view_Record).pack(pady=10)
    Button(mini1_frame, text='Delete / Update', font=('Franklin Gothic', 20), borderwidth=8, cursor='hand2', command=delete_record).pack(pady=10)
    Button(mini2_frame, text='Estimates', font=('Franklin Gothic', 20), borderwidth=8, cursor='hand2', command=estimate_file).pack(pady=10)
    Button(mini2_frame, text='Division', font=('Franklin Gothic', 20), borderwidth=8, cursor='hand2', command=division_file).pack(pady=10)
    Button(mini2_frame, text='Summary', font=('Franklin Gothic', 20), borderwidth=8, cursor='hand2', command=summary_file).pack(pady=10)


# Verifying user name and password
# Updating Cursor and database
comp = True
def verification_user():
    global database, comp

    print(database_e.get(), user_name_e.get(), pass_e.get())
    if user_name_e.get() == 'admin' and pass_e.get() == 'root':
        database = 'Esystem20_' + database_e.get()
        if comp:
            file_menu.add_command(label='Complaints', command=lambda: complaints_database(database, root))
            comp = False
        global data_base, cursor
        # Updating database variable
        ip = open("ip.txt", "r").read()
        print(ip)
        try:
            data_base = mysql.connector.connect(
                host=ip,
                user='root',
                password='root',
                database=database
            )
            cursor = data_base.cursor()
            menu_records()
        except:
            messagebox.showerror("Database Error", "Database not found")
            # Updating cursor
            root.quit()
    else:
        user_name_e.delete(0, END)
        pass_e.delete(0, END)
        invalid_label.config(text="** Invalid User name or Password")
    # except:
    # messagebox.showerror("Invalid Database", "Could not find searched Database Try again")


# Home Frame
def home():
    global database_e, user_name_e, pass_e, invalid_label
    forget_frame()
    home_frame.pack(fill=BOTH, expand=True)
    # Welcome Screen
    Label(home_frame, image=welcome_img).pack(pady=30)

    Label(home_frame, text="Select Database", font=('Arial', 15)).pack(pady=10)
    database_e = Entry(home_frame, font=('Arial', 12), width=8)
    database_e.pack()

    mini_home_frame = Frame(home_frame)
    mini_home_frame.pack(pady=40)

    Label(mini_home_frame, text="User Name", font=('Arial', 15)).grid(row=0, column=0, pady=10)
    user_name_e = Entry(mini_home_frame, font=('Arial', 15))
    user_name_e.grid(row=0, column=1,)

    Label(mini_home_frame, text="Password", font=('Arial', 15)).grid(row=1, column=0,pady=10)
    pass_e = Entry(mini_home_frame, font=('Arial', 15), show='\u25CF')
    pass_e.grid(row=1, column=1,)

    invalid_label = Label(home_frame, text='', font=('Arial', 12), fg='red')
    invalid_label.pack()

    Button(home_frame, image=login_img, borderwidth=0, command=verification_user).pack(pady=20)


# Restart the program
def restart():
    root.quit()

def forget_frame():
    home_frame.forget()
    data_addition_f.forget()
    menu_home_f.forget()
    delete_f.forget()

    for child in home_frame.winfo_children():
        child.destroy()

    for child in menu_home_f.winfo_children():
        child.destroy()

    for child in delete_f.winfo_children():
        child.destroy()

    for child in data_addition_f.winfo_children():
        child.destroy()


# images
welcome_img = ImageTk.PhotoImage(Image.open("img/es2022/welcome.png").resize((937, 112), Image.ANTIALIAS))
login_img = ImageTk.PhotoImage(Image.open("img/es2022/login.png").resize((100, 50), Image.ANTIALIAS))
addrecord_img = ImageTk.PhotoImage(Image.open("img/es2022/addrecord.png").resize((323, 54), Image.ANTIALIAS))
delete_img = ImageTk.PhotoImage(Image.open("img/es2022/deleteRecord.png").resize((323, 54), Image.ANTIALIAS))
submit_img = ImageTk.PhotoImage(Image.open("img/es2022/submit.png").resize((100, 50), Image.ANTIALIAS))
addnewR_img = ImageTk.PhotoImage(Image.open("img/es2022/addNewRecord.png").resize((800, 90), Image.ANTIALIAS))
viewRecord_img = ImageTk.PhotoImage(Image.open("img/es2022/view.png").resize((323, 54), Image.ANTIALIAS))
mainMenu_img = ImageTk.PhotoImage(Image.open("img/es2022/mainMenu.png").resize((937, 112), Image.ANTIALIAS))
estimates_img = ImageTk.PhotoImage(Image.open("img/es2022/estimates.png").resize((323, 54), Image.ANTIALIAS))
search_img = ImageTk.PhotoImage(Image.open("img/es2022/search.png").resize((130, 40), Image.ANTIALIAS))
delete_rec_img = ImageTk.PhotoImage(Image.open("img/es2022/del.png").resize((55, 50), Image.ANTIALIAS))
update_img = ImageTk.PhotoImage(Image.open("img/es2022/update.png").resize((170, 65), Image.ANTIALIAS))
homebtn_img = ImageTk.PhotoImage(Image.open("img/es2022/homebtn.png").resize((55, 50), Image.ANTIALIAS))
refresh_img = ImageTk.PhotoImage(Image.open("img/es2022/refreshbtn.png").resize((55, 50), Image.ANTIALIAS))



# Menu
main_menu = Menu(root)
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Change Database', command=home)
file_menu.add_command(label='Price Rate Updater', command=rateUpdater)
file_menu.add_command(label='Exit', command=root.quit)

main_menu.add_cascade(label='Application', menu=file_menu)

action_menu = Menu(main_menu, tearoff=0)
action_menu.add_command(label='Data Addition')
action_menu.add_command(label='Edit')
action_menu.add_command(label='Delete')

main_menu.add_cascade(label='Action', menu=action_menu)

root.config(menu=main_menu)


# Frames
# Data addition Frame
data_addition_f = Frame(root)
# Menu Frame
menu_home_f = Frame(root)
# Home frame
home_frame = Frame(root)

# Delete Record Frame
delete_f = Frame(root)

home()


root.mainloop()