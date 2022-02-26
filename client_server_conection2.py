#!/usr/bin/env python
#--*--coding:UTF-8 --*--

import socket

host = ''
port = 1338

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
client, direction = s.accept()
print(direction)
print(client.getpeername())
client.send("HHola Ediciones ENI\n introduzca una palabra o fin si desea terminar la conversación".encode())
while 1:
    data=client.recv(1024)
    if data == "fin\n":
        break
    print("Cliente > " + data)
    palabra=input("Servidor > ")
    client.send(palabra.encode())
client.close()
s.close()
