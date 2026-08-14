# import socket
# import sys

# def start_client(host='192.168.1.15', port=12345):
#     try:
#         client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#         print(f"Connecting to {host}:{port}")
#         client_socket.connect((host, port))

#         password = input("Enter password: ")

#         client_socket.send(password.encode())

#         response = client_socket.recv(1024).decode()
#         print("Server:", response)

#         client_socket.close()

#     except Exception as e:
#         print(e)
#         sys.exit()

# if __name__ == "__main__":
#     start_client()


import socket

SERVER_IP = "10.10.100.16"   # Change this to the server's IP
PORT = 12344

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((SERVER_IP, PORT))
    print("Connected to server.")

    message = input("Enter message: ")
    client.send(message.encode())

    reply = client.recv(1024).decode()
    print("Server replied:", reply)

except Exception as e:
    print("Error:", e)

finally:
    client.close()