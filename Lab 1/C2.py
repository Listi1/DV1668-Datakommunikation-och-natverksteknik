#C2 UDP SERVER
from socket import *

PORT = 12000
START = 10000
i=0

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", PORT))

print("Server running...")

while True:
    message = serverSocket.recv(1500).decode()

    if(message[0:5] != str(START+i)):
        print("ERROR! MISSING PACKETS")

    i+=1