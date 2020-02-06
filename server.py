import socket
import time
import sys

class Server:
    __yes = 'DY'
    __no = 'DN'

    def __init__(self):
        self.__ip = ""
        self.__port = -1

    def __init__ (self,ip,port):
        self.__ip = ip
        self.__port = port

    def __del__(self):
        self.__server.close()
        print("server end")

    def getIP(self):
        return self.__ip
    def getPORT(self):
        return self.__port
    def getServerData(self):
        print("ip : %s" %self.getIP())
        print("port : %s" %self.getPORT())

    def serverInit(self,MAX):
        print("Start server")
        self.__server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.getServerData()
        self.__host_addr = (self.getIP(),self.getPORT())
        self.__server.bind((self.getIP(),self.getPORT()))
        self.__server.listen(MAX)

    def serverStart(self):
        self.__client,self.__host_addr=self.__server.accept()
        print("Connection acceptd from %s"%self.__host_addr[0])
        while True:
            self.__client.send(self.__yes.encode('utf-8'))
            time.sleep(1)
            self.__client.send(self.__no.encode('utf-8'))
            time.sleep(1)

ip = socket.gethostname()

server = Server(ip,55555)
server.serverInit(5)
server.serverStart()
