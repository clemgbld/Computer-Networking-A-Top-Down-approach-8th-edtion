from socket import socket, AF_INET, SOCK_DGRAM
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(("localhost", 12000))
serverSocket.settimeout(10)

currentSequenceNumber = 1

print("Ready to serve")
while True:
    try:
        message, address = serverSocket.recvfrom(1024)
        data = message.split()
        sequenceNumber = int(data[0])
        print(f"""Sequence number: {sequenceNumber}""")
        if currentSequenceNumber < sequenceNumber:
            diff = sequenceNumber - currentSequenceNumber
            print(f"""Packets lost count: {diff}""")
            currentSequenceNumber += diff + 1
        else:
            currentSequenceNumber += 1

        timeStamp = float(data[1])

        print(f"""Time elapsed: {time.time() - timeStamp}ms""")

    except TimeoutError:
        if currentSequenceNumber < 10:
            diff = 10 - currentSequenceNumber
            print(f"""Packets lost count: {diff}""")

        print("Client application has stopped")
        serverSocket.close()
        break
