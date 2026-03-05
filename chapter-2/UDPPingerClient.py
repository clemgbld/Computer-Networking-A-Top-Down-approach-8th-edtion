from socket import socket, AF_INET, SOCK_DGRAM
import time

serverName = "localhost"
serverPort = 12000
times = []
packetsLoss = 0
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(0, 10):
    try:
        print(f"""Ping sequence_number: {i + 1}""")
        start = time.time()
        clientSocket.sendto("a lower case sentence".encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        end = time.time()
        elapsed = end - start
        times.append(elapsed)
        print(f"""RTT: {elapsed}""")
        print(modifiedMessage.decode())
    except TimeoutError:
        packetsLoss += 1
        print("Request timed out")

print(f"""MAX RTT {max(times)}""")
print(f"""MIN RTT {min(times)}""")
print(f"""AVERAGE RTT {sum(times) / len(times)}""")
print(f"""PACKET LOSS RATE {packetsLoss / 10 * 100}%""")


clientSocket.close()
