from tkinter import *

root = Tk()
root.title("sk")
root.geometry("400x400")
root.iconbitmap("img/p.ico")

pannel1 = PanedWindow(bd=4, relief="raised", bg='red')
pannel1.pack(fill=BOTH, expand=1)

label_01 = Label(pannel1, text="hey")
pannel1.add(label_01)





root.mainloop()

