from socket import *
import threading


serverPort = 7
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')

def handleClient(connectionSocket, address):
   sentence = connectionSocket.recv(1024).decode()
   print(sentence)
   capitalizedSentence = sentence.upper() #kan udelades
   connectionSocket.send(capitalizedSentence.encode())
   connectionSocket.close()


while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target = handleClient,args = (connectionSocket,addr)).start()