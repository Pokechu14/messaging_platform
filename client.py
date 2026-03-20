import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("192.168.100.12", 9090))

done = False

client_name = input("Enter the name of your client: ")
client.send(client_name.encode("utf-8"))

def send_message():
    client.send(input().encode("utf-8"))

def recieve_message():
    print(client.recv(1024).decode("utf-8"))


while not done:
    threading.Thread(target=send_message).start()
    threading.Thread(target=recieve_message).start()