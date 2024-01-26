import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234
HEADER_SIZE = 64

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


def receive_message(client_socket: socket.socket) -> None:
    """
    Receive a message from the server.

    Args:
        client_socket (socket.socket): Client socket to receive message from.
    """
    while True:
        message_length = int(client_socket.recv(HEADER_SIZE).decode("utf-8"))
        print(client_socket.recv(message_length).decode("utf-8"))


def send_message(client_socket: socket.socket, message: str) -> None:
    """
    Send a message through a socket.

    Args:
        client_socket (socket.socket): Socket to send message through.
        message (str): Message to send.
    """
    message_length = len(message)
    header = f"{message_length:>{HEADER_SIZE}}"
    client_socket.send(header.encode("utf-8"))
    client_socket.send(message.encode("utf-8"))


username = input("Enter your name: ")
threading.Thread(target=receive_message, args=(client_socket,)).start()

while True:
    message = input("")
    send_message(client_socket, f"[{username}]: {message}")
