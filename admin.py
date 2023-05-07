import bcrypt, re, random, io, string
import datetime
from tkcalendar import Calendar
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox, ttk, filedialog, Tk, Label, Entry, Button, END
import tkinter as tk
from time import strftime
from datetime import date
import mysql.connector
from mysql.connector import Error
from captcha.image import ImageCaptcha

class Adminpage(tk.Frame):
    def __init__(self,parent, controller):
        global login_details
        tk.Frame.__init__(self,parent,bg='AntiqueWhite1')
    
        #inti logo
        # inti_logo(self)

        #show admin date and clock
        # adminclock(self)

        #admin view as normal user
        # def view_user():
        #     controller.show_frame(Homepage)
        # self.viewuser_btn=tk.Button(self,height=1, width=10, font=f, command=view_user, text='View as User')
        # self.viewuser_btn.place(x=945, y=135)

        # #Logout
        # def log_out():
        #     controller.show_frame(Loginpage)
        #     messagebox.showinfo('Logout Status', 'Logged out successfully!')
        # self.logout_btn=tk.Button(self, height=1, width=9, font=f, command=log_out, text='Logout')
        # self.logout_btn.place(x=950 ,y=180)