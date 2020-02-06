import socket
import time
import sys

SERVER_IP = socket.gethostname()
SERVER_PORT = 55555

print("Starting socket: TCP...")
server_addr = (SERVER_IP, SERVER_PORT)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connecting to server @ %s:%d..." %(SERVER_IP, SERVER_PORT))
socket_tcp.connect(server_addr)

while True:
    data = socket_tcp.recv(512)
    data = data.decode('utf-8')
    if 'DN' == data:
        print("Close: %s" % data)
    elif 'DY' == data:    
        print("Open: %s" % data)
    elif '' == data:
        print("server disconnect")
        break
    else:
        print(data)
socket_tcp.close()
