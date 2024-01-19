import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello World")
    data = s.recv(1024)


print(f"Received {data!r}")
