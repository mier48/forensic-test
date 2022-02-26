import socket
print("Creación de socket...")
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket creado")
print("Conexión al host remoto")
s.connect(("www.latierrucarally.es", 80))
print("Conexión efectuada")
s.send('GET /index.html HTML/1.1\r\n\r\n'.encode())
# data=s.recv(2048)
# print(data)
while 1:
    data=s.recv(128)
    print(data)
    if data == "":
        break
s.close()
