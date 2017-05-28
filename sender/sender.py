import socket
import threading
import socketserver


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    ip = "127.0.0.1"
    port = 8080

    def forward(self, ip, port, message):
        print("forwarding")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ip, port))
            sock.sendall(message)
            response = sock.recv(1024)
            return response

    def handle(self):
        print("handling")
        data = self.request.recv(1024)
        response = self.forward(self.ip, self.port, data)
        self.request.sendall(response)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 5000

    print("starting sender")

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    with server:
        ip, port = server.server_address

        # # Start a thread with the server -- that thread will then start one
        # # more thread for each request
        # server_thread = threading.Thread(target=server.serve_forever)
        # # Exit the server thread when the main thread terminates
        # server_thread.daemon = True
        # server_thread.start()
        # print("Server loop running in thread:", server_thread.name)

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()

