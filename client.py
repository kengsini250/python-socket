import socket
import time
import sys

class Client:
    def __init__(self):
        self.__ip = ""
        self.__port = -1
    def __init__ (self,ip,port):
        self.__ip = ip
        self.__port = port

    def __del__(self):
        self.__client.close()
        print("client end")

    def getIP(self):
        return self.__ip
    def getPORT(self):
        return self.__port

    def clientInit(self):
        print("Start client")
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__host_addr = (self.getIP(),self.getPORT())
        print("Connecting to server @ %s:%d..." %(self.getIP(), self.getPORT()))
        self.__client.connect(self.__host_addr)

    def clientStart(self):
        while True:
            self.__data = self.__client.recv(512)
            self.__data = self.__data.decode('utf-8')
            if 'DN' == self.__data:
                print("Close: %s" % self.__data)
            elif 'DY' == self.__data:    
                print("Open: %s" % self.__data)
            elif '' == self.__data:
                print("server disconnect")
                break
            else:
                print(self.__data)

ip = socket.gethostname()
client = Client(ip,55555)
client.clientInit()
client.clientStart()
