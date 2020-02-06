import socket
import time
import sys

class Server:
    __yes = 'DY'
    __no = 'DN'

    def __init__(self):
        self.ip = ""
        self.port = -1

    def __init__ (self,ip,port):
        self.ip = ip
        self.port = port

    def __del__(self):
        self.server.close()
        print("server end")

    def getIP(self):
        return self.ip
    def getPORT(self):
        return self.port
    def getServerData(self):
        print("ip : %s" %self.getIP())
        print("port : %s" %self.getPORT())

    def serverInit(self,MAX):
        print("Start socket")
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.getServerData()
        self.host_addr = (self.getIP(),self.getPORT())
        self.server.bind((self.getIP(),self.getPORT()))
        self.server.listen(MAX)

    def serverStart(self):
        self.client,self.host_addr=self.server.accept()
        print("Connection acceptd tfrom %s"%self.host_addr[0])
        while True:
            self.client.send(self.__yes.encode('utf-8'))
            time.sleep(1)
            self.client.send(self.__no.encode('utf-8'))
            time.sleep(1)


server = Server(socket.gethostname(),55555)
server.serverInit(5)
server.serverStart()
