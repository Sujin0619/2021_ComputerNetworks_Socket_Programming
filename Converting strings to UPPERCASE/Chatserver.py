#import socket module
from socket import *

serverName = '127.0.0.1'  # define local host
serverPort = 12000  # define server port
serverSocket = socket(AF_INET, SOCK_STREAM)  # each means IPv4, TCP
serverSocket.bind(('', serverPort))  # bind port number to server's socket
serverSocket.listen(1)  # listen TCP connection requests of client
print("The server is ready to receive.")

try:
    while True:
        # Establish the connection
        print('Ready to serve...')

        connectionSocket, clientAddress = serverSocket.accept()
        # Serve r creates a new socket dedicated to client by using accept() method
        # clientAddress has IP address and port number of client by using accept() method

        message = connectionSocket.recv(2048)
        # Server receive the message from Client

        countString = len(message.decode())
        # countString is the length of string
        reversedString = "".join(reversed(message.decode()))
        # reverseString is the reversed string

        connectionSocket.send(bytes([countString]))
        # Server converts the length from int to bytes by bytes method
        connectionSocket.send(reversedString.encode())
        # Server converts the reversed string from string to bytes by encode() method

        connectionSocket.close()
        # After sending modifiedMessage, program closes connection socket

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass



