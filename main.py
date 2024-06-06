import socket
import threading

# import time


def process_request(request, client_socket):
    # add delay to test handling of concurrent requests
    # time.sleep(1)

    first_line = request.split("\r\n")[0]
    path = first_line.split(" ")[1]

    if path == "/":
        path = "/index.html"

    if ".." in path:
        client_socket.sendall(f"HTTP/1.1 400 Bad Request".encode())
        print("response sent")
        return

    try:
        with open("www" + path) as f:
            html_page = f.read()
            client_socket.sendall(f"HTTP/1.1 200 OK\r\n\r\n{html_page}\r\n".encode())
    except FileNotFoundError:
        client_socket.sendall(f"HTTP/1.1 404 Not Found\r\n".encode())

    print("response sent")


def handle_connection(client_socket):
    with client_socket:
        data = client_socket.recv(4096)
        request = data.decode()
        print(request)
        process_request(request, client_socket)


if __name__ == "__main__":
    PORT = 8080

    server_socket = socket.socket()
    server_socket.bind(("127.0.0.1", PORT))
    server_socket.listen()

    print("Listening on port", PORT)

    while True:
        client_socket, address = server_socket.accept()
        print(f"connection from {address}")
        t = threading.Thread(target=handle_connection, args=[client_socket])
        t.start()
