# Python Network Programming Project: Simple File Transfer Application

## Objective

Create an application that allows users to transfer files over a network between a client and a server.

## Notes

### Key Concepts

- **Packet**: Single unit of data sent over a network.
- **Endpoint**: Destination for packets.
- **IP Address**: Identifies device.
- **Ports**: Identifies application.
- **Gateway**: Functions as a bridge between networks.

### What is a Socket

- A socket is an interface which handles communication between different machines.
- Network sockets abstract away connection management.
- They take an IP address and port number as parameters and handle connections.

### How Socket Connections Work

- Can either listen for connections, or perform connections.
- They bind to each other. Essentially, when I connect to google.com, a socket on my computer listens to a socket from Google's server.
- Sockets have different protocols built into them.
