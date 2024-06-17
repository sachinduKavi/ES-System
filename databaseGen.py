from tkinter import *
from PIL import ImageTk, Image
from tkcalendar import Calendar
import mysql.connector
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil


# connecting mysql data base
try:
    data_base = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root'
    )
    print("Through Network")
except:
    messagebox.showerror("Network Error", "Change IP address")


# Cursor initialize

cursor = data_base.cursor()


# Creating price table with item rating
def e_items(database_name):
    forget_frames()
    eitem_f.pack(fill=BOTH, expand=1)
    global led40_e, set40_e, led100_e, led200_e, bulb250_e, choke250_e, ignitor250_e, holder125_e, switch5a_e, toff_e, wire1_e, wire7_e
    Label(eitem_f, text="Connected to " + database_name, font=('Palatino Linotype', 12)).pack(padx=8, anchor=W)
    Label(eitem_f, text='Price Schedule and Ratings', font=('Palatino Linotype', 38)).pack(pady=20)

    # Mini Display
    mini2 = Frame(eitem_f, padx=20)
    mini2.pack()

    Label(mini2, text='40W LED Screw Bulb', font=('Arial', 12)).grid(row=0, column=0, pady=5, sticky=W)
    led40_e = Entry(mini2, font=('Arial', 12), width=8)
    led40_e.grid(row=0, column=1, padx=20)
    Label(mini2, text='40W LED Complete Set', font=('Arial', 12)).grid(row=1, column=0, pady=5, sticky=W)
    set40_e = Entry(mini2, font=('Arial', 12), width=8)
    set40_e.grid(row=1, column=1, padx=20)
    Label(mini2, text='100W LED Complete Set', font=('Arial', 12)).grid(row=2, column=0, pady=5, sticky=W)
    led100_e = Entry(mini2, font=('Arial', 12), width=8)
    led100_e.grid(row=2, column=1, padx=20)
    Label(mini2, text='200W LED Flash Light', font=('Arial', 12)).grid(row=3, column=0, pady=5, sticky=W)
    led200_e = Entry(mini2, font=('Arial', 12), width=8)
    led200_e.grid(row=3, column=1, padx=20)
    Label(mini2, text='250W Bulb', font=('Arial', 12)).grid(row=4, column=0, pady=5, sticky=W)
    bulb250_e = Entry(mini2, font=('Arial', 12), width=8)
    bulb250_e.grid(row=4, column=1, padx=20)
    Label(mini2, text='250W SV Choke', font=('Arial', 12)).grid(row=5, column=0, pady=5, sticky=W)
    choke250_e = Entry(mini2, font=('Arial', 12), width=8)
    choke250_e.grid(row=5, column=1, padx=20)
    Label(mini2, text='250W Ignitor', font=('Arial', 12)).grid(row=0, column=2, pady=5, sticky=W)
    ignitor250_e = Entry(mini2, font=('Arial', 12), width=8)
    ignitor250_e.grid(row=0, column=3, padx=20)
    Label(mini2, text='125W Screw Holder', font=('Arial', 12)).grid(row=1, column=2, pady=5, sticky=W)
    holder125_e = Entry(mini2, font=('Arial', 12), width=8)
    holder125_e.grid(row=1, column=3, padx=20)
    Label(mini2, text='5A Switch', font=('Arial', 12)).grid(row=2, column=2, pady=5, sticky=W)
    switch5a_e = Entry(mini2, font=('Arial', 12), width=8)
    switch5a_e.grid(row=2, column=3, padx=20)
    Label(mini2, text='T-OFF', font=('Arial', 12)).grid(row=3, column=2, pady=5, sticky=W)
    toff_e = Entry(mini2, font=('Arial', 12), width=8)
    toff_e.grid(row=3, column=3, padx=20)
    Label(mini2, text='1/1.13 Wire', font=('Arial', 12)).grid(row=4, column=2, pady=5, sticky=W)
    wire1_e = Entry(mini2, font=('Arial', 12), width=8)
    wire1_e.grid(row=4, column=3, padx=20)
    Label(mini2, text='7/0.53 Wire', font=('Arial', 12)).grid(row=5, column=2, pady=5, sticky=W)
    wire7_e = Entry(mini2, font=('Arial', 12), width=8)
    wire7_e.grid(row=5, column=3, padx=20)

    global invalid_label
    invalid_label = Label(mini2, text='', font=('Arial', 15), fg='red')
    invalid_label.grid(row=6, column=0, columnspan=4, pady=10)

    global lB01
    lB01 = Label(eitem_f, fg='red').pack(pady=20)

    Button(eitem_f, image=next_img, borderwidth=0, command=create_item_table).pack()


# Add item prices to sql database table
def create_item_table():
    # Adding data to item_rates

    cursor.execute(f"""INSERT INTO item_rates values('led40', '{float(led40_e.get())}')""")
    cursor.execute(f"""INSERT INTO item_rates values('set40', '{float(set40_e.get())}')""")
    cursor.execute(f"""INSERT INTO item_rates values('led100', '{float(led100_e.get())}')""")
    cursor.execute(f"""INSERT INTO item_rates values('led200', '{float(led200_e.get())}')""")
    cursor.execute(f"""INSERT INTO item_rates values('bulb250', '{float(bulb250_e.get())}')""")
    cursor.execute(f"""INSERT INTO item_rates values('choke250', '{float(choke250_e.get())}')""")
    cursor.execute(f"""INSERT INTO item_rates values('ignitor250', '{float(ignitor250_e.get())}')""")
    cursor.execute(f"""INSERT INTO item_rates values('holder125', '{float(holder125_e.get())}')""")
    cursor.execute(f"""INSERT INTO item_rates values('switch5a', '{float(switch5a_e.get())}')""")
    cursor.execute(f"""INSERT INTO item_rates values('toff', '{float(toff_e.get())}')""")
    cursor.execute(f"""INSERT INTO item_rates values('wire1', '{float(wire1_e.get())}')""")
    cursor.execute(f"""INSERT INTO item_rates values('wire7', '{float(wire7_e.get())}')""")
    data_base.commit()
    led40_e.delete(0, END)
    forget_frames()
    MDR()


# Adding data to tree view and sql database
count = 0
def add_treeview():
    global count
    if (minister_e.get() != "" and division_e.get() != "" and reservation_e.get() != ""):
        # Conversion
        m_name_final = ""
        first = True
        minister_list = minister_e.get().split(" ")
        for npart in minister_list:
            if len(npart) < 4:
                m_name_final += npart.upper()
                first = False
            else:
                if first:
                    m_name_final += npart[0].upper() + npart[1:]
                    first = False
                else:
                    m_name_final += " " + npart[0].upper() + npart[1:]

        division = division_e.get()
        final_division = division[0].upper() + division[1:]
        reservation = reservation_e.get()
        tree_view.insert(parent='', index=count, values=(m_name_final, final_division, reservation))
        count += 1
        print('dataAdded')
        cursor.execute(F"INSERT INTO minister_division_rev VALUES('{m_name_final.replace(' ', '_')}', '{final_division}', '{reservation}')")
        data_base.commit()

    minister_e.delete(0, END)
    division_e.delete(0, END)
    reservation_e.delete(0, END)


# Add text file function
def add_text():
    global count
    text_file_location = filedialog.askopenfilename(title="Add Text File", filetype=(('TXT', 'txt'),))
    text_file = open(text_file_location, 'r')
    # print(text_file.readlines())

    text_list = text_file.readlines()
    for record in text_list:
        record = record.strip()
        record_list = record.split("#")
        print(record_list)
        minister_name = record_list[0]
        division = record_list[1]
        reservation = record_list[2]
        m_name_final = ""
        minister_list = minister_name.split(" ")

        division_list = division.split(" ")
        final_division = ""
        div_first = True
        for div in division_list:
            if div_first:
                final_division += div[0].upper() + div[1:]
                div_first = False
            else:
                final_division += " " + div[0].upper() + div[1:]

        # capitalizing minister name
        first = True
        for npart in minister_list:
            if len(npart) < 4:
                m_name_final += npart.upper()
                first = False
            else:
                if first:
                    m_name_final += npart[0].upper() + npart[1:]
                    first = False
                else:
                    m_name_final += " " + npart[0].upper() + npart[1:]


        print(m_name_final)
        print(final_division)
        # Adding data to tree view and sql database
        tree_view.insert(parent='', index=count, values=(m_name_final, final_division, reservation))
        count += 1
        print('dataAdded')
        cursor.execute(F"INSERT INTO minister_division_rev VALUES('{m_name_final.replace(' ', '_')}', '{final_division}', '{reservation}')")
        data_base.commit()


# Creating MDR Function
def MDR():
    mdr_frame.pack(fill=BOTH, expand=1)
    Label(mdr_frame, text='Ministers And Division Reservation', font=('Palatino Linotype', 34)).pack(pady=20)

    # Enabling Tree View Function
    global tree_view
    tree_view = ttk.Treeview(mdr_frame)
    tree_view['columns'] = ('Minister', 'Division', 'Reservation')

    tree_view.column('#0', width=0, stretch=NO)
    tree_view.column('Minister', width=200, anchor=CENTER)
    tree_view.column('Division', width=200, anchor=CENTER)
    tree_view.column('Reservation', width=200, anchor=CENTER)

    tree_view.heading('#0', text='')
    tree_view.heading('Minister', text='Minister')
    tree_view.heading('Division', text='Division')
    tree_view.heading('Reservation', text='Reservation')

    # Frame for add button
    add_button_frame = Frame(mdr_frame)
    add_button_frame.pack()

    # Creating minister division reservation table
    try:
        cursor.execute("CREATE TABLE minister_division_rev("
                       "mname varchar(255),"
                       "division varchar(255),"
                       "reservation varchar(255))")
    except:
        cursor.execute("DROP TABLE minister_division_rev")
        cursor.execute("CREATE TABLE minister_division_rev("
                       "mname varchar(255),"
                       "division varchar(255),"
                       "reservation varchar(255))")
    print("MDR Table Created")
    Label(add_button_frame, text='Minister', font=('Arial', 12)).grid(row=0, column=0, padx=25)
    Label(add_button_frame, text='Division', font=('Arial', 12)).grid(row=0, column=1, padx=25)
    Label(add_button_frame, text='Reservation', font=('Arial', 12)).grid(row=0, column=2, padx=25)

    global minister_e, division_e, reservation_e

    minister_e = Entry(add_button_frame, font=('Arial', 12), width=25)
    minister_e.grid(row=1, column=0, pady=10, padx=5)
    division_e = Entry(add_button_frame, font=('Arial', 12), width=25)
    division_e.grid(row=1, column=1, pady=10, padx=5)
    reservation_e = Entry(add_button_frame, font=('Arial', 12), width=25)
    reservation_e.grid(row=1, column=2, pady=10, padx=5)

    tree_view.pack(pady=20)

    # Add Button
    Button(add_button_frame, image=add_img, borderwidth=0, command=add_treeview).grid(row=2, column=2, sticky=E, padx=5)
    Button(add_button_frame, image=add_text_file, borderwidth=0, command=add_text).grid(row=2, column=0, sticky=W, padx=5)
    Button(mdr_frame, image=finish_img, borderwidth=0, command=final_step).pack()


# Defining PHP File
def phpfile():
    # Input Files
    input_file1 = open('txt/displayUpper.txt', 'r')
    input_file2 = open('txt/displayBottom.txt', 'r')
    input_file3 = open('txt/displaylower3.txt', 'r')
    input_file_estimate1 = open('txt/Estimate_upper.txt', 'r')
    input_file_estimate2 = open('txt/Estimate_lower.txt', 'r')
    input_file_estimateDrop = open('txt/EstimateDrop.txt', 'r')
    input_file_divisions_1 = open('txt/divisions_upper.txt', 'r')
    input_file_divisions_2 = open('txt/divisions_lower.txt', 'r')
    input_file_sdivision_1 = open('txt/sdivision_upper.txt', 'r')
    input_file_sdivision_2 = open('txt/sdivision_lower.txt', 'r')
    input_file_summary_1 = open('txt/Summary_upper.txt', 'r')
    input_file_summary_2 = open('txt/Summary_lower.txt', 'r')
    input_file_datevalue_1 = open('txt/datevalue_upper.txt', 'r')
    input_file_datevalue_2 = open('txt/datevalue_low.txt', 'r')
    input_file_Complaints_view1 = open('txt/complaintsViewUpper.txt', 'r')
    input_file_Complaints_view2 = open('txt/complaintsViewDown.txt', 'r')
    input_file_complainsView_update1 = open('txt/updateComplaintsViewtop.txt', 'r')
    input_file_complainsView_update2 = open('txt/updateComplaintsViewdown.txt', 'r')
    input_file_toDoList_1 = open('txt/toDoListUpper.txt', 'r')
    input_file_toDoList_2 = open('txt/toDoListLower.txt', 'r')
    input_file_toDOListUpdate_1 = open('txt/toDoListUpdate_upper.txt', 'r')
    input_file_toDOListUpdate_2 = open('txt/toDoListUpdate_lower.txt', 'r')


    # Creating Display PHP
    try:
        os.makedirs(f'C:/MAMP/htdocs/{database_name}')
    except:
        pass
    output_file = open(f'C:/MAMP/htdocs/{database_name}/Display.php', 'w')
    estimate_out_file = open(f'C:/MAMP/htdocs/{database_name}/Estimate.php', 'w')
    estimate_drop_out_file = open(f'C:/MAMP/htdocs/{database_name}/EstimateDrop.html', 'w')
    divisions_out_file = open(f'C:/MAMP/htdocs/{database_name}/divisions.php', 'w')
    sdivision_out_file = open(f'C:/MAMP/htdocs/{database_name}/sdivision.php', 'w')
    summary_out_file = open(f'C:/MAMP/htdocs/{database_name}/Summary.php', 'w')
    datevalue_out_file = open(f'C:/MAMP/htdocs/{database_name}/dateValue.php', 'w')
    complaintsView_out_file = open(f'C:/MAMP/htdocs/{database_name}/complaintsView.php', 'w')
    complaintsViewupdate_out_file = open(f'C:/MAMP/htdocs/{database_name}/updateComplaints.php', 'w')
    toDoList_upt_file = open(f'C:/MAMP/htdocs/{database_name}/toDoList.php', 'w')
    toDoListUpdate_out_file = open(f'C:/MAMP/htdocs/{database_name}/toDoListUpdate.php', 'w')

    # Entering Upper code
    data = input_file1.read()
    output_file.write(data)
    summary_out_file.write(input_file_summary_1.read())
    # Write data in the for estimates
    estimate_out_file.write(input_file_estimate1.read())
    divisions_out_file.write(input_file_divisions_1.read())
    sdivision_out_file.write(input_file_sdivision_1.read())
    datevalue_out_file.write(input_file_datevalue_1.read())
    complaintsView_out_file.write(input_file_Complaints_view1.read())
    complaintsViewupdate_out_file.write(input_file_complainsView_update1.read())
    toDoList_upt_file.write(input_file_toDoList_1.read())
    toDoListUpdate_out_file.write(input_file_toDOListUpdate_1.read())

    divisions_out_file.close()
    output_file.close()
    estimate_out_file.close()
    sdivision_out_file.close()
    summary_out_file.close()
    datevalue_out_file.close()
    complaintsView_out_file.close()
    complaintsViewupdate_out_file.close()
    toDoList_upt_file.close()
    toDoListUpdate_out_file.close()

    divisions_out_file = open(f'C:/MAMP/htdocs/{database_name}/divisions.php', 'a')
    output_file = open(f'C:/MAMP/htdocs/{database_name}/Display.php', 'a')
    sdivision_out_file = open(f'C:/MAMP/htdocs/{database_name}/sdivision.php', 'a')
    # Appending data for estimate
    estimate_out_file = open(f'C:/MAMP/htdocs/{database_name}/Estimate.php', 'a')
    summary_out_file = open(f'C:/MAMP/htdocs/{database_name}/Summary.php', 'a')
    # date Value
    datevalue_out_file = open(f'C:/MAMP/htdocs/{database_name}/dateValue.php', 'a')
    # complaints
    complaintsView_out_file = open(f'C:/MAMP/htdocs/{database_name}/complaintsView.php', 'a')
    complaintsViewupdate_out_file = open(f'C:/MAMP/htdocs/{database_name}/updateComplaints.php', 'a')
    toDoList_upt_file = open(f'C:/MAMP/htdocs/{database_name}/toDoList.php', 'a')
    toDoListUpdate_out_file = open(f'C:/MAMP/htdocs/{database_name}/toDoListUpdate.php', 'a')

    # Fetching data from database
    cursor.execute("SELECT mname FROM minister_division_rev")

    # Divisions append system name
    divisions_out_file.write(f"$system_name = '{database_name}';\n")
    # Estimate append data system name
    estimate_out_file.write(f"$system_name = '{database_name}';\n")
    # Sdivision Append system name
    sdivision_out_file.write(f"$system_name = '{database_name}';\n")
    # Summary Append system name
    summary_out_file.write(f"$system_name = '{database_name}';\n")
    # dateValue append system name
    datevalue_out_file.write(f"$system_name = '{database_name}';\n")
    # Complaints
    complaintsView_out_file.write(f"$system_name = '{database_name}';\n")
    complaintsViewupdate_out_file.write(f"$system_name = '{database_name}';\n")
    toDoList_upt_file.write(f"$system_name = '{database_name}';\n")
    toDoListUpdate_out_file.write(f"$system_name = '{database_name}';\n")

    result = cursor.fetchall()
    for record in result:
        output_file.write("<option value='"+str(record[0])+"'>"+str(record[0].replace('_', ' '))+"</option>\n")

    # Appending lower part for Estimate
    estimate_out_file.write(input_file_estimate2.read())
    # Entering down part
    output_file.write(input_file2.read())
    output_file.write(f"$system_name = '{database_name}';\n")
    output_file.write(input_file3.read())
    # Writing Estimate Drop
    estimate_drop_out_file.write(input_file_estimateDrop.read())
    # Appending lower part for divisions
    divisions_out_file.write(input_file_divisions_2.read())
    # Appending lower part for sdivision
    sdivision_out_file.write(input_file_sdivision_2.read())
    # Appending lower part for Summary
    summary_out_file.write(input_file_summary_2.read())
    # Appending lower part for date Value
    datevalue_out_file.write(input_file_datevalue_2.read())
    # complaints
    complaintsView_out_file.write(input_file_Complaints_view2.read())
    complaintsViewupdate_out_file.write(input_file_complainsView_update2.read())
    toDoList_upt_file.write(input_file_toDoList_2.read())
    toDoListUpdate_out_file.write(input_file_toDOListUpdate_2.read())


    # Close files
    estimate_out_file.close()
    output_file.close()
    estimate_out_file.close()
    divisions_out_file.close()
    sdivision_out_file.close()
    summary_out_file.close()
    datevalue_out_file.close()
    complaintsView_out_file.close()
    complaintsViewupdate_out_file.close()
    toDoList_upt_file.close()
    toDoListUpdate_out_file.close()

    # Copying Image folder
    src = "Image/i.png"
    src2 = "Image/summary.png"
    cross = "Image/cross.jpg"
    tick = "Image/tick.png"
    printer = "Image/printer.jpg"
    try:
        os.makedirs(f"C:/MAMP/htdocs/{database_name}/Image")
    except:
        pass
    des = f"C:/MAMP/htdocs/{database_name}/Image"

    shutil.copy2(src, des)
    shutil.copy2(src2, des)
    shutil.copy2(cross, des)
    shutil.copy2(tick, des)
    shutil.copy2(printer, des)
    print("image file copied")


def complaints():

    cursor.execute("""CREATE TABLE Complaints(
                    ref_number int PRIMARY KEY AUTO_INCREMENT,
                    dte varchar(255),
                    comp_name nvarchar(255),
                    mobile_num varchar(255),
                    rd_address nvarchar(255),
                    light_type varchar(255),
                    lp_number varchar(255),
                    description nvarchar(1024),
                    w_state BOOLEAN,
                    zone varchar(50))""")


    print("Complaints Table created successfully")



# Final Step Finishing
def final_step():
    m_list = []
    sql = "SELECT * FROM minister_division_rev"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    for mname in result:
        m_list.append(mname[0])

    print(m_list)

    for mname in m_list:
        print(mname)
        try:
            cursor.execute(f"CREATE TABLE {mname} (index_num INT AUTO_INCREMENT PRIMARY KEY,\
                         dte varchar(255),\
                         ename varchar(255),\
                         division varchar(255),\
                         led40 INT,\
                         set40 INT,\
                         set100 INT,\
                         led200 INT,\
                         holder125 INT,\
                         bulb250 INT,\
                         choke250 INT,\
                         ignitor250 INT,\
                         switch5a INT,\
                         toff INT,\
                         wire1 INT,\
                         wire7 INT,\
                         oname1 varchar(255),\
                         oval1 INT,\
                         oname2 varchar(255),\
                         oval2 INT,\
                         rowcost FLOAT)")
        except:
            cursor.execute(f"DROP TABLE {mname}")
            cursor.execute(f"CREATE TABLE {mname} (index_num INT AUTO_INCREMENT PRIMARY KEY,\
                         dte varchar(255),\
                         ename varchar(255),\
                         division varchar(255),\
                         led40 INT,\
                         set40 INT,\
                         set100 INT,\
                         led200 INT,\
                         holder125 INT,\
                         bulb250 INT,\
                         choke250 INT,\
                         ignitor250 INT,\
                         switch5a INT,\
                         toff INT,\
                         wire1 INT,\
                         wire7 INT,\
                         oname1 varchar(255),\
                         oval1 INT,\
                         oname2 varchar(255),\
                         oval2 INT,\
                         rowcost FLOAT)")
    print('FinishTableCreating')

    # Creating candidates table
    try:
        cursor.execute("CREATE TABLE candidates(\
                index_num INT AUTO_INCREMENT PRIMARY KEY,\
                dte varchar(255),\
                ename varchar(255),\
                cname varchar(255),\
                division varchar(255),\
                led40 INT,\
                set40 INT,\
                set100 INT,\
                led200 INT,\
                holder125 INT,\
                bulb250 INT,\
                choke250 INT,\
                ignitor250 INT,\
                switch5a INT,\
                toff INT,\
                wire1 INT,\
                wire7 INT,\
                oname1 varchar(255),\
                oval1 INT,\
                oname2 varchar(255),\
                oval2 INT,\
                rowcost FLOAT)")
    except:
        cursor.execute("DROP TABLE candidates")
        cursor.execute("CREATE TABLE candidates(\
                index_num INT AUTO_INCREMENT PRIMARY KEY,\
                dte varchar(255),\
                ename varchar(255),\
                cname varchar(255),\
                division varchar(255),\
                led40 INT,\
                set40 INT,\
                set100 INT,\
                led200 INT,\
                holder125 INT,\
                bulb250 INT,\
                choke250 INT,\
                ignitor250 INT,\
                switch5a INT,\
                toff INT,\
                wire1 INT,\
                wire7 INT,\
                oname1 varchar(255),\
                oval1 INT,\
                oname2 varchar(255),\
                oval2 INT,\
                rowcost FLOAT)")

    val = messagebox.askokcancel("Finished", 'Database created Successfully')
    print(val)
    phpfile()
    complaints()
    if val:
        root.quit()


# Creating database
def create_database(dataname, ilabel):
    global data_base, cursor, database_name
    database_name = "Esystem20_" + dataname.get()
    try:
        if int(dataname.get()) > 2000 and int(dataname.get()) < 2050:
            forget_frames()
            print(database_name)
            # database_name = 'testing2021'
            try:
                # Creating Database
                cursor.execute(f"CREATE DATABASE {database_name}")
                print("database created")
            except:
                print("drop database")
                cursor.execute(f"DROP DATABASE {database_name}")
                cursor.execute(f"CREATE DATABASE {database_name}")

            # cursor.execute(f"USE {database_name}")
            data_base = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database=database_name
            )
            e_items(database_name)
            cursor = data_base.cursor()
            try:
                # Creating Table Name item_Rates
                cursor.execute("""CREATE TABLE item_rates (item varchar(255), price_rates FLOAT);""")
                print('Table created')
            except:
                print('table droped')
                cursor.execute("DROP TABLE item_rates")
                cursor.execute("""CREATE TABLE item_rates (item varchar(255), price_rates FLOAT);""")
                print('Table created')
        else:
            ilabel.config(text="***Invalid Range")
    except:
        ilabel.config(text="***Enter valid Year")


def database_name():
    forget_frames()
    database_f.pack(fill=BOTH, expand=1)
    Label(database_f, text='Create New Database', font=('Palatino Linotype', 40)).pack(pady=40)
    mini_f = Frame(database_f)
    mini_f.pack(pady=40)
    # Database Name
    Label(mini_f, text='Database Year ', font=('Arial', 15)).grid(row=0, column=0)
    database_name_e = Entry(mini_f, font=('Arial', 15), width=6)
    database_name_e.grid(row=0, column=1)

    invalid_l = Label(mini_f, text="", fg='red', font=('Arial', 15))
    invalid_l.grid(row=1, column=0, columnspan=2, pady=20)

    Button(mini_f, image=next_img, borderwidth=0, command=lambda: create_database(database_name_e, invalid_l)).grid(
        row=2, column=0, columnspan=2, pady=60)


def verification():
    user_name = user_en.get()
    password = psw.get()

    if user_name == 'admin' and password == 'root':
        database_name()
    else:
        incorrect_l.config(text="***Incorrect User Name or Password")
        user_en.delete(0, END)
        psw.delete(0, END)


# Hide All Active Frames
def forget_frames():
    welcome.forget()
    database_f.forget()
    eitem_f.forget()
    mdr_frame.forget()


root = Tk()
root.title("DataBase Generator")
root.geometry("900x600")
root.iconbitmap("img/data.ico")
root.resizable(width=False, height=False)

# Images
login_img = ImageTk.PhotoImage(Image.open("img/login.png").resize((100, 50), Image.ANTIALIAS))
next_img = ImageTk.PhotoImage(Image.open("img/next.png").resize((180, 70), Image.ANTIALIAS))
add_img = ImageTk.PhotoImage(Image.open("img/add.png").resize((90, 35),Image.ANTIALIAS))
finish_img = ImageTk.PhotoImage(Image.open("img/finish.png").resize((180, 70)), Image.ANTIALIAS)
add_text_file = ImageTk.PhotoImage(Image.open("img/es2022/addTextFile.png").resize((30, 30), Image.ANTIALIAS))

# Menus
main_menu = Menu(root)
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label='Exit', command=root.quit)

main_menu.add_cascade(label='File', menu=file_menu)

root.config(menu=main_menu)

# welcome screen
welcome = Frame(root)
welcome.pack(fill=BOTH, expand=1)

# division Frame
division_f = Frame(root)

# Database Frame
database_f = Frame(root)

# Eitems Frame and Rates
eitem_f = Frame(root)

welcome_l = Label(welcome, text='Welcome', font=('Palatino Linotype', 50))
welcome_l.pack(pady=20)
welcome_l = Label(welcome, text='Login as Admin to create new Database', font=('Palatino Linotype', 15))
welcome_l.pack(pady=5)

# User Name and psd Frame
e_box_frame = Frame(welcome)
e_box_frame.pack(pady=50)

# Minister Division Reservation Frame
mdr_frame = Frame(root)

Label(e_box_frame, text='User Name :', font=('Arial', 15)).grid(row=0, column=0, padx=10)
user_en = Entry(e_box_frame, font=('Arial', 15))
user_en.grid(row=0, column=1, pady=10)

Label(e_box_frame, text='Password :', font=('Arial', 15)).grid(row=1, column=0, padx=10)
psw = Entry(e_box_frame, font=('Arial', 15), show="\u25CF")
psw.grid(row=1, column=1, pady=10)

# Hidden label
incorrect_l = Label(e_box_frame, text='', fg='red', font=('Arial', 15))
incorrect_l.grid(row=2, column=0, columnspan=2)

Button(e_box_frame, image=login_img, borderwidth=0, command=verification).grid(row=3, column=0, columnspan=2, pady=40)

mainloop()
