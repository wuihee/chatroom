import socket


def run_server() -> None:
    # Create a socket object.
    # AF_INET - Specifies IP address family for IPV4.
    # SOCK_STREAM - Specifies TCP socket.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
