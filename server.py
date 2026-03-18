import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "192.168.100.12"
PORT = 9090

server.bind((HOST, PORT))
server.listen()

client, addr = server.accept()

client_name = client.recv(1024).decode("utf-8")
print(f"Succesfully connected to {client_name}!")

done = False

while not done:
    msg = client.recv(1024).decode("utf-8")
    if msg.lower() == "quit":
        done = True
    else:
        print(msg)

    
    client.send(input("Message: ").encode("utf-8"))