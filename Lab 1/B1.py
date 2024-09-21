#B1 HTTP REQUEST
from socket import *
serverName = 'www.ingonline.nu'
serverPort = 80

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

clientSocket.send(b"GET /tictactoe/index.php?board=xoxoeoeex HTTP/1.1\r\nHost:www.ingonline.nu\r\nConnection:close\r\n\r\n")
response = clientSocket.recv(4096)
print(response.decode())

clientSocket.close()
