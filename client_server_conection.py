#!/usr/bin/env python


import socket
import time

host = socket.gethostbyname(socket.gethostname())
print(host)
port = 1234

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

client, direction = s.accept()
print(direction)
print("Se ha efectuado una conexión desde ")
print(client.getpeername())
client.close()
s.close()
