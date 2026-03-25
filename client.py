import socket
import threading
import sys
import datetime

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


clientpcname = socket.gethostname()
clientIP = socket.gethostbyname(clientpcname)
serverIP = input("Enter server ip: ")
serverport = input("Enter server port: ")
client.connect((serverIP, serverport))

done = False

client_name = input("Enter username: ")
client.send(client_name.encode("utf-16"))
print("press up arrow to enter message")
if (event.type == KEYUP):
    messagetosend = input("Enter message ")
def send_message():
    client.send(f"{messagetosend} --- sent {now} by {client_name} ".encode("utf-16"))

def recieve_message():
    print(client.recv(3024).decode("utf-16"))


while not done:
    now = datetime.datetime.now()
    threading.Thread(target=send_message).start()
    threading.Thread(target=recieve_message).start()
