import socket

class Server:
    __server = None
    __host = None
    __port = None
    __connected = False

    def __init__(self, host=None, port=None):
        self.__port = port
        self.__host = host

    def start(self, host=None, port=None):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((host or self.__host, port or self.__port))
        self.__server.listen()
        self.__connected = True
        print("Server started and running")
        conn, addr = self.__server.accept()
        print(f"Connected by {addr}")
        with conn:
            while True:
                msg = conn.recv(1024)
                if(msg):
                    print(f"address {addr} sent: {msg.decode()}")


    def stop(self):
        print('closing')
        if not self.__server or not self.__connected:
            return
        self.__server.close()
        self.__connected = False

