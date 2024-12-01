# Forensic Test

Este repositorio contiene ejemplos y scripts relacionados con análisis forense, comunicación mediante sockets y pruebas básicas de clientes y servidores. Los ejemplos están diseñados con fines educativos y para aprendizaje.

---

## Contenido del Repositorio

### 1. Servidor TCP Básico
Un servidor TCP que escucha en un puerto específico, acepta una conexión y muestra información básica sobre el cliente.

```
import socket

host = socket.gethostbyname(socket.gethostname())
port = 1235

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

client, address = s.accept()
print(address)
print(f"Se ha efectuado una conexión desde {client.getpeername()}")
client.close()
s.close()
```

---

### 2. Cliente TCP para Solicitudes HTTP
Un cliente TCP que envía solicitudes HTTP a un servidor web y muestra la respuesta.

```
import socket

host = "www.example.com"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

request = "GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
s.sendall(request.encode())

response = s.recv(4096)
print(response.decode())

s.close()
```

---

### 3. Servidor UDP
Un servidor UDP que recibe mensajes, los evalúa (de forma segura) y envía una respuesta al cliente.

```
import socket
from math import *

host = "127.0.0.1"
port = 20000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
print("Servidor UDP activo en el puerto 20000")

while True:
    data, addr = s.recvfrom(1024)
    print(f"Mensaje recibido de {addr}: {data.decode('utf-8')}")
    try:
        result = eval(data.decode('utf-8'), {"__builtins__": None}, {"sqrt": sqrt, "pow": pow})
        s.sendto(str(result).encode(), addr)
    except Exception as e:
        s.sendto(f"Error: {e}".encode(), addr)
```

---

### 4. Cliente UDP
Un cliente UDP que envía mensajes al servidor y recibe respuestas.

```
import socket

host = "127.0.0.1"
port = 20000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Introduce un mensaje (o 'salir' para terminar): ")
    if message.lower() == "salir":
        break
    s.sendto(message.encode(), (host, port))
    response, addr = s.recvfrom(1024)
    print(f"Respuesta del servidor: {response.decode('utf-8')}")

s.close()
```

---

### 5. Cliente FTP Básico
Un cliente FTP básico que se conecta a un servidor, envía comandos y cierra la conexión.

```
import socket

host = "ftp.example.com"
port = 21

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print(s.recv(1024).decode('utf-8'))

s.send("USER anonymous\r\n".encode())
print(s.recv(1024).decode('utf-8'))

s.send("PASS guest@\r\n".encode())
print(s.recv(1024).decode('utf-8'))

s.send("QUIT\r\n".encode())
s.close()
```

---

## Cómo Usar

1. Clona este repositorio:
```
git clone https://github.com/mier48/forensic-test.git
```
2. Accede al directorio:
```
cd forensic-test
```
3. Ejecuta los scripts según las instrucciones.

---

## Requisitos

- Python 3.x
- Acceso a red para pruebas de cliente/servidor.
- Permisos para abrir puertos en tu máquina.

---

## Contribuciones

Si tienes sugerencias o quieres contribuir, por favor abre un _pull request_ o crea un _issue_.

---