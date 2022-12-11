#!/usr/bin/env python

import socket
import time

host = socket.gethostbyname(socket.gethostname())
port = 1234

print(f"Connecting to {host}:{port} ...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)
