import socket
import sys

def main():
    if len(sys.argv) != 3:
        print("Uso: python cliente_udp.py <host> <puerto>")
        sys.exit(1)

    host = sys.argv[1]
    textport = sys.argv[2]

    # Crear un socket UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Verificar y convertir el puerto
        try:
            port = int(textport)
        except ValueError:
            port = socket.getservbyname(textport, 'udp')

        # Conectar al servidor
        s.connect((host, port))
        print(f"Conectado a {host}:{port}")

        # Enviar datos
        print("Introduzca los datos a transmitir:")
        data = sys.stdin.readline().strip()
        if not data:
            print("No se ingresaron datos. Terminando.")
            s.close()
            sys.exit(1)

        s.sendall(data.encode())
        print("Datos enviados. Esperando respuesta (Ctrl-C para detener).")

        # Recibir respuesta
        while True:
            buf = s.recv(2048)
            if not buf:
                print("Conexión cerrada por el servidor.")
                break
            print("Respuesta recibida:", buf.decode('utf-8', errors='replace'))

    except socket.error as e:
        print(f"Error de socket: {e}")
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario.")
    finally:
        print("Cerrando socket.")
        s.close()

if __name__ == "__main__":
    main()
