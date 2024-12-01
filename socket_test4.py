import socket

# Configuración del cliente
BUF_SIZE = 1024
SERVER_ADDRESS = ('127.0.0.1', 20000)  # Cambia '127.0.0.1' por la IP real del servidor

def udp_client():
    # Crear el socket UDP
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        while True:
            # Leer entrada del usuario
            peticion = input('¿Qué desea enviar al servidor? (dejar vacío para salir): ').strip()
            if not peticion:
                print("Saliendo del cliente UDP...")
                break

            # Enviar la solicitud al servidor
            my_socket.sendto(peticion.encode('utf-8'), SERVER_ADDRESS)

            # Recibir la respuesta del servidor
            try:
                resp, adr = my_socket.recvfrom(BUF_SIZE)
                print(f"=> Respuesta del servidor {adr}: {resp.decode('utf-8', errors='replace')}")
            except socket.timeout:
                print("No se recibió respuesta del servidor.")
    except KeyboardInterrupt:
        print("\nCliente detenido manualmente.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Cerrar el socket
        my_socket.close()
        print("Socket cerrado. Fin del cliente UDP.")

if __name__ == "__main__":
    udp_client()
