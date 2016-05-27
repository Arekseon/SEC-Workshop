#!/usr/bin/python
#example:
#python3 TCT.py 10.0.1.18 5009 message
import sys
import socket

if (len(sys.argv) < 4):
	print("not enough information")
else:
	host = sys.argv[1]
	port = sys.argv[2]
	message = sys.argv[3]
	print ("host: " + host + "port: " + port)
	print ("send message: " + message)

	with socket.create_connection((host, port)) as my_socket:
		print('created socket', my_socket)
		print('sending command...')
		bytes = str.encode(message)
		my_socket.send(bytes)
		data = my_socket.recv(512)
		print(data)
		print("###")
		#my_socket.send(message)
