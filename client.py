import socket
import threading
import datetime
import sys

now = datetime.datetime.now()
clientname = socket.gethostname()
clientIP = socket.gethostbyname(clientname)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
platform = sys.platform
if platform == win32:
    clientWINVER = sys.getwindowsversion().major

#aten servu on 192.168.100.
#aten servun portti on 9090
serverIP = (input("Enter server IP:")
serverPORT = (input("Enter server port:")

client.connect((serverIP, serverPORT))

done = False #bruh

client_name = input("Enter the name of your client: ")
client.send(client_name.encode("utf-16"))

def send_message():
    client.send(input("Enter message:"),now.encode("utf-16"))

def recieve_message():
    print(client.recv(1024),.decode("utf-16"))


while not done:                  #aw hell nah man
    threading.Thread(target=send_message).start()
    threading.Thread(target=recieve_message).start()
