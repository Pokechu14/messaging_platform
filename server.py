import socket
import threading

clients = {}

#initialize server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "192.168.100.12"
PORT = 9090

server.bind((HOST, PORT))
server.listen()


def add_client():
    client, addr = server.accept()
    client_name = client.recv(1024).decode("utf-8")
    clients[client_name] = client   #clients[example].send("example".encode("utf-8"))
    print(f"Succesfully connected to {client_name}!")

def handle_client(client_socket, client_name):
    while True:
        message = client_socket.recv(1024).decode("utf-8")
        if message == "":
            del clients[client_socket]
            break
        
        for socket in clients.values():
            socket.send(f"{client_name}: {message}".encode("utf-8"))
    




"""
done = False
while not done:
    msg = client.recv(1024).decode("utf-8")
    if msg.lower() == "quit":
        done = True
    else:
        print(msg)

    
    client.send(input("Message: ").encode("utf-8"))
"""