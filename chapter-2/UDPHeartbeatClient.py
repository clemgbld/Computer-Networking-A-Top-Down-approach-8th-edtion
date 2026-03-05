import random
from socket import socket, AF_INET, SOCK_DGRAM
import time

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(0, 10):
    rand = random.randint(0, 10)
    if rand == 4:
        continue
    sequenceNumber = i + 1
    clientSocket.sendto(
        f"""{sequenceNumber} {time.time()}""".encode(), (serverName, serverPort)
    )
    time.sleep(0.5)


clientSocket.close()
