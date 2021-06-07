from socket import *
import os
from os.path import exists

serverName = '127.0.0.1'  # define local host
serverPort = 1234  # define server port
serverSocket = socket(AF_INET, SOCK_STREAM)  # each means IPv4, TCP
print("Initialising Winsock... Initialised.")
serverSocket.bind(('', serverPort))  # bind port number to server's socket
print("Bind Success.")
serverSocket.listen(1)  # listen TCP connection requests of client

nowdir = os.getcwd()  # nowdir means the current directory


def getfiledata(fileName, directory):
    # Function that returns data in a file
    with open(directory + "\\" + fileName, 'r', encoding="UTF-8") as f:
        # Open and read file in the directory
        data = ""
        for line in f:  # Read the contents of the file line by line
            data += line  # Put the lines we read into the variable 'data' in order
    return data  # Finally, the data is returned


def getfilesize(fileName, directory):  # Function that returns file size
    fileSize = os.path.getsize(directory + "\\" + fileName)  # File size in directory
    return str(fileSize)  # Converts the size of the file to a string and returns it


while True:
    print("Wating for connection...")
    connectionSocket, addr = serverSocket.accept()

    filename = connectionSocket.recv(2048)
    # Receives the file name in binary byte stream from the client
    filename = filename.decode('utf-8')  # Converts the bytes to string

    if not exists(nowdir + "\\" + filename):
        # if there is no file in the current directory
        msg = "error"
        connectionSocket.sendall(msg.encode())  # Send an error message
        connectionSocket.close()

    connectionSocket.sendall(getfilesize(filename, nowdir).encode())
    # Send the size of the file using the 'getfilesize' function
    connectionSocket.sendall(getfiledata(filename, nowdir).encode())
    # Send the contents of the file using the 'getfiledata' function

    received_data = connectionSocket.recv(2048)
    # Receive the data that server sent to the client
    print("Received data = " + received_data.decode())  # Print the data
    print('Writing success!')
    print('Press any key to continue...')
