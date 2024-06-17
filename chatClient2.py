from socket import *
import threading
from tkinter import *
from tkinter import simpledialog
from tkinter import scrolledtext


class client:
    def __init__(self):
        self.HOST = '192.168.1.7'
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((self.HOST, 9999))
        # Connection message from server
        print(self.sock.recv(1024).decode('utf-8'))

        # Sending username for server
        msg_box = Tk()
        msg_box.withdraw()
        self.username = simpledialog.askstring("User name", "Enter your user name", parent=msg_box)
        print(self.username)
        self.sock.send(self.username.encode('utf-8'))

        # Calling GUI Application
        GUI_thread = threading.Thread(target=self.GUI)
        GUI_thread.start()

        message_thread = threading.Thread(target=self.message_receive)
        message_thread.start()

    def message_receive(self):
        while True:
            # self.text_box.configure(state=NORMAL)
            message_up = self.sock.recv(1024).decode('utf-8')
            print("Broadcast " + message_up)
            self.text_box.insert(END, message_up + "\n")
            self.text_box.yview(END)
            # self.text_box.configure(state=DISABLED)


    def transfer(self, event):
        # Sending message to server
        msg = self.typo.get()
        self.typo.delete(0, END)
        print(msg)
        self.sock.send(msg.encode('utf-8'))

    def GUI(self):
        self.root = Tk()
        self.root.geometry("500x420")
        self.root.title(f"ChatAPP - {self.username}")
        # Label(root, text=self.username).pack(side=LEFT)
        self.text_box = scrolledtext.ScrolledText(self.root)
        # self.text_box.configure(state=DISABLED)
        self.text_box.pack()

        self.typoFrame = Frame(self.root)
        self.typoFrame.pack()

        self.typo = Entry(self.typoFrame, width=40, font=('Arial', 15))
        self.typo.pack(side=LEFT)

        self.typo.focus()
        self.root.bind('<Return>', self.transfer)
        Button(self.typoFrame, text='Send', command=lambda: self.transfer("Btn")).pack(side=LEFT)

        self.root.mainloop()




client()