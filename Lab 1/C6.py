#C6 TCP SERVER
from socket import *
PORT = 12000
START = 10000
i=0

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", PORT))

serverSocket.listen(1)

print("Server running...")
connectionSocket, addr = serverSocket.accept()

while True:
    message = connectionSocket.recv(1500).decode()

    if(message[0:5] != str(START+i)):
        print("ERROR! MISSING PACKETS")

    i+=1
