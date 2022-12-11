#!/usr/bin/env python


import socket
import time

host = socket.gethostbyname(socket.gethostname())
print(host)
port = 1235

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

client, address = s.accept()
print(address)
print(f"Se ha efectuado una conexión desde {client.getpeername()}")
client.close()
s.close()
