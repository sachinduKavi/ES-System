from tkinter import *
import mysql.connector

# Connecting to database
data_base = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
)

# Initializing cursor
cursor = data_base.cursor()

root = Tk()
root.geometry("400x400")
root.title("Data Extractor")






root.mainloop()