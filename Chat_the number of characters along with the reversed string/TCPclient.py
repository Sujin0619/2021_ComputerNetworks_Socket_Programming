from socket import *  # import socket module

serverName = '127.0.0.1'  # define local host so that server can listen
serverPort = 12000  # define server port so that server can listen
clientSocket = socket(AF_INET, SOCK_STREAM)  # each means IPv4, TCP
clientSocket.connect((serverName, serverPort))  # connect to server


message = input("Input lowercase sentence: ")  # input from client
clientSocket.send(message.encode())
# convert the message from string to bytes by using encode() method
# then, send bytes into socket send() method


modifiedMessage = clientSocket.recv(2048)
# receive modified message from server
# recv(2048) method means that socket takes the buffer size 2048 as input


print("From Server : ", modifiedMessage.decode())
# Convert modifiedMessage from bytes to string and Print it


clientSocket.close()  # Then, close the socket


