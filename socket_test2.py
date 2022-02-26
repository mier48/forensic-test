#!/usr/bin/env python
#--*--coding:UTF-8 --*--

import socket
import sys

host=sys.argv[1]
textport=sys.argv[2]
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port=int(textport)
except ValueError:
    port=socket.getservbyname(textport,'udp')
s.connect((host, port))
print("Introduzca los datos a transmitir")
data=sys.stdin.readline().strip()
s.sendall(data.encode())
print("Esperando respuesta, Ctrl-c para detener")
while 1:
    buf=s.recv(2048)
    if not len(buf):
        break
    print(buf)
