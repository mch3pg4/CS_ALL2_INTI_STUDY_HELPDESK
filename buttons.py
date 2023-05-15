import bcrypt, re, random, io, string
import datetime
from tkcalendar import Calendar
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox, ttk, filedialog, Tk, Label, Entry, Button, END
import tkinter as tk
from time import strftime
from datetime import date
from tktooltip import ToolTip


f=('Arial', 14)
f2=('Arial', 12)
bgc='#F9D3B9'

#clock and date
def clockdate(self):
    
    def my_time():
        time_string = strftime('%H:%M:%S %p %a %d/%m/%Y') # time format 
        l1.config(text=time_string)
        l1.after(1000,my_time) # time delay of 1000 milliseconds 

    
    l1=tk.Label(self,font=('Arial', 19, 'bold'),bg=bgc, foreground='black')
    l1.place(x=750, y=12)
    my_time()

#ui background with inti logo
def ui_bg(self, image_file):
    self.raw_image=Image.open(image_file)
    self.img=self.raw_image.resize((1240,773),Image.LANCZOS)
    self.background_image=ImageTk.PhotoImage(self.raw_image)
    self.background_label = tk.Label(self, image=self.background_image)
    self.background_label.place(x=-5,y=-5)
    self.background_label.image = self.background_image

#toggle show/hide password function
def toggle_password(pwd_tf, pwd_btn):
    if pwd_tf.cget('show') == '':
        pwd_tf.config(show='*')
        pwd_btn.config(text='Show',cursor= "hand2")
    else:
        pwd_tf.config(show='')
        pwd_btn.config(text='Hide',cursor= "hand2")


#logout button 
def log_out_btn(self, frame, controller):
    def logout():
        controller.show_frame(frame)
        messagebox.showinfo('Logout Status', 'Logged out successfully!')

    image8=Image.open('images\\logout.png')
    img8=image8.resize((50,50))
    my_img8=ImageTk.PhotoImage(img8)
    logout_icon=Label(image=my_img8)
    logout_icon.image=my_img8

    logout_btn=tk.Button(self, image=my_img8,cursor='hand2', command=logout)
    logout_btn.place(x=1300,y=5)
    ToolTip(logout_btn, msg='Logout')