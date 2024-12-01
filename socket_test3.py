import socket
import sys
from math import *

BUF_SIZE = 1024
ADDRESS = ('', 20000)

# Crear el socket del servidor
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server.bind(ADDRESS)
print("Servidor UDP activo en el puerto 20000")

# Función segura para evaluar expresiones matemáticas
def safe_eval(expression):
    try:
        # Validar que la expresión solo contenga caracteres permitidos
        allowed_chars = "0123456789+-*/().eE "  # Permite números, operadores, paréntesis y notación científica
        if not all(char in allowed_chars for char in expression):
            return "Expresión no permitida"

        # Evaluar la expresión
        result = eval(expression, {"__builtins__": None}, {"sqrt": sqrt, "pow": pow, "sin": sin, "cos": cos, "tan": tan, "log": log, "pi": pi, "e": e})
        return str(result)
    except Exception as e:
        return f"Error: {e}"

# Bucle principal del servidor
try:
    while True:
        request, client_address = socket_server.recvfrom(BUF_SIZE)
        expression = request.decode('utf-8').strip()  # Decodificar los datos recibidos
        print(f"Expresión recibida de {client_address}: {expression}")

        # Evaluar la expresión de forma segura
        response = safe_eval(expression)
        print(f"Enviando respuesta: {response}")

        # Enviar la respuesta al cliente
        socket_server.sendto(response.encode('utf-8'), client_address)
except KeyboardInterrupt:
    print("\nServidor detenido.")
finally:
    socket_server.close()
    print("Socket cerrado.")
