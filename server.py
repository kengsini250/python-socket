import socket
import time
import sys

HOST_IP = socket.gethostname()
HOST_PORT = 55555
print("Start socket")

socket_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("TCP server listen @%s:%d!" %(HOST_IP,HOST_PORT))
host_addr = (HOST_IP,HOST_PORT)
socket_tcp.bind(("",HOST_PORT))
socket_tcp.listen(1)

yes = 'DY'
no = 'DN'

while True:
    client,host_addr=socket_tcp.accept()
    print("Connection acceptd tfrom %s"%host_addr[0])
    while True:
        client.send(yes.encode('utf-8'))
        time.sleep(1)
        client.send(no.encode('utf-8'))
        time.sleep(1)
socket_tcp.close()
print("server end")