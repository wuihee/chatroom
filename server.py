import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

client_socket, address = server_socket.accept()
print(f"Accepted connection from {address[0]}.")

message = client_socket.recv(1024)
client_socket.send(f"{message.decode()}".encode("utf-8"))
