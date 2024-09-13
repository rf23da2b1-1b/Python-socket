from socket import *

# slags konstanter
serverName = 'localhost'
serverPort = 7


clientSocket = socket(AF_INET, SOCK_STREAM) # Stream = tcp
clientSocket.connect( (serverName,serverPort) )

# læser input fra skærm/tastetur
sentence = input('Input : ')

sentence = sentence + '\r\n'
byteSentence = sentence.encode() # laver tegn til byte
clientSocket.send(byteSentence)

#venter på svar
returnSentence = clientSocket.recv(1024)
print('Modtaget: ', returnSentence.decode()) # byte til tegn

clientSocket.close()