import socket

from constants import HEADER_SIZE


def send_message(sock: socket.socket, message: str) -> None:
    """
    Send a message through socket.

    Args:
        message (str): Message to be sent.
        sock (socket.socket): Socket to send message to.
    """
    message = message.encode("utf-8")
    message_length = len(message)
    header = f"{message_length:>{HEADER_SIZE- message_length}}".encode("utf-8")
    sock.send(header)
    sock.send(message)
