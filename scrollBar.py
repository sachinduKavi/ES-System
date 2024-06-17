from tkinter import *

root = Tk()
root.geometry("400x400")
root.iconbitmap("img/p.ico")



main_f = Frame(root, bg='red')

scrollbar = Scrollbar(main_f, orient=VERTICAL)
# config scroll bar

m_list = Listbox(main_f, yscrollcommand=scrollbar)




#scrollbar.config()
scrollbar.config(command=m_list.yview)
scrollbar.pack(side=RIGHT, fill=Y)


main_f.pack()
m_list.pack(pady=10)

for i in range(50):
    m_list.insert(END, i)

root.mainloop()