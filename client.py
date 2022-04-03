import socket
from time import sleep
class Client:
    __client = None
    __host = None
    __port = None 
    __connected = False

    def __init__(self, host=None, port=None):
        self.__port = port
        self.__host = host
    
    def connect(self, host=None, port=None):
        try:
            if host and port:
                self.__host = host
                self.__port = port
            self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__client.connect((host or self.__host, port or self.__port))
            self.sendMessage(' ')
            self.__connected = True
            print('Connected succesfully')
            return self.__connected
        except:
            self.__connected = False
            print('server not found')
            return self.__connected
    
    def isConnected(self):
        return self.__connected
    
    def getPort(self):
        return self.__port
    
    def getHost(self):
        return self.__host

    def sendMessage(self, message):
        try:
            self.__client.sendall(str.encode(message))
            print(message,' [sent]')
        except: 
            self.__connected = False
            print('error sending message, make sure the server is running')

    def reconnect():
        try:
            self.__client.connect((host or self.__host, port or self.__port))
            self.__connected = True
            print('Connected succesfully')
        except:
            sleep(2)
            print('server not found, reconnecting...')
            self.reconnect()

    def closeConnection(self):
        if not self.__client:
            return
        self.__client.close()
        self.__connected = False