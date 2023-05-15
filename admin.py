import bcrypt, re, random, io, string
from tkcalendar import Calendar
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox, ttk, filedialog, Tk, Label, Entry, Button, END
import tkinter as tk
import mysql.connector
from mysql.connector import Error
from buttons import clockdate, ui_bg, log_out_btn
from ALL2_test1 import Loginpage



f=('Arial', 14)
f2=('Arial', 12)
bgc='#F9D3B9'

class AdminPage(tk.Frame):
    def __init__(self,parent=None, controller=None, name=None):
        global login_details
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.name=name
        self.parent=parent

        #admin page background
        ui_bg(self, 'images\\Slide5.png')

        #admin page title
        self.admin_title=tk.Label(self, text='Admin Page', font=('Helvetica', 18, 'bold'), bg=bgc)
        self.admin_title.place(x=450, y=10)

        #show list of students from db

        #add/delete/view books

        #add/edit/delete quiz

        #chat discussions

        #add/delete/view course materials

        #view appointments


        #show admin date and clock
        clockdate(self)

        #admin view as normal user
        # def view_user():
        #     controller.show_frame(Homepage)
        # self.viewuser_btn=tk.Button(self,height=1, width=10, font=f, command=view_user, text='View as User')
        # self.viewuser_btn.place(x=945, y=135)

        # #Logout
        log_out_btn(self, Loginpage, controller)
        
        #     controller.show_frame(Loginpage)
        #     messagebox.showinfo('Logout Status', 'Logged out successfully!')
        # self.logout_btn=tk.Button(self, height=1, width=9, font=f, command=log_out, text='Logout')
        # self.logout_btn.place(x=950 ,y=180)

