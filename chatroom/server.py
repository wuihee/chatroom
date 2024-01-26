import selectors
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234
HEADER_SIZE = 64

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
    active_clients.append(client_socket)


def broadcast(message: str) -> None:
    """
    Broadcast message to all active clients.

    Args:
        message (str): Message to broadcast.
    """
    for client_socket in active_clients:
        message_length = len(message)
        header = f"{message_length:>{HEADER_SIZE}}"
        client_socket.send(header.encode("utf-8"))
        client_socket.send(message.encode("utf-8"))


def receive_message(key: selectors.SelectorKey, mask: int) -> None:
    """
    Receive a message from an existing connection.

    Args:
        key (selectors.SelectorKey): The ready socket object.
        mask (int): Bitmask of events ready.
    """
    client_socket = key.fileobj
    if mask & selectors.EVENT_READ:
        message_length = int(client_socket.recv(HEADER_SIZE).decode("utf-8"))
        message = client_socket.recv(message_length).decode("utf-8")
        broadcast(message)


print(f"Server started on {HOST} on port {PORT}.")

try:
    while True:
        events = selector.select(timeout=None)
        for key, mask in events:
            if key.fileobj is server_socket:
                accept_connection(server_socket)
            else:
                receive_message(key, mask)
except KeyboardInterrupt:
    print("Server is shutting down.")
finally:
    server_socket.close()
    selector.close()
