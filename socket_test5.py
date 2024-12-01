import socket
import sys

def main():
    if len(sys.argv) != 4:
        print("Uso: python cliente_tcp.py <host> <puerto> <archivo>")
        sys.exit(1)

    host = sys.argv[1]
    textport = sys.argv[2]
    archivo = sys.argv[3]

    # Crear el socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f"Error en la creación del socket: {e}")
        sys.exit(1)

    # Validar el puerto
    try:
        port = int(textport)
    except ValueError:
        print(f"El puerto '{textport}' no es válido.")
        sys.exit(1)

    # Conectar al servidor
    try:
        s.connect((host, port))
        print(f"Conectado a {host}:{port}")
    except socket.gaierror as e:
        print(f"Error de dirección de conexión al servidor: {e}")
        sys.exit(1)
    except socket.error as e:
        print(f"Error de conexión: {e}")
        sys.exit(1)

    # Enviar solicitud HTTP
    try:
        data = f"GET {archivo} HTTP/1.0\r\nHost: {host}\r\n\r\n"
        s.sendall(data.encode())
        print(f"Solicitud enviada: {data.strip()}")
    except socket.error as e:
        print(f"Error de envío de datos: {e}")
        sys.exit(1)

    # Recibir datos del servidor
    try:
        while True:
            buf = s.recv(2048)
            if not buf:
                break
            print(buf.decode('utf-8', errors='replace'))
    except socket.error as e:
        print(f"Error de recepción de datos: {e}")
    except KeyboardInterrupt:
        print("\nCliente interrumpido por el usuario.")
    finally:
        # Cerrar el socket
        s.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    main()
