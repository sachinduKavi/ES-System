from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import pygame
import os
import time
from mutagen.mp3 import MP3


turn = True
root = Tk()
root.geometry("430x390")
root.title("Music")
root.resizable(width=False, height=False)
root.iconbitmap("img/music/music.ico")
root.config(bg='white')


pygame.mixer.init()

def keyboard(event):
    print(event)
    print(event.keycode)
    if event.keycode == 98:
        next()
    elif event.keycode == 104:
        back()
    elif event.keycode == 13:
        play()
    elif event.keycode == 32:
        pause()


def play_time():
    curr_time = pygame.mixer.music.get_pos() / 1000

    # Get song length through mutagen
    curr_song = "audio/" + play_list.selection_get() + ".mp3"
    song_len = MP3(curr_song).info.length
    print(song_len)
    curr_time = time.strftime('%M:%S', time.gmtime(curr_time))
    song_len = time.strftime('%M:%S', time.gmtime(song_len))
    print(curr_time)
    status_bar.config(text=curr_time + "  /  " + song_len)
    status_bar.after(1000, play_time)


def play():
    song = "audio/" + play_list.selection_get() + ".mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    play_time()


def pause():
    global turn
    if turn:
        pygame.mixer.music.pause()
        turn = False
    else:
        pygame.mixer.music.unpause()
        turn = True


def stop():
    pygame.mixer.music.stop()
    status_bar.config(text='')




def add_songs():
    song = filedialog.askopenfilename(initialdir='audio/', title='Add Songs', filetypes=(('MP3', 'mp3'),))
    song = song.replace("D:/PythonGUI/audio/", "")
    song = song.replace(".mp3", "")
    play_list.insert(0, song)


def next():
    next_num = play_list.curselection()
    next_num = next_num[0] + 1
    if next_num == play_list.size():
        next_num = 0
    play_list.selection_clear(0, END)
    play_list.selection_set(next_num)
    play()


def back():
    next_num = play_list.curselection()
    next_num = next_num[0] - 1
    if next_num < 0:
        next_num = 8
    play_list.selection_clear(0, END)
    play_list.selection_set(next_num)
    play()


play_list = Listbox(root, width=60, height=15, bg='#004F5E', fg='white', activestyle='none')
play_list.pack(pady=20)

# add all songs to play list in audio dir
all_song = os.listdir('audio')
for item in all_song:
    item = item.replace(".mp3", "")
    play_list.insert(END, item)


# importing images foe buttons
play_img = ImageTk.PhotoImage(Image.open('img/music/play.png').resize((50, 50)), Image.ANTIALIAS)
pause_img = ImageTk.PhotoImage(Image.open('img/music/pause.png').resize((50, 50)), Image.ANTIALIAS)
next_img = ImageTk.PhotoImage(Image.open('img/music/next.jpg').resize((50, 50)), Image.ANTIALIAS)
back_img = ImageTk.PhotoImage(Image.open('img/music/back.jpg').resize((50, 50)), Image.ANTIALIAS)
stop_img = ImageTk.PhotoImage(Image.open('img/music/stop.png').resize((50, 50)), Image.ANTIALIAS)

# button frame
btn_frame = Frame(root)
btn_frame.pack(pady=10)

# Creating buttons
Button(btn_frame, image=back_img, borderwidth=0, command=back).grid(row=0, column=0, padx=12)
Button(btn_frame, image=pause_img, borderwidth=0, command=pause).grid(row=0, column=1, padx=12)
Button(btn_frame, image=play_img, borderwidth=0, command=play).grid(row=0, column=2, padx=12)
Button(btn_frame, image=stop_img, borderwidth=0, command=stop).grid(row=0, column=3, padx=12)
Button(btn_frame, image=next_img, borderwidth=0, command=next).grid(row=0, column=4, padx=12)

# Menus
main_menu = Menu(root)
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Add Music", command=add_songs)
file_menu.add_command(label='Exit', command=root.quit)
main_menu.add_cascade(label='File', menu=file_menu)

command_menu = Menu(main_menu, tearoff=0)
command_menu.add_command(label='Play', command=play)
command_menu.add_command(label='Pause', command=pause)
command_menu.add_command(label='Stop', command=stop)
command_menu.add_command(label='Next', command=next)
command_menu.add_command(label='Back', command=back)
main_menu.add_cascade(label='Command', menu=command_menu)

root.config(menu=main_menu)

# Add Status Bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E, padx=10)
status_bar.pack(side=BOTTOM, fill=X, ipady=2)


# keyboard binding
root.bind("<Key>", keyboard)


root.mainloop()
