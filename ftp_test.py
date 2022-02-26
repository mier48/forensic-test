#!/usr/bin/env python
#--*--coding:UTF-8 --*--

import socket

host="ftp.ibiblio.org"
port=21
def fin():
    data = s.recv(1024)
    print(data)
    if data == "":
        pass

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
fin()
s.send("USER anonymous\r\n".encode())
fin()
s.send("PASS pepe@casa.es\r\n".encode())
fin()
s.send("HELP\r\n".encode())
fin()
s.send("QUIT\r\n".encode())
s.close()
