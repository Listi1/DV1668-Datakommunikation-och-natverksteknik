#C5 TCP CLIENT
from socket import *
import time
SERVER = "192.168.0.4"
PORT = 12000
NUM = 10000
FILLER = "A"*1430
SENDS = 1000
i = 0

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((SERVER, PORT))

while i < SENDS:
    clientSocket.send(str(str(NUM+i)+";"+str(FILLER)+"####").encode())
    i+=1
    time.sleep(0.015)

clientSocket.close()