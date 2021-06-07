# import socket and sys module
from socket import *

serverName = '127.0.0.1'  # define local host
serverPort = 1234  # define server port
serverSocket = socket(AF_INET, SOCK_STREAM)  # each means IPv4, TCP
serverSocket.bind(('', serverPort))  # bind port number to server's socket
serverSocket.listen(1)  # listen TCP connection requests of client

while True:
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(2048)
        # Receives the request message from the client

        filename = message.split()[1]
        # Extract the path of requested object from the message
        # The path is the second part of HTTP header, [1]

        f = open(filename[1:])
        # the extracted path includes '\', read the path from the second

        outputdata = f.read()
        # Read the file and store the entire content of the file in outputdata

        f.close()

        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
        # Send one HTTP header line into socket
        # HTTP/1.1 : HTTP version, 200 : HTTP Status code, OK : Response syntax

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
             connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()  # Close the client socket
        print("OK!")

    except IOError:
        # Send response message for file not found
        connectionSocket.send('\nHTTP/1.1 404 Not Found'.encode())



