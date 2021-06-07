# import socket module
from socket import *

serverName = "127.0.0.1"
serverPort = 12000  # Server listen through this port
serverSocket = socket(AF_INET, SOCK_DGRAM)  # each means IPv4, UDP
serverSocket.bind(('', serverPort))  # bind port number to server's socket
print("The server is ready to receive.")

try:
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        # Server receives the message from client and put into message variable
        # clientAddress has IP address and port number of client

        modifiedMessage = message.decode().upper()
        # Convert the message from bytes to string by decode() method
        # then, Capitalize it by upper() method

        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        # Send capitalized message to server's socket
        # then, Internet will deliver the message to clientAddress

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass

