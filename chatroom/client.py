import socket

from .constants import PORT
from .utils import send_message

HOST = socket.gethostbyname(socket.gethostname())

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


while True:
    send_message(client_socket, input("> "))
