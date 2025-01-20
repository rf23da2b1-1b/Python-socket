from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    toAddress = clientAddress
    modifiedMessage = message.decode()
    print('Modtaget ', modifiedMessage, '     fra adresse ', clientAddress, ' til adresse ', clientAddress.)
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
