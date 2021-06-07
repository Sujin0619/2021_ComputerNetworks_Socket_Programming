# import socket module
from socket import *

serverName = '127.0.0.1'  # define local host
serverPort = 1234  # define port number
file_name = 'requestedFile.html'  # set html file name

clientSocket = socket(AF_INET, SOCK_STREAM)  # each means IPv4, TCP
clientSocket.connect((serverName, serverPort))  # connect to server

message = 'GET /' + file_name
# message is GET method

clientSocket.send(message.encode())
# convert the message from string to bytes by using encode() method
# then, send bytes into socket send() method

header = clientSocket.recv(2048).decode()
# receives the header from server
# recv(2048) method means that socket takes the buffer size 2048 as input
messageRecv = clientSocket.recv(2048).decode()
# receives one message from server
# recv(2048) method means that socket takes the buffer size 2048 as input
finalMessage = ''
# finalMessage variable will have all messages from server

while messageRecv:
    finalMessage += messageRecv  # Connect messages
    messageRecv = clientSocket.recv(2048).decode()  # receives next message from sever

print(finalMessage)
clientSocket.close()
# Print finalMessage and close the socket
