import socket
import time

CONNECTION_PORT = 8080

client_socket = socket.socket()
client_socket.connect(("127.0.0.1", CONNECTION_PORT))

client_socket.sendall("GET / HTTP/1.1".encode())
data = client_socket.recv(4096)
print(data.decode("utf-8"))

client_socket.close()
