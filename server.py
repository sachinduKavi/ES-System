# Server python
from tkinter import *
from socket import *
import time



# Creating server socket
server_s = socket(AF_INET, SOCK_STREAM)
# Get host name by gethostname() function
host = gethostname()

print(host)
# Binding server host name to socket
server_s.bind((host, 9999))


# Server listening up to 5 clients
server_s.listen(5)
while True:
    client_s, addr = server_s.accept()
    print("got a connection", client_s, addr)
    # print(client_s)
    client_s.send("Connection successful to the server".encode("ascii"))
    msg = client_s.recv(1024)
    print(msg.decode('ascii'))


    client_s.close()

