import tkinter as tk
import websocket

class App:
    def __init__(self, master):
        self.master = master
        self.websocket = websocket.WebSocketApp("ws://localhost:8000",
                                                 on_message=self.on_message,
                                                 on_error=self.on_error,
                                                 on_close=self.on_close)
        self.websocket.on_open = self.on_open

        self.label = tk.Label(self.master, text="WebSocket client")
        self.label.pack()

        self.message_label = tk.Label(self.master, text="")
        self.message_label.pack()

        self.button = tk.Button(self.master, text="Send message", command=self.send_message)
        self.button.pack()

    def on_message(self, message):
        self.message_label.config(text=message)

    def on_error(self, error):
        print(error)

    def on_close(self):
        print("WebSocket closed")

    def on_open(self):
        self.websocket.send("Hello, server!")

    def send_message(self):
        self.websocket.send("Message from client")

root = tk.Tk()
app = App(root)
root.mainloop()
