from socket import *  # import socket module

# Prepare a server socket
serverName = "127.0.0.1"
serverPort = 12000  # Server listen through this port
serverSocket = socket(AF_INET, SOCK_STREAM)  # each means IPv4, TCP
serverSocket.bind(('', serverPort))  # bind port number to server's socket
serverSocket.listen(1)  # listen TCP connection requests of client
print("The server is ready to receive.")

try:
    while True:
        # Establish the connection
        print('Ready to serve...')

        connectionSocket, clientAddress = serverSocket.accept()
        # Server creates a new socket dedicated to client by using accept() method
        # clientAddress has IP address and port number of client by using accept() method

        message = connectionSocket.recv(2048)
        # Server receive the message from Client

        modifiedMessage = message.decode().upper()
        # Server converts the message from bytes to a string by decode() method
        # then, capitalizes it by upper() method

        connectionSocket.send(modifiedMessage.encode())
        # Server converts the capitalized message from string to bytes by encode() method

        connectionSocket.close()
        # After sending modifiedMessage, program closes connection socket

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass



