from socket import *

serverName = '127.0.0.1'  # define local host
serverPort = 1234  # define port number
clientSocket = socket(AF_INET, SOCK_STREAM)  # each means IPv4, TCP
clientSocket.connect((serverName, serverPort))  # connect to server

filename = 'sent_data.txt'
# The file name which client want to receive from the server
filenameReceived = 'Received_data.txt'
# The file name to store data received from the server

clientSocket.sendall(filename.encode('utf-8'))  # Send the name of file

reSize = clientSocket.recv(2048)
# if the server has a file, client will receive the size of the file
# if not, client will receive an error message
reSize = reSize.decode()
# Convert the bytes to string

if reSize == "error":  # This means that the server doesn't have the file
    print("No file")
    clientSocket.close()


with open(filenameReceived, 'wt', encoding="UTF-8") as f:
    # Open the new text file and write the text
    data = clientSocket.recv(int(reSize))
    # Get data as big as the size of file from server
    f.write(data.decode())
    # Write data to file of client
    clientSocket.sendall(data.decode().encode())
    # Send the data received from the server to server
