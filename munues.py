from tkinter import *

def new_file():
    forget()
    file_new_frame.pack(fill='both', expand=1)
    l01 = Label(file_new_frame, text="hello").pack()


def edit():
    forget()
    file_edit_frame.pack()


def forget():
    file_new_frame.pack_forget()
    file_edit_frame.pack_forget()



root = Tk()
root.title("SK")
root.iconbitmap("img/p.ico")
root.geometry("400x400")

m_menu = Menu(root)
root.config(menu=m_menu)


file = Menu(m_menu)
Edit = Menu(m_menu)
View = Menu(m_menu)

m_menu.add_cascade(label="File", menu=file)
file.add_command(label="New", command=new_file)
file.add_command(label="New Project")

file.add_separator()

file.add_command(label="Save")
file.add_command(label="Save as")

file.add_separator()


file.add_command(label="Exit", command=root.quit)

file.add_separator()

m_menu.add_cascade(label="Edit", menu=Edit)
Edit.add_command(label="hello", command=edit)



m_menu.add_cascade(label="View", menu=View)
View.add_command(label='Tool Window')

file_new_frame = Frame(root, width=400, height=400, bg='red')
file_edit_frame = Frame(root, width=400, height=400, bg='blue')





root.mainloop()