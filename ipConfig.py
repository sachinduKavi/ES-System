from tkinter import *
from tkinter import messagebox


def cancel():
    win3.quit()


def update_ip(ip):
    # Update new ip
    ans = messagebox.askyesno("New IP", f"Do you want to change host Ip as {ip.get()}")
    if ans:
        ip_file = open("ip.txt", "w")
        print(ip.get().strip())
        ip_file.write(ip.get().strip())
        ip_file.close()
        win3.quit()


def caller_ip():
    ip_add()


def ip_add():
    global win3
    win3 = Tk()
    win3.geometry("300x100")
    win3.iconbitmap("img/es2022/ip.ico")
    win3.title("IP Configure")

    mini_ip_frame = Frame(win3)
    mini_ip_frame.pack(pady=15, anchor=W, padx=5)

    Label(mini_ip_frame, text='Enter new host IP address:', font=('Arial', 10)).grid(row=0, column=0, columnspan=2)
    ip_e = Entry(mini_ip_frame, font=('Arial', 10))
    ip_e.grid(row=1, column=0)

    Button(mini_ip_frame, text='Update', command=lambda :update_ip(ip_e)).grid(row=1, column=2)
    Button(mini_ip_frame, text='Cancel', command=cancel).grid(row=1, column=3, padx=5)

    win3.mainloop()

