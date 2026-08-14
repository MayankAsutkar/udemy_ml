import socket
import sys

def start_server(host='0.0.0.0', port=12345):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind((host, port))
        print(f"Server started on {host}:{port}")

        server_socket.listen(5)
        print("Waiting for clients...")

        while True:
            up = low = num = sym = 0      # Reset for every client

            client_socket, client_address = server_socket.accept()
            print(f"Connected by {client_address}")

            data = client_socket.recv(1024).decode()

            print("Password received:", data)

            for ch in data:
                if ch.isupper():
                    up += 1
                elif ch.islower():
                    low += 1
                elif ch.isdigit():
                    num += 1
                else:
                    sym += 1

            if up and low and num and sym:
                client_socket.send("Strong Password".encode())
            else:
                client_socket.send("Weak Password".encode())

            client_socket.close()

    except Exception as e:
        print(e)
        sys.exit()

if __name__ == "__main__":
    start_server()