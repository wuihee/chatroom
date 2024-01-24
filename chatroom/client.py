import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234
HEADER_SIZE = 64

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


while True:
    message = input("> ")
    message_length = len(message)
    header = f"{message_length:>{HEADER_SIZE}}"
    client_socket.send(header.encode("utf-8"))
    client_socket.send(message.encode("utf-8"))
