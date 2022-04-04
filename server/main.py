import socketserver
from server import Server

socketserver = Server('127.0.0.1', 4000)
socketserver.start()
# socketserver.stop()