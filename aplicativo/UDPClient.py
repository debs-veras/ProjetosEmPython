from socket import*
serverName = '192.168.1.103'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = -1

while message:
  message = input('O que você deseja?: ')
  clientSocket.sendto(message.encode(), (serverName, serverPort))

clientSocket.close()