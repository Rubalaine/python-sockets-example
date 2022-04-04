from client import Client

socketClient = Client('127.0.0.1', 4000)
socketClient.connect()
while True:
    message = input("Envie uma mensagem ao servidor: ")
    if message == "close":
        socketClient.sendMessage(message)
        socketClient.closeConnection()
        break
    socketClient.sendMessage(message)
