import socket

buf = 1024
direcc = ('direccion_ip_servido', 20000)

if __name__ == '__main__':
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        peticion = input('?: ').strip()
        if peticion == "":
            break
        mySocket.sendto(peticion.encode(), direcc)
        resp, adr = mySocket.recvfrom(buf)
        print("=> %s" % resp)
    mySocket.close()
    print("fin del cliente UDP")
