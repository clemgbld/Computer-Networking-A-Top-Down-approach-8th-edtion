# import socket module
from socket import socket, AF_INET, SOCK_STREAM

# import sys  # In order to terminate the program
import threading

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverPort = 12000
serverSocket.bind(("localhost", serverPort))
serverSocket.listen(1)
# Fill in end


def task(connectionSocket):
    try:
        filename = connectionSocket.recv(1024).decode()
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send("HTTP/1.1 200 OK".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("Content-type: text/html".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("\r\n".encode())
        # Fill in end
        # Send the content of the requested file to the client
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found".encode())
        connectionSocket.send("\r\n".encode())
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()


while True:
    # Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    thread = threading.Thread(target=task, args=(connectionSocket,))
    thread.start()

    # Fill in end
    # serverSocket.close()
    # sys.exit()  # Terminate the program after sending the corresponding data
