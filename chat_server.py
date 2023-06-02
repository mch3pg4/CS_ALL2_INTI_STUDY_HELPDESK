import socket
from threading import *

host='192.168.0.142'
port=5000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen()

clients=[]
nicknames=[]

def broadcast(message, prefix=""):
    for client in clients:
        client.send(prefix.encode('utf-8')+message)

def handle_client(client):
    while True:
        try:
            message=client.recv(1024)
            print(f"{nicknames[clients.index(client)]}")
            broadcast(message,nicknames[clients.index(client)]+": ")
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            nicknames.remove(nickname)
            break

def accept_msg():
    while True:
        client,address=server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode('utf-8'))
        nickname=client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} has connected to the server!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread=Thread(target=handle_client,args=(client,))
        thread.start()

print("Server running...")
accept_msg()