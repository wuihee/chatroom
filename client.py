import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.send(input().encode("utf-8"))

message = client_socket.recv(1024)
print(f"From Server: {message.decode()}")
