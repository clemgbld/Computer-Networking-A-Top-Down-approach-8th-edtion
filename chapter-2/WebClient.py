from socket import socket, AF_INET, SOCK_STREAM
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("port", type=int)
parser.add_argument("filename")

args = parser.parse_args()


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((args.host, args.port))
clientSocket.send(args.filename.encode())
file = clientSocket.recv(1024)
print("From Server: ", file.decode())
clientSocket.close()
