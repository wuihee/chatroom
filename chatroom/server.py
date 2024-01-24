import selectors
import socket

from utils import send_message

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234
HEADER = 64

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
server_socket.setblocking(False)

selector = selectors.DefaultSelector()
selector.register(server_socket, selectors.EVENT_READ)
active_clients = []


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


def broadcast_message(message: str) -> None:
    """
    Broadcast message to all clients.

    Args:
        message (str): Message to broadcast.
    """
    pass


def service_connection(key: selectors.SelectorKey, mask: int) -> None:
    """
    Recieve a message from an existing connection.

    Args:
        key (selectors.SelectorKey): The ready socket object.
        mask (int): Bitmask of events ready.
    """
    client_socket = key.fileobj
    # If the event is the read from the socket,
    if mask & selectors.EVENT_READ:
        message_length = int(client_socket.recv(HEADER).decode("utf-8"))
        message = client_socket.recv(message_length).decode("utf-8")
        print(f"[{client_socket.getsockname()[0]}]: {message}")


print(f"Server started on {HOST} on port {PORT}.")

try:
    while True:
        events = selector.select(timeout=None)
        for key, mask in events:
            # When fileobj is server_socket, server_socket is ready to be read
            # from, i.e. there is a new client connection incomming.
            if key.fileobj is server_socket:
                accept_connection(server_socket)
            # If the fileobj is not the server_socket, it means one of the
            # client sockets registered wants to send a message.
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Server is shutting down.")
finally:
    server_socket.close()
    selector.close()
