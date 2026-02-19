from socket import socket, AF_INET, SOCK_STREAM

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("localhost", serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    str = connectionSocket.recv(4096).decode()
    print(str)
    connectionSocket.send(
        "HTTP/1.1 200 OK \nLast-Modified: Wed, 19 Feb 2025 12:00:00 GMT".encode()
    )
    connectionSocket.close()
