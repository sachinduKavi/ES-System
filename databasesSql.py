from tkinter import *
import pymysql
from tkcalendar import DateEntry, Calendar
import csv

#clear Button.......
def clear():
    e_Date.delete(0, END)
    e_lname.delete(0, END)
    e_fname.delete(0, END)
    e_mobile.delete(0, END)
    e_description.delete(0, END)
    e_lightnum.delete(0, END)
    e_address.delete(0, END)




root = Tk()
root.title('SK')
root.iconbitmap('img/p.ico')
root.geometry('900x600')

conn = pymysql.connect(
    user='root',
    password='root',
    port=3306,
    database='pythonGui',
)


cursor_n = conn.cursor()

topic = Label(root, text='2021 Light Complains management', font=('Old English Text MT', 40), pady=20,padx=30)
topic.grid(row=0, column=0, columnspan=2)

cursor_n.execute("select * from lcomplains")
print(cursor_n.description)


#submit Button...
def enter():
    global state
    print(state)
    sql_Insert = "INSERT INTO lcomplains (dte,f_name,l_name,mobile_num,address,light_num,description,state_value) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (e_Date.get(),e_fname.get(),e_lname.get(),e_mobile.get(),e_address.get(),e_lightnum.get(),e_description.get(),1)

    cursor_n.execute(sql_Insert,values)
    conn.commit()
    clear()


def export(result):
    with open('Data.csv', 'w') as file:
        w = csv.writer(file, dialect='excel')
        for record in result:
            w.writerow(record)


def look():
    data = Tk()
    data.title('Data')
    data.iconbitmap('img/p.ico')
    data.geometry('1000x400')



    sql_look = "SELECT * FROM lcomplains ORDER BY ref_num DESC"

    cursor_n.execute(sql_look)

    result = cursor_n.fetchall()

    Label(data,text='Ref NO').grid(row=0, column=0, padx=10)
    Label(data,text='Date').grid(row=0, column=1, padx=10)
    Label(data,text='First Name').grid(row=0, column=2, padx=10)
    Label(data,text='Last Name').grid(row=0, column=3, padx=10)
    Label(data,text='Mobile').grid(row=0, column=4, padx=10)
    Label(data,text='Address').grid(row=0, column=5, padx=10)
    Label(data,text='Light Number').grid(row=0, column=6, padx=10)
    Label(data,text='Description').grid(row=0, column=7, padx=10)
    Label(data,text='State').grid(row=0, column=8, padx=10)

    count2 = 1
    for val in result:
        count1 = 0
        for x in val:
            if count1 == 0:
                Label(data, text='RE' + str(x)).grid(row=count2, column=count1, padx=10)
            else:
                Label(data, text=x).grid(row=count2, column=count1, padx=10)
            count1 += 1
        count2 += 1

    b_export = Button(data, text='Export',padx=20, command=lambda :export(result))
    b_export.grid(row=1, column=11, padx=40)




label_date = Label(root, text='Date', font=('Imprint MT Shadow', 17), padx=20).grid(row=1, column=0, sticky=E)
label_fname = Label(root, text='First Name', font=('Imprint MT Shadow', 17), padx=20).grid(row=2, column=0, sticky=E)
label_lname = Label(root, text='Last Name', font=('Imprint MT Shadow', 17), padx=20).grid(row=3, column=0, sticky=E)
label_mobile= Label(root, text='Mobile Number', font=('Imprint MT Shadow', 17), padx=20).grid(row=4, column=0, sticky=E)
label_address = Label(root, text='Address', font=('Imprint MT Shadow', 17), padx=20).grid(row=5, column=0, sticky=E)
label_lightnum = Label(root, text='Light Number', font=('Imprint MT Shadow', 17), padx=20).grid(row=6, column=0, sticky=E)
label_description = Label(root, text='Description', font=('Imprint MT Shadow', 17), padx=20).grid(row=7, column=0, sticky=E)
label_state = Label(root, text='State', font=('Imprint MT Shadow', 17), padx=20).grid(row=8, column=0, sticky=E)


state = IntVar()

e_Date = DateEntry(root, date_pattern="yyyy-mm-dd")
e_Date.grid(row=1, column=1, sticky=W)
e_fname = Entry(root, width=40)
e_fname.grid(row=2, column=1, sticky=W)
e_lname = Entry(root, width=40)
e_lname.grid(row=3, column=1, sticky=W)
e_mobile = Entry(root, width=40)
e_mobile.grid(row=4, column=1, sticky=W)
e_address = Entry(root, width=40)
e_address.grid(row=5, column=1, sticky=W)
e_lightnum = Entry(root, width=40)
e_lightnum.grid(row=6, column=1, sticky=W)
e_description = Entry(root, width=40)
e_description.grid(row=7, column=1, sticky=W)
e_state = Checkbutton(root, text='Done', variable=state, onvalue=1, offvalue=0)
e_state.grid(row=8, column=1, sticky=W)

#reset button
b_reset = Button(root, text='Reset', command=clear, padx=20)
b_reset.grid(row=9, column=0, sticky=E, padx=20)

# submit Button
b_submit = Button(root, text='Submit', command=enter, padx=20)
b_submit.grid(row=9, column=1, sticky=W, padx=20)

#look for data button
b_look = Button(root, text='View Data', command=look, padx=100)
b_look.grid(row=10, column=0, columnspan=2, pady=20)




root.mainloop()