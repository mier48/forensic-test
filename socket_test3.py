import socket
import sys
from math import *

buf = 1024
direcc = ('', 20000)

socketserver=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketserver.bind(direcc)
print("Servidor activo")

#bucle de servicio del Servidor
while True:
    peticion, direccclient = socketserver.recvfrom(buf)
    peticion=peticion.strip()
    try:
        resp = "%s" % eval(peticion)
    except:
        resp = "%s" % sys.exec_info()[1]
    socketserver.sendto("%s" % resp, direccclient)
#socketserver.close()
