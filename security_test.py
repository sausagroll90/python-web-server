import socket

if __name__ == "__main__":

    CONNECTION_PORT = 8080

    client_socket = socket.socket()
    client_socket.connect(("127.0.0.1", CONNECTION_PORT))

    # attempt to access document outside www/ directory
    client_socket.sendall("GET /../hacked.html HTTP/1.1".encode())
    data = client_socket.recv(4096)
    print(data.decode("utf-8"))

    assert data.decode("utf-8") == "HTTP/1.1 400 Bad Request"

    client_socket.close()
