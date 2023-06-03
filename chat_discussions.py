import tkinter as tk
from tkinter import SOLID, W, WORD, Y, Button, Frame, Text, ttk
from tkinter import scrolledtext
from socket import *
from threading import *
from tkinter import simpledialog


bgc='antique white'
f=('Arial', 12)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        #host, port
        host='192.168.0.142'
        port=5000
        address=(host, port)

        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(address)

        # self.interface_done = False
        self.running=True

        self.name = simpledialog.askstring("Name", "Please enter your name", parent=self)
        self.client_socket.send(self.name.encode('utf-8'))

        # interface_thread= Thread(target=self.interface)
        receive_thread = Thread(target=self.receive_msg)
        
        # interface_thread.start()
        receive_thread.start()
        

        # Discussions server treeview scroll
        self.discussions_frame = tk.Frame(self, width=300, height=500, bg=bgc)
        self.discussions_frame.place(x=125, y=100)

        self.discussions_txt = tk.Label(self.discussions_frame, text='Discussions', font=('Arial', 29), bg=bgc)
        self.discussions_txt.grid(row=0, column=0, pady=10)

        self.discussions_tv_frame = tk.Frame(self.discussions_frame, bg=bgc)
        self.discussions_tv_frame.grid(row=1, column=0)

        self.discussions_tv_scroll = tk.Scrollbar(self.discussions_tv_frame)
        self.discussions_tv_scroll.pack(side=tk.RIGHT, fill=Y)

        self.discussions_tv = ttk.Treeview(self.discussions_tv_frame, yscrollcommand=self.discussions_tv_scroll.set, height=15)
        self.discussions_tv.pack()

        self.discussions_tv_scroll.config(command=self.discussions_tv.yview)

        self.discussions_tv.column('#0', width=435, minwidth=435)
        self.discussions_tv.heading('#0', text='Discussion Servers', anchor=W)

        # Insert server names
        self.discussions_tv.insert(parent='', index='end', iid=0, text='Computer Architecture & Networks')

        
        # Chat msg input entry
        self.chat_entry_frame = tk.Frame(self, width=675, height=50, bg=bgc)
        self.chat_entry_frame.place(x=641, y=600)

        self.chat_entry = Text(self.chat_entry_frame, height=5, width=52, font=f, wrap=WORD, relief=SOLID, bd=2)
        self.chat_entry.grid(row=0, column=0, padx=10, pady=5)

        # Send btn
        self.send_btn = Button(self.chat_entry_frame, text='Send', font=f, relief=SOLID, bd=2, cursor='hand2', command=self.send_msg)
        self.send_btn.grid(row=0, column=1, padx=10, pady=5)

        #show users list
        self.users_frame = tk.Frame(self, width=300, height=500, bg=bgc)
        self.users_frame.place(x=125, y=450)

        self.users_txt = tk.Label(self.users_frame, text='Users', font=('Arial', 29), bg=bgc)
        self.users_txt.grid(row=0, column=0, pady=10)

        self.users_tv_frame = tk.Frame(self.users_frame, bg=bgc)
        self.users_tv_frame.grid(row=1, column=0)

        self.users_tv_scroll = tk.Scrollbar(self.users_tv_frame)
        self.users_tv_scroll.pack(side=tk.RIGHT, fill=Y)

        self.users_tv = ttk.Treeview(self.users_tv_frame, yscrollcommand=self.users_tv_scroll.set, height=15)
        self.users_tv.pack()

        self.users_tv_scroll.config(command=self.users_tv.yview)
        
        self.users_tv.column('#0', width=435, minwidth=435)

        

        self.interface_done = True


    def send_msg(self):
            message = f"{self.name}: {self.chat_entry.get('1.0', 'end-1c')}"
            self.chat_entry.delete('1.0', 'end')
            self.client_socket.send(bytes(message,('utf-8')))

            # Get the message from the entry field
            # Implement the logic to send the message to the server or other clients
            # You can use a WebSocket connection or any other communication mechanism

    def receive_msg(self):
            self.chat_scrolledtxt = scrolledtext.ScrolledText(self, width=58, height=21, bg='white', relief=SOLID, bd=2, font=f, wrap=WORD)
            self.chat_scrolledtxt.place(x=650, y=115)
            while self.running:
                try:
                    # Display the received message in the chat message area
                    message = self.client_socket.recv(1024).decode('utf-8')
                    self.chat_scrolledtxt.config(state='normal')
                    self.chat_scrolledtxt.insert(tk.END, message + '\n')
                    self.chat_scrolledtxt.config(state='disabled')
                    self.chat_scrolledtxt.see(tk.END)  # Scroll to the end of the text area
                except OSError:
                    break
            # # Insert user names
            # names=self.client_socket.recv(1024).decode('utf-8')
            # for n in names:
            #     self.users_tv.insert(parent='', index='end', iid=0, text=n) 
    



    

app = App()
app.geometry('1280x720+80+5')
app.title('Chat Discussions')
app.resizable(False, False)
app.mainloop()
