import selectors
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
server_socket.setblocking(False)

selector = selectors.DefaultSelector()
selector.register(server_socket, selectors.EVENT_READ)


def accept_connection(server_socket: socket.socket) -> None:
    """
    Accept a new connection from a new client.

    Args:
        server_socket (socket.socket): Socket object for the server.
    """
    client_socket, address = server_socket.accept()
    print(f"Accepted connection from {address[0]}.")
    client_socket.setblocking(False)
    selector.register(client_socket, selectors.EVENT_READ)


def service_connection():
    pass


while True:
    client_socket, address = server_socket.accept()
    print(f"Accepted connection from {address[0]}.")

    message = client_socket.recv(1024)
    client_socket.send(f"{message.decode()}".encode("utf-8"))
