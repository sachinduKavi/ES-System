from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("canvus")

def move(val):
    global oval_1, x, y
    if val == 'l':
        m_canvas.move(oval_1, -10, 0)
    elif val == 'r':
        m_canvas.move(oval_1, 10, 0)
    elif val == 'u':
        m_canvas.move(oval_1, 0, -10)
    elif val == 'd':
        m_canvas.move(oval_1, 0, 10)

m_canvas = Canvas(root, width=500, height=500, bg='pink')
m_canvas.pack()
x, y = 10, 10
oval_1 = m_canvas.create_oval(x, y, x+10, y+10, fill='red')

root.bind("<Left>", lambda x: move('l'))
root.bind("<Right>", lambda x: move('r'))
root.bind("<Up>", lambda x: move('u'))
root.bind("<Down>", lambda x: move('d'))

mainloop()