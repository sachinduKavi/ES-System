from tkinter import *
import mysql.connector
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from tkinter import messagebox
import os
import webbrowser
from pieChart import piemain


sys_name = None


def complaints_database(system_name, root):
    global data_base, sys_name, ip
    sys_name = system_name
    ip = open("ip.txt", "r").read()
    print(ip)
    try:
        data_base = mysql.connector.connect(
            host=ip,
            user='root',
            password='root',
            database=system_name
        )
        print("Through Network")
    except:
        messagebox.showerror("Network Error", "Change IP address")

    global cursor
    # Initializing cursor
    cursor = data_base.cursor()
    # Creating new window
    global win2
    if __name__ == "__main__":
        win2 = Tk()
    else:
        win2 = Toplevel(root)
    win2.title(f"Complaints - {system_name}")
    win2.iconbitmap("img/es2022/complaint.ico")
    win2.resizable(width=False, height=False)
    # win2.resizable(width=False, height=False)

    main_menu()


def database_add():
    global status_val
    print(light_typo.get())
    mobile_num = mobile_e.get(1.0, END)
    answer = True
    try:
        cursor.execute(f"SELECT ref_number FROM Complaints WHERE mobile_num={mobile_num}")
        result = cursor.fetchall()
    except:
        result = []
        continu = messagebox.askyesno("Missing Field", "Phone Number is missing do you want to continue ?", parent=win2)
        if not(continu):
            answer = False
    print(result)

    if len(result) > 0:
        ids = ""
        for ref in result:
            ids += " CM" + str(ref[0])
        answer = messagebox.askyesnocancel("Match Found", f"Similar records found in database as {ids} \n  Click YES to Continue \n  Click NO to Reset\n  Click CANCEL to Edit", parent=win2)
        print("answer" + str(answer))

    if answer:
        cursor.execute(f"""INSERT INTO Complaints (dte, comp_name, mobile_num, rd_address, light_type, lp_number, description, w_state, zone)
                        VALUES (
                        '{date_e.get()}',
                        '{compName_e.get()}',
                        '{mobile_num}',
                        '{rd_e.get(1.0, END)}',
                        '{light_typo.get()}',
                        '{lightnum_e.get()}',
                        '{des_e.get(1.0, END)}',
                        '{status_val}',
                        '{zonevar.get()}'
                        )""")
        data_base.commit()
        print('Successfully Added complaints')
        ans = messagebox.askyesno("Record Added Successfully", "Record created successfully, do you want to create another record ?", parent=win2)
        if ans:
            resetBtn()
        else:
            main_menu()
    else:
        if not(answer) == None:
            resetBtn()


def resetBtn():
    global status_val
    mobile_e.delete(1.0, END)
    light_typo.set(None)
    des_e.delete(1.0, END)
    rd_e.delete(1.0, END)
    lightnum_e.delete(0, END)
    compName_e.delete(0, END)
    status_val = 0
    sts_btn.config(image=cross_img)
    division_selected.set("Not Specified")
    zonevar.set("Not Specified")


def tick_cross():
    global status_val
    if status_val:
        sts_btn.config(image=cross_img)
        status_val = 0
    else:
        sts_btn.config(image=tick_img)
        status_val = 1
    print(status_val)


def record_del(ref_num):
    ans = messagebox.askyesno("Delete Record", f"Click Yes to Delete record CM{ref_num}", parent=win2)
    if ans:
        cursor.execute(f"DELETE FROM Complaints WHERE ref_number={ref_num}")
        data_base.commit()
        messagebox.showinfo("Record Deleted", f"Record CM{ref_num} Deleted successfully", parent=win2)
        mini_forget()


first1 = True


def mini_forget():
    record_frame.forget()
    for child in record_frame.winfo_children():
        child.destroy()


def update_rec(ref):
    print(ref)
    # Updating Record
    cursor.execute(f"""INSERT INTO Complaints (dte, comp_name, mobile_num, rd_address, light_type, lp_number, description, w_state, zone)
                    VALUES (
                    '{date_e.get()}',
                    '{compName_e.get()}',
                    '{mobile_e.get(1.0, END)}',
                    '{rd_e.get(1.0, END)}',
                    '{light_typo.get()}',
                    '{lightnum_e.get()}',
                    '{des_e.get(1.0, END)}',
                    '{status_val}',
                    '{zonevar.get()}'
                    )""")

    # Deleting Previous Record
    cursor.execute(f"DELETE FROM Complaints WHERE ref_number='{ref}'")
    data_base.commit()

    # Fetching updated ref number
    cursor.execute("SELECT ref_number FROM Complaints")
    result = cursor.fetchall()
    max = -10
    for record in result:
        ref_n = int(record[0])
        if max < ref_n:
            max = ref_n
    messagebox.showinfo("Record Updated", f"Record update successfully as CM{max}", parent=win2)
    # print(max)
    # Clearing screen
    mini_forget()


def search_rec(ref_no_e, p_number_e):
    global record_frame, first1
    try:
        if first1:
            first1 = False
        else:
            mini_forget()
        record_frame = Frame(update_frame)
        record_frame.pack(anchor=W, pady=10, padx=5)
        cursor.execute(f"SELECT * FROM Complaints")
        result = cursor.fetchall()
        pass_list = []
        # print(result)
        for record in result:
            p_number1 = record[3][:10]
            ref_num = record[0]
            # print(p_number1)
            try:
                id_num = int(ref_no_e.get())
            except:
                id_num = ""
            if p_number_e.get() == p_number1 or id_num == ref_num:
                pass_list.append(record)
        print(pass_list)

        # Multiple records options
        if len(pass_list) > 1:
            stri = ""
            for rec in pass_list:
                stri += "CM" + str(rec[0]) + " "
            print(stri)
            messagebox.showerror("Multiple Records found", f"Multiple records found as {stri}", parent=win2)
        else:
            record_value = pass_list[0]
            id_num = record_value[0]
            # Making Global variable
            global date_e, mobile_e, rd_e, light_typo, lightnum_e, des_e, compName_e
            print(record_value[0])
            Label(record_frame, text='Date ', font=('Arial', 12)).grid(row=0, column=0, pady=10, sticky=W)
            date_e = DateEntry(record_frame, font=('Arial', 12), date_pattern="yyyy-mm-dd")
            date_e.grid(row=0, column=1, pady=10, sticky=W, padx=10)
            date_e.delete(0, END)
            date_e.insert(0, record_value[1])

            # Displays Record Number
            Label(record_frame, text='CM' + str(record_value[0]), font=('Arial', 18), fg='red', relief=GROOVE).grid(row=0, column=1, padx=20, sticky=E)

            Label(record_frame, text='Complainer Name', font=('Arial', 12)).grid(row=1, column=0, pady=10, sticky=W)
            compName_e = Entry(record_frame, font=('Arial', 12), width=25)
            compName_e.grid(row=1, column=1, pady=10, sticky=W, padx=10)
            compName_e.delete(0, END)
            compName_e.insert(0, record_value[2])

            Label(record_frame, text='Mobile Number', font=('Arial', 12)).grid(row=2, column=0, pady=10, sticky=NW)
            mobile_e = Text(record_frame, font=('Arial', 12), width=11, height=2)
            mobile_e.grid(row=2, column=1, pady=10, sticky=W, padx=10)
            mobile_e.insert(1.0, record_value[3])

            Label(record_frame, text='Rd. Address', font=('Arial', 12)).grid(row=3, column=0, pady=10, sticky=NW)
            rd_e = Text(record_frame, font=('Arial', 12), width=40, height=2)
            rd_e.grid(row=3, column=1, pady=10, sticky=W, padx=10)
            rd_e.insert(1.0, record_value[4])

            light_typo = StringVar()
            light_typo.set(record_value[5])
            Label(record_frame, text='Light Bulb Type', font=('Arial', 12)).grid(row=4, column=0, pady=10, sticky=NW)
            radio_frame = Frame(record_frame)

            radio_frame.grid(row=4, column=1, pady=10, sticky=W)
            Radiobutton(radio_frame, text='40W LED', value='40W LED', variable=light_typo).grid(row=0, column=0, sticky=W)
            Radiobutton(radio_frame, text='100W LED', value='100W LED', variable=light_typo).grid(row=0, column=1, sticky=W)
            Radiobutton(radio_frame, text='250W Bulb', value='250W Bulb', variable=light_typo).grid(row=0, column=2,
                                                                                                    sticky=W)
            Radiobutton(radio_frame, text='125W MV Bulb', value='125W MV Bulb', variable=light_typo).grid(row=1, column=0,
                                                                                                          sticky=W)
            Radiobutton(radio_frame, text='Other', value='Other', variable=light_typo).grid(row=1, column=1, sticky=W)

            Label(record_frame, text='Light Post Number', font=('Arial', 12)).grid(row=5, column=0, pady=10, sticky=W)
            lightnum_e = Entry(record_frame, font=('Arial', 12), width=15)
            lightnum_e.grid(row=5, column=1, pady=10, sticky=W, padx=10)
            lightnum_e.insert(0, record_value[6])

            Label(record_frame, text='Description', font=('Arial', 12)).grid(row=6, column=0, pady=10, sticky=NW)
            des_e = Text(record_frame, font=('Arial', 12), width=40, height=2)
            des_e.grid(row=6, column=1, pady=10, sticky=W, padx=10)
            des_e.insert(1.0, record_value[7])

            global tick_img, cross_img, sts_btn, status_val
            tick_img = ImageTk.PhotoImage(Image.open("img/es2022/tick.png").resize((20, 20), Image.ANTIALIAS))
            cross_img = ImageTk.PhotoImage(Image.open("img/es2022/cross.jpg").resize((20, 20), Image.ANTIALIAS))
            if record_value[8] == 1:
                img = tick_img
                status_val = 1
            else:
                img = cross_img
                status_val = 0
            Label(record_frame, text='Status', font=('Arial', 12)).grid(row=7, column=0, pady=10, sticky=NW)
            sts_btn = Button(record_frame, image=img, command=tick_cross)
            sts_btn.grid(row=7, column=1, sticky=W)

            # Creating zone
            global zonevar
            zonevar = StringVar()
            Label(record_frame, text="Zone").grid(row=8, column=0, sticky=W)

            # Creating division drop down
            # Sub divisions
            global Thalahena_subd, Negombo_subd, Kochchikade_subd
            Thalahena_subd = ['Kepungoda', 'Thalahena Dungalpitiya', 'South Pitipana West', 'South Pitipana East',
                              'Pitipana North', 'Duwa']
            Negombo_subd = ['Munnakkaraya', 'Kadol Uyana', 'Bolawalana', 'Kurana', 'Udayarthoppuwa',
                            'Wellaweediya North', 'Wellaweediya South', 'Periyamulla', 'Agurukaramulla', 'Hunupitiya',
                            'Kudapaduwa', 'Siriwardene Place']
            Kochchikade_subd = ['Kudapaduwa North', 'Dalupotha', 'Dalupotha East', 'Kattuwa', 'Eththukala',
                                'Daluwakotuwa East', 'Palangathure', 'Poruthota', 'Pallansena South', 'Kammalthuraya',
                                'Kochchikade']
            # Division List
            division_list = ['Not Specified']
            division_list += Thalahena_subd + Negombo_subd + Kochchikade_subd

            radio_frame2 = Frame(record_frame)
            radio_frame2.grid(row=9, column=0, sticky=W, columnspan=2)
            # Radio buttons for zonal area
            Radiobutton(radio_frame2, text="Kochchikade\nSub Division", value="Kochchikade", variable=zonevar, indicatoron=False, bg='light blue').grid(row=0, column=0, pady=0)
            Radiobutton(radio_frame2, text="Negombo Town\nSub Division", value="Negombo Town", variable=zonevar, indicatoron=False, bg='light blue').grid(row=0, column=1, pady=0)
            Radiobutton(radio_frame2, text="Thalahena\nSub Division", value="Thalahena", variable=zonevar, indicatoron=False, bg='light blue').grid(row=0, column=2, pady=0)
            Radiobutton(radio_frame2, text="Not\nSpecified", value="Not Specified", variable=zonevar, indicatoron=False, bg='light blue').grid(row=0, column=3, pady=0)
            zonevar.set(record_value[9])

            # Variable for division dropdown
            global division_selected
            division_selected = StringVar()
            division_selected.set("Not Specified")
            division_drop = OptionMenu(radio_frame2, division_selected, *division_list, command=zonal)
            division_drop.grid(row=0, column=4, padx=20)

            # Button Images
            update_img = ImageTk.PhotoImage(Image.open("img/es2022/update.png").resize((130, 60)))
            delete_img = ImageTk.PhotoImage(Image.open("img/es2022/del.png").resize((40, 40)))
            cancel_img = ImageTk.PhotoImage(Image.open("img/es2022/cancel.png").resize((130, 40)))
            btn_frame = Frame(record_frame)
            btn_frame.grid(row=10, column=0, sticky=W, columnspan=2, pady=10)

            Button(btn_frame, image=update_img, borderwidth=0, cursor='hand2', command=lambda: update_rec(id_num)).grid(row=0, column=0, padx=5)
            Button(btn_frame, image=delete_img, borderwidth=0, command=lambda: record_del(record_value[0]), cursor='hand2').grid(row=0, column=1, padx=5)
            Button(btn_frame, image=cancel_img, borderwidth=0, command=mini_forget, cursor='hand2').grid(row=0, column=2, padx=5)
    except:
        messagebox.showerror("No record found", "IndexError: list index out of range", parent=win2)
    ref_no_e.delete(0, END)
    p_number_e.delete(0, END)
    mainloop()


def update_delete():
    forget_frames()
    win2.geometry("550x700")
    global update_frame

    update_frame = Frame(win2)
    update_frame.pack(fill=BOTH, expand=True)

    # Title
    Label(update_frame, text='Search / Update / Delete', font=('Arial', 15)).pack(pady=5, anchor=W, padx=5)

    # Search Record bar
    search_frame = Frame(update_frame)
    search_frame.pack(anchor=W)
    # record number
    Label(search_frame, text='Ref No. CM', font=('Arial', 12)).grid(row=1, column=0, padx=5, sticky=W)
    Label(search_frame, text='Phone Number', font=('Arial', 12)).grid(row=0, column=0, padx=5)

    ref_no_e = Entry(search_frame, font=('Arial', 12), width=4)
    ref_no_e.grid(row=1, column=1, padx=5, sticky=W)

    p_number_e = Entry(search_frame, font=('Arial', 12), width=11)
    p_number_e.grid(row=0, column=1, padx=5)

    search_img = ImageTk.PhotoImage(Image.open("img/es2022/search.png").resize((100, 35), Image.ANTIALIAS))
    home_btn = ImageTk.PhotoImage(Image.open("img/es2022/homebtn.png").resize((50, 50), Image.ANTIALIAS))
    Button(search_frame, image=search_img, borderwidth=0, command=lambda: search_rec(ref_no_e, p_number_e), cursor='hand2').grid(row=0, column=2, padx=10, rowspan=2)
    Button(search_frame, image=home_btn, borderwidth=0, command=main_menu, cursor='hand2').grid(row=0, column=3, padx=10, rowspan=2)

    mainloop()


status_val = 0


# Change zonal function
def zonal(selected_division):
    print("Selected division: " + selected_division)
    if selected_division in Thalahena_subd:
        zonevar.set("Thalahena")
        print("Thalahena selected")
    elif selected_division in Negombo_subd:
        zonevar.set("Negombo Town")
    elif selected_division in Kochchikade_subd:
        zonevar.set("Kochchikade")
    else:
        zonevar.set("Not Specified")


# Add new complaints
def add_complaints():
    forget_frames()
    win2.geometry("530x680")
    global new_complaints_f
    new_complaints_f = Frame(win2)
    new_complaints_f.pack(fill=BOTH, expand=True)

    complaintsnew_img = ImageTk.PhotoImage(Image.open("img/es2022/newcomplaints.png").resize((400, 60), Image.ANTIALIAS))
    Label(new_complaints_f, image=complaintsnew_img).pack(pady=5, anchor=W, padx=5)

    mini_f = Frame(new_complaints_f)
    mini_f.pack(pady=10, anchor=W, padx=10)

    # Making Global variable
    global date_e, mobile_e, rd_e, light_typo, lightnum_e, des_e, compName_e

    Label(mini_f, text='Date ', font=('Arial', 12)).grid(row=0, column=0, pady=10, sticky=W)
    date_e = DateEntry(mini_f, font=('Arial', 12), date_pattern="yyyy-mm-dd")
    date_e.grid(row=0, column=1, pady=10, sticky=W, padx=10)

    Label(mini_f, text='Complainer Name', font=('Arial', 12)).grid(row=1, column=0, pady=10, sticky=W)
    compName_e = Entry(mini_f, font=('Arial', 12), width=25)
    compName_e.grid(row=1, column=1, pady=10, sticky=W, padx=10)

    Label(mini_f, text='Mobile Number', font=('Arial', 12)).grid(row=2, column=0, pady=10, sticky=NW)
    mobile_e = Text(mini_f, font=('Arial', 12), width=11, height=2)
    mobile_e.grid(row=2, column=1, pady=10, sticky=W, padx=10)

    Label(mini_f, text='Rd. Address', font=('Arial', 12)).grid(row=3, column=0, pady=10, sticky=NW)
    rd_e = Text(mini_f, font=('Arial', 12), width=40, height=2)
    rd_e.grid(row=3, column=1, pady=10, sticky=W, padx=10)

    light_typo = StringVar()
    light_typo.set(None)
    Label(mini_f, text='Light Bulb Type', font=('Arial', 12)).grid(row=4, column=0, pady=10, sticky=NW)
    radio_frame = Frame(mini_f)

    radio_frame.grid(row=4, column=1, pady=10, sticky=W)
    Radiobutton(radio_frame, text='40W LED', value='40W LED', variable=light_typo).grid(row=0, column=0, sticky=W)
    Radiobutton(radio_frame, text='100W LED', value='100W LED', variable=light_typo).grid(row=0, column=1, sticky=W)
    Radiobutton(radio_frame, text='250W Bulb', value='250W Bulb', variable=light_typo).grid(row=0, column=2, sticky=W)
    Radiobutton(radio_frame, text='125W MV Bulb', value='125W MV Bulb', variable=light_typo).grid(row=1, column=0, sticky=W)
    Radiobutton(radio_frame, text='Other', value='Other', variable=light_typo).grid(row=1, column=1, sticky=W)

    Label(mini_f, text='Light Post Number', font=('Arial', 12)).grid(row=5, column=0, pady=10, sticky=W)
    lightnum_e = Entry(mini_f, font=('Arial', 12), width=15)
    lightnum_e.grid(row=5, column=1, pady=10, sticky=W, padx=10)

    Label(mini_f, text='Description', font=('Arial', 12)).grid(row=6, column=0, pady=10, sticky=NW)
    des_e = Text(mini_f, font=('Arial', 12), width=40, height=2)
    des_e.grid(row=6, column=1, pady=10, sticky=W, padx=10)

    global tick_img, cross_img, sts_btn, status_val
    tick_img = ImageTk.PhotoImage(Image.open("img/es2022/tick.png").resize((20, 20), Image.ANTIALIAS))
    cross_img = ImageTk.PhotoImage(Image.open("img/es2022/cross.jpg").resize((20, 20), Image.ANTIALIAS))

    Label(mini_f, text='Status', font=('Arial', 12)).grid(row=7, column=0, pady=10, sticky=NW)
    sts_btn = Button(mini_f, image=cross_img, command=tick_cross)
    sts_btn.grid(row=7, column=1, sticky=W)

    # Creating zone
    global zonevar
    zonevar = StringVar()
    zonevar.set("Not Specified")

    Label(new_complaints_f, text="Zone").pack(anchor=W, padx=10)

    radio_frame2 = Frame(new_complaints_f)
    radio_frame2.pack(anchor=W, padx=5, pady=5)

    # Creating division drop down
    # Sub divisions
    global Thalahena_subd, Negombo_subd, Kochchikade_subd
    Thalahena_subd = ['Kepungoda', 'Thalahena Dungalpitiya', 'South Pitipana West', 'South Pitipana East', 'Pitipana North', 'Duwa']
    Negombo_subd = ['Munnakkaraya', 'Kadol Uyana', 'Bolawalana', 'Kurana', 'Udayarthoppuwa', 'Wellaweediya North', 'Wellaweediya South', 'Periyamulla', 'Agurukaramulla', 'Hunupitiya', 'Kudapaduwa', 'Siriwardene Place']
    Kochchikade_subd = ['Kudapaduwa North', 'Dalupotha', 'Dalupotha East', 'Kattuwa', 'Eththukala', 'Daluwakotuwa East', 'Palangathure', 'Poruthota', 'Pallansena South', 'Kammalthuraya', 'Kochchikade']
    # Division List
    division_list = ['Not Specified']
    division_list += Thalahena_subd + Negombo_subd + Kochchikade_subd

    Radiobutton(radio_frame2, text="Kochchikade\nSub Division", value="Kochchikade", variable=zonevar, indicatoron=False, bg='light blue').grid(row=0, column=0, pady=0)
    Radiobutton(radio_frame2, text="Negombo Town\nSub Division", value="Negombo Town", variable=zonevar, indicatoron=False, bg='light blue').grid(row=0, column=1, pady=0)
    Radiobutton(radio_frame2, text="Thalahena\nSub Division", value="Thalahena", variable=zonevar, indicatoron=False, bg='light blue').grid(row=0, column=2, pady=0)
    Radiobutton(radio_frame2, text="Not\nSpecified", value="Not Specified", variable=zonevar, indicatoron=False, bg='light blue').grid(row=0, column=3, pady=0)

    # Variable for division dropdown
    global division_selected
    division_selected = StringVar()
    division_selected.set("Not Specified")
    division_drop = OptionMenu(radio_frame2, division_selected, *division_list, command=zonal)
    division_drop.grid(row=0, column=4, padx=20)

    btn_frame = Frame(new_complaints_f)
    btn_frame.pack(anchor=W, padx=25, pady=10)

    submit_img = ImageTk.PhotoImage(Image.open("img/es2022/submit.png").resize((100,50), Image.ANTIALIAS))
    Button(btn_frame, image=submit_img, borderwidth=0, command=database_add, cursor='hand2').grid(row=0, column=0, padx=10)
    resetbtn_img = ImageTk.PhotoImage(Image.open("img/es2022/reset.png").resize((100,50), Image.ANTIALIAS))
    Button(btn_frame, image=resetbtn_img, borderwidth=0, command=resetBtn, cursor='hand2').grid(row=0, column=1, padx=10)
    home_btn = ImageTk.PhotoImage(Image.open("img/es2022/homebtn.png").resize((50, 50), Image.ANTIALIAS))
    Button(btn_frame, image=home_btn, borderwidth=0, command=main_menu, cursor='hand2').grid(row=0, column=2, padx=10)

    new_complaints_f.mainloop()


def show_rec():
    global sys_name
    try:
        os.startfile(f"ComplaintsView-{sys_name[-4:]}")
    except:
        messagebox.showerror("Missing File", f"Change File name as: ComplaintsView-{sys_name[-4:]}", parent=win2)
        webbrowser.open_new(f"http://{ip}/{sys_name}/ComplaintsView.php")


first = True


def main_menu():
    global main_menu_frame, first
    forget_frames()
    # Main menu frame

    main_menu_frame = Frame(win2)
    main_menu_frame.pack(fill=BOTH, expand=True)
    win2.geometry("400x600")

    # Background Image
    lightpost_back_img = ImageTk.PhotoImage(Image.open("img/es2022/lightpost (4).jpg").resize((500, 600), Image.ANTIALIAS))
    back = Label(main_menu_frame, image=lightpost_back_img)
    back.place(x=-20, y=0)

    # Buttons for options
    Button(main_menu_frame, text='Add Complaints', font=('Arial', 15), bg='black', fg='white', command=add_complaints, cursor='hand2').place(x=50, y=150)
    Button(main_menu_frame, text='Search / Update / Delete', font=('Arial', 15), bg='black', fg='white', cursor='hand2', command=update_delete).place(x=50, y=225)
    Button(main_menu_frame, text='Show Records', font=('Arial', 15), bg='black', fg='white', cursor='hand2', command=show_rec).place(x=50, y=300)
    Button(main_menu_frame, text='Progress', font=('Arial', 15), bg='black', fg='white', cursor='hand2', command=lambda:piemain(win2, sys_name, False)).place(x=50, y=375)

    main_menu_frame.mainloop()


def forget_frames():
    global first, first1
    first = True
    first1 = True
    try:
        main_menu_frame.forget()
        for child in main_menu_frame.winfo_children():
            child.destroy()
    except:
        pass

    try:
        new_complaints_f.forget()
        for child in new_complaints_f.winfo_children():
            child.destory()
    except:
        pass

    try:
        update_frame.forget()
        for child in update_frame.winfo_children():
            child.destory()
    except:
        pass



if __name__ == "__main__":
    print("Run as main file")
    complaints_database("Esystem20_2022", None)


