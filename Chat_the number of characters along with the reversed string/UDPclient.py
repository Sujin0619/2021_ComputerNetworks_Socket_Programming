# import socket module
from socket import *

serverName = "127.0.0.1"  # define local host so that server can listen
serverPort = 12000  # define server port so that server can listen
clientSocket = socket(AF_INET, SOCK_DGRAM)  # each means IPv4, UDP

message = input("Input lowercase sentence: ")  # input from client
clientSocket.sendto(message.encode(), (serverName, serverPort))
# convert the message from string to bytes by encode() method
# Attach the destination address to the messages
# then, send bytes into client socket

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# When the capitalized message arrives at the client's socket
# message put into modifiedMessage variable
# serverAddress has IP address and port of server

print(modifiedMessage.decode())
# Convert the message from bytes to string
# then, print it

clientSocket.close()


