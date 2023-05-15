import bcrypt, re, random, io, string
from tkcalendar import Calendar
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox, ttk, filedialog, Tk, Label, Entry, Button, END
import tkinter as tk
import mysql.connector
from mysql.connector import Error
from buttons import ui_bg, admin_btns, clockdate




f=('Arial', 14)
f2=('Arial', 12)
bgc='#F9D3B9'

#show all students
#show students listview
class StudentsView(tk.Frame):
    def __init__(self,parent=None, controller=None, name=None):
        global show_students_frame, show_books_frame
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.name=name
        self.parent=parent

        #ui_bg and clock 
        ui_bg(self, 'images/Slide5.png')
        clockdate(self)

        admin_btns(self, StudentsView, BooksView, controller)
        show_students_frame=Frame(self, bd=2, relief=SOLID, bg=bgc)
        show_students_frame.place(x=40, y=155)

        #student view label
        student_view_label=Label(show_students_frame, text='Student View', font=('Arial', 20, 'bold'), bg=bgc, fg='black')
        student_view_label.pack(pady=10)

        #show students treeview
        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', font=f)
        style.configure('Treeview', font=f2)

        tree_frame=Frame(show_students_frame)
        tree_frame.pack(pady=10)

        tree_scroll=Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
        my_tree.pack()

        tree_scroll.config(command=my_tree.yview)

        my_tree['columns']= ('Name', 'Student ID', 'Email','Subject 1', 'Subject 2', 'Subject 3','Subject 4')

        #format columns
        my_tree.column('#0', width=0, stretch=NO)
        my_tree.column('Name', width=150, anchor=CENTER, stretch=NO)
        my_tree.column('Student ID', width=150, anchor=CENTER, stretch=NO)
        my_tree.column('Email', width=180, anchor=CENTER, stretch=NO)
        my_tree.column('Subject 1', width=200, anchor=CENTER, stretch=NO)
        my_tree.column('Subject 2', width=200, anchor=CENTER, stretch=NO)
        my_tree.column('Subject 3', width=200, anchor=CENTER, stretch=NO)
        my_tree.column('Subject 4', width=200, anchor=CENTER, stretch=NO)


        #column headings
        my_tree.heading('#0', text='', anchor=CENTER)
        my_tree.heading('Name', text='Name', anchor=CENTER)
        my_tree.heading('Student ID', text='Student ID', anchor=CENTER)
        my_tree.heading('Email', text='Email', anchor=CENTER)
        my_tree.heading('Subject 1', text='Subject 1', anchor=CENTER)
        my_tree.heading('Subject 2', text='Subject 2', anchor=CENTER)
        my_tree.heading('Subject 3', text='Subject 3', anchor=CENTER)
        my_tree.heading('Subject 4', text='Subject 4', anchor=CENTER)

        #get data from database
        con = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="rootpass",
                                    database="all2")
        cur = con.cursor()
        r_set=cur.execute("SELECT a.name, a.user_id, a.email, b.subject1, b.subject2, b.subject3, b.subject4 FROM userdata a, usersubjects b WHERE a.usertype='Student' AND a.user_id = b.user_id;")
        r_set=cur.fetchall()
        for row in r_set:
            my_tree.insert("", tk.END, values=row)

        show_students_frame.forget()

#add/delete /view books
class BooksView(tk.Frame):
    def __init__(self,parent=None, controller=None, name=None):
        global show_students_frame, show_books_frame
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.name=name
        self.parent=parent

        ui_bg(self, 'images/Slide5.png')


        admin_btns(self, StudentsView, BooksView, controller)


        show_books_frame=Frame(self, bd=2, relief=SOLID, bg=bgc)
        show_books_frame.place(x=40, y=155)

        #student view label
        student_view_label=Label(show_books_frame, text='Book View', font=('Arial', 20, 'bold'), bg=bgc, fg='black')
        student_view_label.pack(pady=10)

        #show students treeview
        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', font=f)
        style.configure('Treeview', font=f2)

        tree_frame=Frame(show_books_frame)
        tree_frame.pack(pady=10)

        tree_scroll=Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
        my_tree.pack()

        tree_scroll.config(command=my_tree.yview)

        my_tree['columns']= ('ID', 'Book Cover','Book Name', 'Category')

        #format columns
        my_tree.column('#0', width=0, stretch=NO)
        my_tree.column('ID', width=150, anchor=CENTER, stretch=NO)
        my_tree.column('Book Cover', width=150, anchor=CENTER, stretch=NO)
        my_tree.column('Book Name', width=180, anchor=CENTER, stretch=NO)
        my_tree.column('Category', width=200, anchor=CENTER, stretch=NO)


        #column headings
        my_tree.heading('#0', text='', anchor=CENTER)
        my_tree.heading('ID', text='ID', anchor=CENTER)
        my_tree.heading('Book Cover', text='Book Cover', anchor=CENTER)
        my_tree.heading('Book Name', text='Book Name', anchor=CENTER)
        my_tree.heading('Category', text='Category', anchor=CENTER)


        #get data from database
        con = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="rootpass",
                                    database="all2")
        cur = con.cursor()
        r_set=cur.execute("SELECT idbooks, bookcover, bookname, bookcategory from books;")
        r_set=cur.fetchall()
        for row in r_set:
            book_img = Image.open(row[1])
            book_img = book_img.resize((100, 100), Image.LANCZOS)
            book_img = ImageTk.PhotoImage(book_img)
            my_tree.insert("", tk.END, values=(row[0], book_img, row[2], row[3]))

    



