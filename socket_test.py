import socket

def main():
    try:
        print("Creación de socket...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket creado")

        # Conexión al servidor remoto
        print("Conexión al host remoto")
        s.connect(("www.latierrucarally.es", 80))
        print("Conexión efectuada")

        # Enviar solicitud HTTP
        request = 'GET /index.html HTTP/1.1\r\nHost: www.latierrucarally.es\r\nConnection: close\r\n\r\n'
        s.send(request.encode())
        print("Solicitud enviada")

        # Recibir respuesta
        while True:
            data = s.recv(128)
            if not data:  # El servidor cierra la conexión
                break
            print(data.decode('utf-8', errors='replace'))  # Decodificar con manejo de errores

        s.close()
        print("Conexión cerrada")
    except socket.error as e:
        print(f"Error de socket: {e}")
    except Exception as e:
        print(f"Error general: {e}")

if __name__ == "__main__":
    main()
