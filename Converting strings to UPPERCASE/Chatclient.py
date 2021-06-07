# import socket module
from socket import *

serverName = '127.0.0.1'  # define local host
serverPort = 12000  # define server port
clientSocket = socket(AF_INET, SOCK_STREAM)  # each means IPv4, TCP
clientSocket.connect((serverName, serverPort))  # connect to server

message = input("Input sentence: ")  # input from client
clientSocket.send(message.encode())
# convert the message from string to bytes by using encode() method
# then, send bytes into socket send() method

countMessage = clientSocket.recv(2048)
# receives the length of string from server
# recv(2048) method means that socket takes the buffer size 2048 as input
reversedMessage = clientSocket.recv(2048)
# receive reversed message from server
# recv(2048) method means that socket takes the buffer size 2048 as input

print("The number of characters : ", int.from_bytes(countMessage, byteorder='big'))
# Convert the countMessage from bytes to int by 'int.from_bytes(bytes, byteorder)' method
print("The reversed strings(s) : ", reversedMessage.decode())
# Convert the reverseMessage from bytes to string by decode() method

clientSocket.close()
# Then close the socket

