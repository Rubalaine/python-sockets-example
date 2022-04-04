from http import client
import tkinter as tk
import tkinter.messagebox
import threading
from server import Server

socketServer = Server()

window = tk.Tk()
window.title('Server app')
window.geometry('250x250')
userAlert = tk.StringVar()
messageContainer = tk.StringVar()

def listenMessage():
    while True:
        msg = socketServer.getMessage()
        if msg:
            print(msg)
            messageContainer.set(msg)
            socketServer.clearMessage()

def start(host, port):
    if socketServer.isRunning():
        tk.messagebox.showerror(title="connection error", message="Server is actualy running!")
        return

    _messageListener = threading.Thread(target=listenMessage, daemon=True)
    _messageListener.start()

    _server = threading.Thread(target=socketServer.start, args=(host,port), daemon=True)
    _server.start()

    if socketServer.isRunning():
        userAlert.set("Server up and running")

    

# Top text to display the status of the app: Disconnected|Connected
connectionText = tk.Message(window, pady=20, width=180, textvariable=userAlert)
userAlert.set("Disconnected")
connectionText.pack() 

# host input with label
tk.Label(window, text="enter server host").pack()
hostInput = tk.Entry(window)
hostInput.pack()

# port input with label
tk.Label(window, text="enter server port").pack()
portInput = tk.Entry(window)
portInput.pack(pady=5)

# button to connect to the server
tk.Button(window, text="start server", command= lambda: start(hostInput.get(), int(portInput.get()))).pack(pady=5)

messageContext = tk.Message(window, pady=20, width=180, textvariable=messageContainer)
messageContainer.set(" ")
messageContext.pack()
window.mainloop()