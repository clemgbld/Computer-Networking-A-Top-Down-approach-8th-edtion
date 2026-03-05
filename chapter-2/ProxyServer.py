from socket import socket, AF_INET, SOCK_STREAM
import sys

if len(sys.argv) <= 1:
    print(
        'Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IPAddress Of Proxy Server'
    )
    sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
tcpSerSock.bind((sys.argv[1], int(sys.argv[2])))
tcpSerSock.listen(1)
# Fill in end.
while 1:
    # Strat receiving data from the client
    print("Ready to serve...")
    tcpCliSock, addr = tcpSerSock.accept()
    print("Received a connection from:", addr)
    message = tcpCliSock.recv(3000).decode()
    print(message)
    # Extract the filename from the given message
    print("filename:", message.split()[1])
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n".encode())
        # Fill in start.
        tcpCliSock.send("\r\n".encode())
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i].encode())

        # Fill in end.
        print("Read from cache")
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.", "", 1)
            print(hostn)
            try:
                # Connect to the socket to port 80
                # Fill in start.
                c.connect((hostn, 80))
                # Fill in end.
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                # request = f"GET /{filename} HTTP/1.1\r\n"
                request = "GET / HTTP/1.1\r\n"
                request += f"""Host: {hostn}\r\n"""
                request += "Connection: close\r\n"
                request += "\r\n"
                c.send(request.encode())
                fileobj = c.makefile("rb", 0)
                # Read the response into buffer
                # Fill in start.
                response = fileobj.readlines()
                shouldCache = True
                httpStatusCode = response[0].decode().split()[1]
                if not httpStatusCode.startswith("2"):
                    shouldCache = False

                ## Fill in end.
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket  and the corresponding file in the cache
                tmpFile = open(filename, "w")
                # Fill in start.
                for i in range(0, len(response)):
                    chunk = response[i]
                    str = chunk.decode()
                    if shouldCache:
                        tmpFile.write(str)
                    tcpCliSock.send(chunk)
                tmpFile.close()
            # Fill in end.
            except Exception as e:
                print("Illegal request", e)
            finally:
                c.close()
        else:
            # HTTP response message for file not found
            # Fill in start.
            tcpCliSock.send("HTTP/1.1 404 Not Found\r\n".encode())
            # Fill in end
    # Close the client and the server sockets
    finally:
        tcpCliSock.close()
# Fill in start.
tcpSerSock.close()
# Fill in end.
