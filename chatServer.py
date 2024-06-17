from socket import *
import threading

# Creating server socket
server_s = socket(AF_INET, SOCK_STREAM)
# Get host name of this host machine
HOST = gethostname()
server_s.bind((HOST, 9999))
# Making host to listen
server_s.listen()

# Creating empty list
clients = []
usernames = []

def broadcast(msg):
    for client in clients:
        client.send(msg.encode('utf-8'))


def receive():
    while True:
        client, addre = server_s.accept()
        print(f"Connected with {addre}")

        client.send("Nick Name".encode('utf-8'))
        clients.append(client)
        username = client.recv(1024)
        usernames.append(username)

        print(f"Nick name of the client is {username}")
        broadcast(f"{username} is now connected with server")
        client.send("Connected with server".encode('utf-8'))
        # Creating new thread
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def handle(client):
    while True:

        message = client.recv(1024)
        print(f"{usernames[clients.index(client)]} sent {message}")
        broadcast(message)



print("Server Running")
receive()
