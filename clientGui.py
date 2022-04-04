import tkinter as tk
import tkinter.messagebox
from client import Client

socketClient = Client()
window = tk.Tk()
window.title("Client app")
window.geometry("250x500")
userAlert = tk.StringVar()
def message():
    if not socketClient.isConnected():
        tk.messagebox.showinfo(title="connection error", message="Make sure that you are connected to a server to send a message!")
        return
    socketClient.sendMessage(messageInput.get())
    messageInput.delete(0, 'end')

def connect(host, port):
    connection = socketClient.connect(host,port)
    if not connection:
        tk.messagebox.showinfo(title="connection error", message="Make sure that your server is running to connect!")
        return
    userAlert.set("Connected")
    tk.messagebox.showinfo(title="connected", message="connected to the server!")

def disconnect():
    if socketClient.isConnected():
        socketClient.closeConnection()
    userAlert.set("Disconnected")
# def connect(host, port):
#     socketClient.connect(host, port)
#     while socketClient.isConnected():
#         message = input("write a command: ")
#         if message == "close":
#             server.close()

connectionText = tk.Message(window, pady=20, width=180, textvariable=userAlert)
userAlert.set("Disconnected")
connectionText.pack()

tk.Label(window, text="enter server host").pack()
hostInput = tk.Entry(window)
hostInput.pack()
tk.Label(window, text="enter server port").pack()
portInput = tk.Entry(window)
portInput.pack(pady=5)
tk.Button(window, text="connect to server", command= lambda: connect(hostInput.get(), int(portInput.get()))).pack(pady=5)
tk.Label(window, text="write message to server").pack()
messageInput = tk.Entry(window)
messageInput.pack(pady=5)

tk.Button(window, text="send message", command= lambda: message()).pack(pady=5)
tk.Button(window, text="Disconnect", command= lambda: disconnect()).pack(pady=10)

# greeting = tk.Label(window, text="Hello, Tkinter", fg="white", bg="blue")
# server = None
# def closeApp():
#     window.destroy()
# closeButton =  tk.Button(window, text="Close application", command=closeApp).grid(row=5, column=1)

# tk.Label(window,text="Server address:").grid(row=0)
# tk.Label(window,text="Server port:").grid(row=1)

# addressInput = tk.Entry(window)
# portInput = tk.Entry(window)

# addressInput.grid(row=0, column=1)
# portInput.grid(row=1, column=1)

# def createMessageInput():
#     tk.Label(window, text="message:").grid(row=6)
#     msg
# def startServer():
#     address = addressInput.get()
#     port = int(portInput.get())
#     if(not address and not port):
#         return tk.messagebox.showinfo(title="Invalid", message="Please provide the address and the port!")
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         server = s
#         server.connect((address, port))
#         while True:
#             message = input("Envie uma mensagem ao servidor: ")
#             if message == "close":
#                 server.close()
#                 window.destroy()
#             server.sendall(str.encode(message))


# button = tk.Button(
#         window,
#         text="Conect to server",
#         command=startServer
#     ).grid(row=4, column=1)



# # greeting.pack()
# # button.pack()
# # closeButton.pack()
    


window.mainloop()