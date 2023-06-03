import socket
from threading import *

host='192.168.0.142'
port=5000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen()

clients=[]
names=[]

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message=client.recv(1024)
            print(f"{names[clients.index(client)]}")
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            name=names[index]
            names.remove(name)
            break

def accept_msg():
    while True:
        client,address=server.accept()
        print(f"Connected with {str(address)}")

        # client.send("Enter name".encode('utf-8'))
        name=client.recv(1024).decode('utf-8')

        names.append(name)
        clients.append(client)

        print(f"Nickname of the client is {name}")
        broadcast(f"{name} has connected to the server!\n".encode('utf-8'))
        client.send("You have connected to the server".encode('utf-8'))

        thread=Thread(target=handle_client,args=(client,))
        thread.start()

print("Server running...")
accept_msg()