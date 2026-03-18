import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("192.168.100.12", 9090))

done = False

client_name = input("Enter the name of your client: ")
client.send(client_name.encode("utf-8"))

while not done:
    client.send(input("Message: ").encode("utf-8"))
    print(client.recv(1024).decode("utf-8"))