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
        message = client_socket.recv(1024)
        if message:
            print(f"Echoing Data: {message.decode('utf-8')}")
            client_socket.sendall(message)
        else:
            print("Closing connection.")
            selector.unregister(client_socket)
            client_socket.close()


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
