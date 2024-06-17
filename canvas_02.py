from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('700x800')
root['bg'] = 'white'

def move(event):
    global img_file
    img_file = ImageTk.PhotoImage(Image.open("img/gonsenH.jpg"))
    l_coordinates.config(text="Coordinates X :" + str(event.x) + " y :" + str(event.y))
    image_ob = m_canvas.create_image(event.x, event.y, image=img_file)

m_canvas = Canvas(root, width=600, height=600, bg='white')
m_canvas.pack(pady=50)

l_coordinates = Label(root, text='Coordinates ')
l_coordinates.pack()

img_file = ImageTk.PhotoImage(Image.open("img/gonsenH.jpg"))
image_ob = m_canvas.create_image(-100, -100, image=img_file)



root.bind("<Motion>", move)


mainloop()