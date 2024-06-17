from tkinter import *
import threading
from socket import *
from tkinter import simpledialog
from tkinter import scrolledtext

HOST = gethostname()


class client:
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((HOST, 9999))

        root = Tk()
        root.withdraw()

        self.username = simpledialog.askstring("User Name", "Please Chose nickname", parent=root)
        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        rec_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        rec_thread.start()

    def gui_loop(self):
        self.win = Tk()

        self.chat_l = Label(self.win, text="Chat :", font=('Arial', 20))
        self.chat_l.pack()

        self.text_area = Text(self.win)
        self.text_area.pack()

        self.text_input = Entry(self.win)
        self.text_input.pack()

        self.send_button = Button(self.win, text="Send", command=self.write)
        self.send_button.pack()

        self.gui_done = True



        self.win.mainloop()

    def write(self):
        massage = f"{self.username} : {self.text_input.get()}"
        print(massage)
        self.sock.send(massage.encode('utf-8'))
        self.text_input.delete(0, END)


    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024)
                if message.decode('utf-8') ==  'Nick Name':
                    self.sock.send(self.username.encode('utf-8'))
                else:
                    if self.gui_done:
                        self.text_area.config(state=NORMAL)
                        self.text_area.insert(END, message)
                        self.text_area.yview(END)
                        self.text_area.config(state=DISABLED)

            except ConnectionAbortedError:
                break
            except:

                print("Error")
                self.sock.close()
                break




    def stop(self):
        self.running = False
        self.win.destory()
        self.sock.close()
        exit(0)


client()