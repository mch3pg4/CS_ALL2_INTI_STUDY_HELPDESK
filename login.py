# import bcrypt, re, random, io, string
# from tkinter import *
# from tkinter import messagebox, ttk, filedialog, Tk, Label, Entry, Button, END
# import tkinter as tk
# import tkinter.ttk as ttk
# import mysql.connector
# from mysql.connector import Error
# from buttons import toggle_password, ui_bg
# from admin import AdminPage
# from ALL2_test1 import Homepage, RegisterPage

# f=('Arial', 14)
# f2=('Arial', 12)



# class Loginpage(tk.Frame):
#     def __init__(self, parent=None, controller=None, name=None):
#         tk.Frame.__init__(self, parent)
#         self.controller=controller
#         self.name=name
#         self.parent=parent

#         #loginpage bg
#         ui_bg(self, 'images\\Slide1.png')
        


#         #direct to register page for new users
#         def go_to_register():
#             controller.show_frame(RegisterPage)
#         self.register_link_btn = Button(self, text= "New user? Go to Register Page", cursor= "hand2", font= ('Arial', 14), command=go_to_register)
#         self.register_link_btn.place(x=860,y=500)
        
                
#         def login_response():
#             global login_details
#             try:
#                 uname = self.email_tf.get()
#                 upwd = self.pwd_tf.get()

#                 con = mysql.connector.connect(host="localhost",
#                                               user="root",
#                                               password="rootpass",
#                                               database="all2") 
#                 c = con.cursor()
#                 c.execute("SELECT * FROM userdata WHERE email=%s ",(uname,))
                
#             except Exception as ep:
#                 messagebox.showerror('Error', ep)

#             check_counter=0
#             if uname == '':
#                 warn ='Please enter username.'
#             else: 
#                 check_counter += 1
#             if upwd == "":
#                 warn = "Please enter password."
#             else:
#                 check_counter += 1
#             if check_counter == 2:
#                 login_details=c.fetchone()
#                 if login_details is not None:
#                     if bcrypt.checkpw(upwd.encode('utf-8'),login_details[5].encode('utf-8')) & (login_details[4]== 'Student'):
#                         controller.show_frame(Homepage)
#                     # messagebox.showinfo('Login Status', 'Logged in Successfully!')
#                     # controller.updateProfile( login_details)
#                     # controller.updateHomepage(login_details)
#                     # controller.updateAdmin(login_details)
#                     elif bcrypt.checkpw(upwd.encode('utf-8'),login_details[5].encode('utf-8')) & (login_details[4]== 'Lecturer'):
#                         controller.show_frame(AdminPage)
#                     else:
#                         messagebox.showerror('Login Status', 'invalid username or password')
#             else:
#                 messagebox.showerror('Error', warn)

     
#         # widgets
#         self.left_frame = Frame(self, bd=2, bg='salmon',   relief=SOLID, padx=10, pady=-1000)
#         Label(self.left_frame, text="Email", bg='salmon',font=f).grid(row=0, column=0, sticky=W, pady=10)
#         Label(self.left_frame, text="Password", bg='salmon',font=f).grid(row=1, column=0, pady=10)
#         self.email_tf = Entry(self.left_frame, font=f)
#         self.email_tf.insert(0, 'brad@gmail.com')   #default value for testing

#         self.pwd_tf = Entry(self.left_frame, font=f, show='*')    #default value for testing
#         self.pwd_tf.insert(0, 'Brad,123')
#         self.pwd_btn=Button(self, text='Show', width=4, font=('Arial', 9), cursor= "hand2",command=lambda:toggle_password(self.pwd_tf, self.pwd_btn))
#         self.pwd_btn.place(x=1123, y=382)
        
#         self.login_btn = Button(self.left_frame, width=15, text='Login', font=f, relief=SOLID,cursor='hand2',command=login_response)

#         # widgets placement
#         self.email_tf.grid(row=0, column=1, pady=10, padx=20)
#         self.pwd_tf.grid(row=1, column=1, pady=10, padx=20)
#         self.login_btn.grid(row=2, column=1, pady=10, padx=20)
#         self.left_frame.place(x=815, y=320)
   

