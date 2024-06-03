import socket

PORT = 8080

server_socket = socket.socket()
server_socket.bind(("127.0.0.1", PORT))
server_socket.listen()


def process_request(request, client_socket):
    first_line = request.split("\r\n")[0]
    path = first_line.split(" ")[1]
    if path in ["/", "/index.html"]:
        with open("index.html") as f:
            html_page = f.read()
            client_socket.send(f"HTTP/1.1 200 OK\r\n\r\n{html_page}\r\n".encode())
    else:
        client_socket.send(f"HTTP/1.1 404 Not Found\r\n".encode())


while True:
    client_socket, address = server_socket.accept()
    print(f"connection from {address}")
    with client_socket:
        data = client_socket.recv(4096)
        request = data.decode()
        print(request)
        process_request(request, client_socket)