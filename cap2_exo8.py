#!/usr/bin/env python


import socket
import time


def main():
    host = socket.gethostbyname(socket.gethostname())
    port = 6969

    print("Connecting to {}:{} ...".format(host, port))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        s.bind((host, port))
        s.listen(1)

        client, address = s.accept()

        print("Connection start from: {}".format(client.getpeername()))

        client.close()
        s.close()
    except Exception as E:
        print("Exception: {} ".format(E))
        s.close()


if __name__ == '__main__':
    main()
