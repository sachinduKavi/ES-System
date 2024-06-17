from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


def price_changer():
    ans = messagebox.askyesno("Caution", "Values you entered only affected for future records only, Do you want Continue ?", parent=w1)
    if ans:
        # Removing previous values
        cursor.execute("DELETE FROM item_rates")
        # Updating table
        cursor.execute(f"""INSERT INTO item_rates values('led40', '{float(led40.get())}')""")
        cursor.execute(f"""INSERT INTO item_rates values('set40', '{float(set40.get())}')""")
        cursor.execute(f"""INSERT INTO item_rates values('led100', '{float(led100.get())}')""")
        cursor.execute(f"""INSERT INTO item_rates values('led200', '{float(led200.get())}')""")
        cursor.execute(f"""INSERT INTO item_rates values('bulb250', '{float(bulb250.get())}')""")
        cursor.execute(f"""INSERT INTO item_rates values('choke250', '{float(choke250.get())}')""")
        cursor.execute(f"""INSERT INTO item_rates values('ignitor250', '{float(ignitor.get())}')""")
        cursor.execute(f"""INSERT INTO item_rates values('holder125', '{float(holder125.get())}')""")
        cursor.execute(f"""INSERT INTO item_rates values('switch5a', '{float(switch.get())}')""")
        cursor.execute(f"""INSERT INTO item_rates values('toff', '{float(toff.get())}')""")
        cursor.execute(f"""INSERT INTO item_rates values('wire1', '{float(wire1.get())}')""")
        cursor.execute(f"""INSERT INTO item_rates values('wire7', '{float(wire7.get())}')""")
        data_base.commit()
        messagebox.showinfo("Updated", "Price rates Updated Successfully", parent=w1)

        global first
        first = True
        w1.destroy()


first = True
def search():
    try:
        global database_name, data_base
        database_name = 'Esystem20_' + year.get()
        ip = open("ip.txt", "r").read()
        print(ip)
        try:
            data_base = mysql.connector.connect(
                host=ip,
                user='root',
                password='root',
                database=database_name
            )
            print("Through Network")
        except:
            messagebox.showerror("ERROR", "Database Name Error", parent=w1)
            w1.destroy()

        # Initialize cursor
        global cursor
        cursor = data_base.cursor()

        # Fetching rates from database
        price_rates = []
        cursor.execute("SELECT * FROM item_rates")
        result = cursor.fetchall()
        for record in result:
            print(record)
            price_rates.append(record[1])

        # Creating entries for price values
        global first
        if first:
            first = False
        else:
            forget_frame()
        global mini_frame
        mini_frame = Frame(w1)
        mini_frame.pack(pady=20, anchor=W, padx=80)

        global led40, set40, led100, led200, bulb250, choke250, ignitor, holder125, switch, toff, wire1, wire7
        Label(mini_frame, text='40W LED Screw Bulb  Rs.', font=('Times', 17)).grid(row=0, column=0, sticky=E)
        led40 = Entry(mini_frame, font=('Times', 17), width=8)
        led40.grid(row=0, column=1, sticky=W, padx=10, pady=3)
        led40.insert(0, price_rates[0])

        Label(mini_frame, text='40W LED (Complete Set)  Rs.', font=('Times', 17)).grid(row=1, column=0, sticky=E)
        set40 = Entry(mini_frame, font=('Times', 17), width=8)
        set40.grid(row=1, column=1, sticky=W, padx=10, pady=3)
        set40.insert(0, price_rates[1])

        Label(mini_frame, text='100W LED (Complete Set)  Rs.', font=('Times', 17)).grid(row=2, column=0, sticky=E)
        led100 = Entry(mini_frame, font=('Times', 17), width=8)
        led100.grid(row=2, column=1, sticky=W, padx=10, pady=3)
        led100.insert(0, price_rates[2])

        Label(mini_frame, text='200W LED (Flash Light)  Rs.', font=('Times', 17)).grid(row=3, column=0, sticky=E)
        led200 = Entry(mini_frame, font=('Times', 17), width=8)
        led200.grid(row=3, column=1, sticky=W, padx=10, pady=3)
        led200.insert(0, price_rates[3])

        Label(mini_frame, text='250W Bulb  Rs.', font=('Times', 17)).grid(row=4, column=0, sticky=E)
        bulb250 = Entry(mini_frame, font=('Times', 17), width=8)
        bulb250.grid(row=4, column=1, sticky=W, padx=10, pady=3)
        bulb250.insert(0, price_rates[4])

        Label(mini_frame, text='250W SV Choke  Rs.', font=('Times', 17)).grid(row=5, column=0, sticky=E)
        choke250 = Entry(mini_frame, font=('Times', 17), width=8)
        choke250.grid(row=5, column=1, sticky=W, padx=10, pady=3)
        choke250.insert(0, price_rates[5])

        Label(mini_frame, text='250W Ignitor  Rs.', font=('Times', 17)).grid(row=6, column=0, sticky=E)
        ignitor = Entry(mini_frame, font=('Times', 17), width=8)
        ignitor.grid(row=6, column=1, sticky=W, padx=10, pady=3)
        ignitor.insert(0, price_rates[6])

        Label(mini_frame, text='125W Screw Holder  Rs.', font=('Times', 17)).grid(row=7, column=0, sticky=E)
        holder125 = Entry(mini_frame, font=('Times', 17), width=8)
        holder125.grid(row=7, column=1, sticky=W, padx=10, pady=3)
        holder125.insert(0, price_rates[7])

        Label(mini_frame, text='5A Switch (Thumbler)  Rs.', font=('Times', 17)).grid(row=8, column=0, sticky=E)
        switch = Entry(mini_frame, font=('Times', 17), width=8)
        switch.grid(row=8, column=1, sticky=W, padx=10, pady=3)
        switch.insert(0, price_rates[8])

        Label(mini_frame, text='T-OFF Connectors  Rs.', font=('Times', 17)).grid(row=9, column=0, sticky=E)
        toff = Entry(mini_frame, font=('Times', 17), width=8)
        toff.grid(row=9, column=1, sticky=W, padx=10, pady=3)
        toff.insert(0, price_rates[9])

        Label(mini_frame, text='1/1.13 Wire (Single)  Rs.', font=('Times', 17)).grid(row=10, column=0, sticky=E)
        wire1 = Entry(mini_frame, font=('Times', 17), width=8)
        wire1.grid(row=10, column=1, sticky=W, padx=10, pady=3)
        wire1.insert(0, price_rates[10])

        Label(mini_frame, text='7/0.53 Wire  Rs.', font=('Times', 17)).grid(row=11, column=0, sticky=E)
        wire7 = Entry(mini_frame, font=('Times', 17), width=8)
        wire7.grid(row=11, column=1, sticky=W, padx=10, pady=3)
        wire7.insert(0, price_rates[11])

        global btn_frame
        btn_frame = Frame(w1)
        btn_frame.pack(anchor=E, padx=20)

        Button(btn_frame, image=update_img, borderwidth=0, command=price_changer).grid(row=0, column=0, padx=7)
        Button(btn_frame, image=cancel_img, borderwidth=0, command=forget_frame).grid(row=0, column=1, padx=7)

    except:
        messagebox.showerror("Invalid database name", "Unknown data base year please try again", parent=w1)
        forget_frame()


def forget_frame():
    mini_frame.forget()
    for child in mini_frame.winfo_children():
        child.destroy()

    btn_frame.forget()
    for child in btn_frame.winfo_children():
        child.destroy()


def rateUpdater():
    global w1
    w1 = Toplevel()
    w1.title("Price Rate Updater")
    w1.geometry("600x700")
    w1.resizable(width=False, height=False)
    w1.iconbitmap("img/es2022/update2.ico")

    # importing Images
    global update_img, cancel_img
    price_rates_img = ImageTk.PhotoImage(Image.open("img/es2022/priceRates.png").resize((400, 60)), Image.ANTIALIAS)
    search_1_img = ImageTk.PhotoImage(Image.open("img/es2022/search.png").resize((130, 40), Image.ANTIALIAS))
    update_img = ImageTk.PhotoImage(Image.open("img/es2022/update.png").resize((150, 65), Image.ANTIALIAS))
    cancel_img = ImageTk.PhotoImage(Image.open("img/es2022/cancel.png").resize((120, 35), Image.ANTIALIAS))

    # Heading
    Label(w1, image=price_rates_img).pack(pady=20)
    search_frame = Frame(w1)
    search_frame.pack()

    # Search Database
    Label(search_frame, text='year :', font=('Times', 17)).grid(row=0, column=0)
    global year
    year = Entry(search_frame, width=7, font=('Arial', 17))
    year.grid(row=0, column=1, padx=20)

    Button(search_frame, image=search_1_img, borderwidth=0, command=search).grid(row=0, column=2)

    mainloop()












