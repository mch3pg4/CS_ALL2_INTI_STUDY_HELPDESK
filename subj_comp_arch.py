import bcrypt, re, random, io, string
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox, ttk, filedialog, Tk, Label, Entry, Button, END
import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from mysql.connector import Error
from ALL2_test1 import ui_bg, top_buttons, App


f=('Arial', 14)
f2=('Arial', 12)
bgc='#F9D3B9'

class Subject1(tk.Frame):
    def __init__(self, bg=bgc):
        ui_bg(self)
        top_buttons(self)

        self.courses_lbl = Label(self, text ='Recent Courses', font = ('Arial', 28), bg=bgc)
        self.courses_lbl.pack()
        self.courses_lbl.place(x=380, y=100)

        #courses frame
        self.courses_frame = Frame(self, bg=bgc,relief=SOLID)
        self.courses_frame.place(x=99, y=155)


