import socket

# Configuración del servidor
host = socket.gethostbyname(socket.gethostname())  # Obtiene la dirección IP local
port = 1234  # Puerto del servidor
bufsize = 1024  # Tamaño del buffer para recibir datos

# Crear el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permitir reutilización del puerto
s.bind((host, port))  # Vincular el socket
s.listen(5)  # Escuchar conexiones entrantes (máximo 5 en la cola)

print(f"Servidor activo en {host}:{port}")

try:
    while True:
        print("Esperando conexión...")
        client_socket, client_address = s.accept()  # Aceptar una conexión
        print(f"Conexión establecida con {client_address}")

        # Enviar un mensaje al cliente
        welcome_message = "Bienvenido al servidor. Escribe algo y recibirás una respuesta.\n"
        client_socket.send(welcome_message.encode('utf-8'))

        # Manejar datos recibidos
        while True:
            data = client_socket.recv(bufsize)  # Recibir datos del cliente
            if not data:  # Si no hay datos, el cliente cerró la conexión
                print(f"Conexión cerrada por {client_address}")
                break
            print(f"Mensaje recibido de {client_address}: {data.decode('utf-8')}")
            response = f"Servidor recibió: {data.decode('utf-8')}\n"
            client_socket.send(response.encode('utf-8'))  # Enviar respuesta al cliente

        client_socket.close()  # Cerrar el socket del cliente

except KeyboardInterrupt:
    print("\nServidor detenido manualmente.")
finally:
    s.close()  # Cerrar el socket del servidor
    print("Socket del servidor cerrado.")
