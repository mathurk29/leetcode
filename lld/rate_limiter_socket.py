import socket
import threading
import time

class RateLimiter:
    def __init__(self, rate_limit, time_window):
        self.rate_limit = rate_limit
        self.time_window = time_window
        self.lock = threading.Lock()
        self.client_requests = {}

    def handle_request(self, client_socket):
        client_address = client_socket.getpeername()

        with self.lock:
            if client_address not in self.client_requests:
                self.client_requests[client_address] = []

            current_time = time.time()
            requests = self.client_requests[client_address]

            # Remove requests that are outside the time window
            requests = [req for req in requests if req >= current_time - self.time_window]

            if len(requests) >= self.rate_limit:
                # Reject the request if rate limit is exceeded
                response = "HTTP/1.1 429 Too Many Requests\r\n"
                response += "Content-Length: 0\r\n"
                response += "\r\n"
                client_socket.sendall(response.encode())
            else:
                # Process the request
                requests.append(current_time)
                response = "HTTP/1.1 200 OK\r\n"
                response += "Content-Length: 13\r\n"
                response += "\r\n"
                response += "Hello, World!"
                client_socket.sendall(response.encode())

        client_socket.close()

# Example usage
limiter = RateLimiter(rate_limit=10, time_window=60)  # Allow 10 requests per minute

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8000)
server_socket.bind(server_address)
server_socket.listen(5)
print("Server started")

# Accept incoming client connections and spawn threads to handle requests
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    threading.Thread(target=limiter.handle_request, args=(client_socket,)).start()
