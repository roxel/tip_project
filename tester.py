import socket


def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))


if __name__ == "__main__":
    host, port = "127.0.0.1", 5000

    client(host, port, "Hello World 1")
    client(host, port, "Hello World 2")
    client(host, port, "Hello World 3")

