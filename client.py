import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.send(b"Testing 123..")
data = client_socket.recv(1024)

print(f"Recieved {data!r}")
