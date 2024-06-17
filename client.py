# Client
from socket import *
import time
from tkinter import *

s = socket(AF_INET, SOCK_STREAM)

# Get machine name
host = gethostname()

# Connection to host
s.connect((host, 9999))

msg = s.recv(1024)

s.close()

print(msg.decode("ascii"))
