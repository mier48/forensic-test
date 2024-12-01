import socket

def fin(sock):
    """Función para recibir y mostrar datos del servidor."""
    try:
        data = sock.recv(1024)
        if not data:
            print("Conexión cerrada por el servidor.")
            return False
        print(data.decode('utf-8', errors='replace'))
        return True
    except socket.error as e:
        print(f"Error al recibir datos: {e}")
        return False

def main():
    host = "ftp.ibiblio.org"
    port = 21

    try:
        # Crear y conectar el socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print(f"Conectado a {host}:{port}")

        # Recibir mensaje de bienvenida
        if not fin(s):
            return

        # Enviar comandos FTP
        commands = [
            "USER anonymous\r\n",
            "PASS pepe@casa.es\r\n",
            "HELP\r\n",
            "QUIT\r\n"
        ]

        for cmd in commands:
            print(f"Enviando comando: {cmd.strip()}")
            s.send(cmd.encode('utf-8'))
            if not fin(s):
                break

    except socket.error as e:
        print(f"Error de socket: {e}")
    except Exception as e:
        print(f"Error general: {e}")
    finally:
        # Cerrar el socket
        s.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    main()
