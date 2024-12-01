import socket

def main():
    host = ''  # Escucha en todas las interfaces de red disponibles
    port = 1338

    # Crear el socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"Servidor activo en el puerto {port}, esperando conexiones...")

    # Aceptar una conexión
    client, address = s.accept()
    print(f"Conexión establecida con {address}")
    print(f"Cliente conectado desde: {client.getpeername()}")

    # Enviar mensaje de bienvenida
    welcome_message = (
        "Hola Ediciones ENI\n"
        "Introduzca una palabra o 'fin' si desea terminar la conversación.\n"
    )
    client.send(welcome_message.encode('utf-8'))

    try:
        while True:
            # Recibir datos del cliente
            data = client.recv(1024)
            if not data:  # Si no hay datos, el cliente cerró la conexión
                print("El cliente cerró la conexión.")
                break

            message = data.decode('utf-8').strip()  # Decodificar y eliminar saltos de línea
            if message.lower() == "fin":
                print("El cliente finalizó la conversación.")
                break

            print(f"Cliente > {message}")

            # Enviar respuesta al cliente
            response = input("Servidor > ")
            client.send(response.encode('utf-8'))

    except Exception as e:
        print(f"Error durante la comunicación: {e}")
    finally:
        # Cerrar sockets
        client.close()
        s.close()
        print("Servidor cerrado.")

if __name__ == "__main__":
    main()
