import tkinter as tk
import tkinter.messagebox
from client import Client

socketClient = Client()
window = tk.Tk()
window.title("Client app")
window.geometry("250x500")
userAlert = tk.StringVar()

# send message from gui, only message if is not connected 
def message():
    if not socketClient.isConnected():
        tk.messagebox.showinfo(title="connection error", message="Make sure that you are connected to a server to send a message!")
        return
    socketClient.sendMessage(messageInput.get())
    messageInput.delete(0, 'end')

# connect from gui, will connect and set top message to be "Connected"
def connect(host, port):
    connection = socketClient.connect(host,port)
    if not connection:
        tk.messagebox.showinfo(title="connection error", message="Make sure that your server is running to connect!")
        return
    userAlert.set("Connected")
    tk.messagebox.showinfo(title="connected", message="connected to the server!")

# disconnect from gui, if is connected will disconnect the current connection
def disconnect():
    if socketClient.isConnected():
        socketClient.closeConnection()
    userAlert.set("Disconnected")

# Top text to display the status of the app: Disconnected|Connected
connectionText = tk.Message(window, pady=20, width=180, textvariable=userAlert)
userAlert.set("Disconnected")
connectionText.pack()

# hos input with label
tk.Label(window, text="enter server host").pack()
hostInput = tk.Entry(window)
hostInput.pack()

# port input with label
tk.Label(window, text="enter server port").pack()
portInput = tk.Entry(window)
portInput.pack(pady=5)

# button to connect to the server
tk.Button(window, text="connect to server", command= lambda: connect(hostInput.get(), int(portInput.get()))).pack(pady=5)

# message input with a label
tk.Label(window, text="write message to server").pack()
messageInput = tk.Entry(window)
messageInput.pack(pady=5)

# send message button
tk.Button(window, text="send message", command= lambda: message()).pack(pady=5)

# disconnect button
tk.Button(window, text="Disconnect", command= lambda: disconnect()).pack(pady=10)

window.mainloop()