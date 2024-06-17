from socket import *
import threading

# Creating socket
server_sock = socket(AF_INET, SOCK_STREAM)
HOST = gethostname()
server_sock.bind((HOST, 9999))

# Waiting for client
server_sock.listen()

# Creating empty lists
clients = []
usernames = []


def connection():
    while True:
        print("New server loop, Waiting.......")
        # Establishing new Connection
        client, address = server_sock.accept()
        if client not in clients:
            print(f"New connection from {address}")
            clients.append(client)
            client.send("Connection successful".encode('utf-8'))

            username = client.recv(1024).decode('utf-8')
            print(username)
            usernames.append(username)
            # Creating a new thread
            client_thread = threading.Thread(target=handle, args=(client, username))
            client_thread.start()

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except:
            print(clients.index(client))

def handle(client, username):
    while True:
        # New Message From client
        try:
            message = username + " : " + client.recv(1024).decode('utf-8')
            print(message)
            broadcast(message)
        except ConnectionResetError:
            print("Client has been offline")
            break


connection()