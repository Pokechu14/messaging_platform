import socket
import threading

clients = {}
clients_lock = threading.Lock()


#initialize server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "192.168.100.12"
PORT = 9090

server.bind((HOST, PORT))
server.listen()


def add_client():
    client, addr = server.accept()
    client_name = client.recv(1024).decode("utf-8")
    with clients_lock:
        clients[client_name] = client   #clients[example].send("example".encode("utf-8"))
    print(f"Succesfully connected to {client_name}!")
    return client, client_name

def handle_client(client_socket, client_name):
    while True:
        message = client_socket.recv(1024).decode("utf-8")
        if message == "":
            with clients_lock:
                if client_name in clients:
                    del clients[client_name]
            break
        

        with clients_lock:
            sockets = list(clients.values())
        
        for socket in sockets:
            if socket != client_socket:
                socket.send(f"{client_name}: {message}".encode("utf-8"))
    

running = True
while running:
    client, client_name = add_client()

    threading.Thread(
        target=handle_client,
        args=(client, client_name),
        daemon=True
    ).start()
