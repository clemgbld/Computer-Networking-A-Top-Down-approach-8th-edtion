from socket import socket, AF_INET, SOCK_STREAM

msg = "I love computer networks!\r\n"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "localhost"
port = 1025
# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))
# Fill in end
recv = clientSocket.recv(1024).decode()


def sendCommand(command, code):
    clientSocket.send(command.encode())
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != code:
        print(f"""{code} reply not received from server.""")


print(recv)
if recv[:3] != "220":
    print("220 reply not received from server.")
# Send HELO command and print server response.
heloCommand = "HELO Alice\r\n"
sendCommand(heloCommand, "250")
# Send MAIL FROM command and print server response.
# Fill in start
fromCommand = "MAIL FROM: <clement@hotmail.fr>\r\n"
sendCommand(fromCommand, "250")
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
rcptToCommand = "RCPT TO: <test@example.com>\r\n"
sendCommand(rcptToCommand, "250")
# Fill in end
# Send DATA command and print server response.
# Fill in start
dataCommand = "DATA\r\n"
sendCommand(dataCommand, "354")
# Fill in end
# Send message data.
# Fill in start
clientSocket.sendto(msg.encode(), (mailserver, port))
# Fill in end
# Message ends with a single period.
# Fill in start
sendCommand(endmsg, "250")
# Fill in end
# Send QUIT command and get server response.
# Fill in start
quitCommand = "QUIT\r\n"
sendCommand(quitCommand, "221")
clientSocket.close()
# Fill in end
