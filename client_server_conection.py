import socket

def main():
    # Obtener la dirección IP local
    host = socket.gethostbyname(socket.gethostname())
    print(f"Servidor activo en IP: {host}")
    port = 1235

    # Crear el socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)  # Escuchar una conexión a la vez
    print(f"Esperando conexiones en {host}:{port}...")

    try:
        # Aceptar una conexión
        client, address = s.accept()
        print(f"Conexión establecida desde {address}")
        print(f"Se ha efectuado una conexión desde {client.getpeername()}")

        # Comunicación con el cliente
        welcome_message = "Bienvenido al servidor. ¡Gracias por conectarte!\n"
        client.send(welcome_message.encode('utf-8'))

    except KeyboardInterrupt:
        print("\nServidor detenido manualmente.")
    except Exception as e:
        print(f"Error durante la ejecución del servidor: {e}")
    finally:
        # Cerrar el socket del cliente y del servidor
        client.close()
        s.close()
        print("Conexión cerrada. Servidor apagado.")

if __name__ == "__main__":
    main()
