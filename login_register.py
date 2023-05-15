# import bcrypt, re, random, io, string
# from tkinter import *
# from PIL import Image,ImageTk
# from tkinter import messagebox, ttk, filedialog, Tk, Label, Entry, Button, END
# import tkinter as tk
# import tkinter.ttk as ttk
# import mysql.connector
# from mysql.connector import Error
# from captcha.image import ImageCaptcha
# from buttons import toggle_password, ui_bg
# from admin import AdminPage
# from homepage import Homepage

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
   

# class RegisterPage(tk.Frame):
#     def __init__(self,parent=None, controller=None, name=None):
#         tk.Frame.__init__(self, parent)
#         global image_display, image_label
#         self.controller=controller
#         self.name=name
#         self.parent=parent

#         # registerpage bg
#         ui_bg(self, 'images\\Slide2.png')

#         #direct to register page for new users
#         def go_to_login():
#             controller.show_frame(Loginpage)

#         self.login_link_btn = Button(self, text= "Go to Login Page", cursor= "hand2", font= ('Arial', 14), command=go_to_login)
#         self.login_link_btn.place(x=930,y=720)

#         #for testing
#         #direct to registercourses page for users
#         def go_to_registercourses():
#             controller.show_frame(RegisterCourses)
#         self.registercourses_link_btn = Button(self, text= "Go to Register Courses Page", cursor= "hand2", font= ('Arial', 14), command=go_to_registercourses)
#         self.registercourses_link_btn.place(x=400,y=720)    
        
#         #connect to database
#         con = mysql.connector.connect(host="localhost",
#                                       user="root",
#                                       password="rootpass",
#                                       database="all2")             
      
#         cur=con.cursor()
#         cur.execute('''CREATE TABLE IF NOT EXISTS userdata( iduserdata INT AUTO_INCREMENT UNIQUE,
#                                                             name varchar(70) NOT NULL,
#                                                             user_id varchar(45) NOT NULL PRIMARY KEY, 
#                                                             email varchar(45) NOT NULL UNIQUE, 
#                                                             usertype text NOT NULL, 
#                                                             password varchar(256) NOT NULL)''')
#         con.commit()

#         self.user_var=StringVar()
#         self.user_var.set(None)



#         def createImage(flag=0): 
#             global image_display, image_label
            
#             # Generate new random string for captcha
#             # self.random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
#             self.random_string = ''.join(random.choices('a', k=6))  #default value for testing, to be changed later

#             # create captcha image
#             self.image_captcha = ImageCaptcha(width=200, height=55)
#             self.image_generated = self.image_captcha.generate(self.random_string)
#             self.image_display = ImageTk.PhotoImage(Image.open(self.image_generated))
            
#             #executed when pressed reload captcha button
#             if flag == 1:
#                 # Remove previous Image (if present) and display new one
#                 self.image_label.config(image=self.image_display)


#         def insert_record():
#             check_counter=0
#             warn = " "
#             if self.register_name.get() == "":
#                 warn = 'Please enter a name.'
#             else:
#                 check_counter += 1
            
#             if self.register_userid.get() == "" or not re.match(r'^[Pp]\d{8}$', self.register_userid.get()):
#                 warn='Please enter a valid student ID.'
#             else:
#                 check_counter += 1

#             if self.register_email.get() == "" or not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", self.register_email.get()):
#                 warn = 'Please enter a valid email.'
#             else:
#                 check_counter += 1

#             if self.user_var.get() == 'None':
#                 warn = 'Select User Type'
#             else:
#                 check_counter += 1

#             if self.register_pwd.get() == "" or not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+}{":;\'?/>.<,])(?=.*[a-zA-Z]).{8,}$', self.register_pwd.get()):
#                 warn = 'Please enter a minimum 8-character password.\nPassword must contain at least 1 digit and 1 special character.'
#             else:
#                 check_counter += 1

#             if self.pwd_again.get() == "":
#                 warn = 'Please re-enter your password.'
#             else:
#                 check_counter += 1

#             if self.register_pwd.get() != self.pwd_again.get():
#                 warn = 'Your passwords do not match!'
#             else:
#                 check_counter += 1

#             if self.reg_captcha.get() != self.random_string:
#                 warn = 'Wrong captcha'
#             else:
#                 check_counter += 1

#             if check_counter == 8:
#                 try:
#                     con = mysql.connector.connect(host="localhost",
#                                                   user="root",
#                                                   password="rootpass",
#                                                   database="all2")      
#                     cur = con.cursor()
                    
#                     #get user entries
#                     iduserdata= None
#                     name= self.register_name.get()
#                     user_id= self.register_userid.get()
#                     email= self.register_email.get()
#                     usertype= self.user_var.get()
#                     password= self.register_pwd.get()
#                     hashed_pw= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                    
#                     insert_data = ("INSERT INTO userdata(iduserdata, name, user_id, email, usertype, password) VALUES (%s,%s,%s,%s,%s,%s);")
#                     data= (iduserdata, name, user_id, email, usertype, hashed_pw)
#                     cur.execute(insert_data,data)

#                     con.commit()
#                     messagebox.showinfo('Register', 'Account Created Successfully!')
#                     if self.user_var.get()== 'Lecturer':
#                         controller.show_frame(AdminPage)
#                     else:
#                         controller.show_frame(RegisterCourses)

#                 except Exception as ep:
#                     messagebox.showerror('', ep)
#             else:
#                 messagebox.showerror('Error', warn)

#         #captcha function
#         createImage()

#         #register frame
#         self.reg_frame = Frame(self, bd=2, bg='salmon',relief=SOLID, padx=10, pady=-1000)
#         Label(self.reg_frame, text="Name", bg='salmon',font=f).grid(row=0, column=0, sticky=W, pady=10, padx=10)
#         Label(self.reg_frame, text="ID", bg='salmon',font=f).grid(row=1, column=0, sticky=W, pady=10, padx=10)
#         Label(self.reg_frame, text="Email", bg='salmon',font=f).grid(row=2, column=0, sticky=W, pady=10, padx=10)
#         Label(self.reg_frame,text="User Type",bg='salmon',font=f).grid(row=3, column=0, sticky =W, pady=10, padx=10)
#         Label(self.reg_frame, text="Enter Password", bg='salmon',font=f).grid(row=4, column=0, sticky=W, pady=10, padx=10)
#         Label(self.reg_frame, text="Re-Enter Password", bg='salmon',font=f ).grid(row=5, column=0, sticky=W, pady=10)
#         Label(self.reg_frame, text="Enter Captcha", bg='salmon',font=f ).grid(row=6, column=0, sticky=W, pady=10)
#         self.image_label = Label(self.reg_frame, image=self.image_display)
#         self.image_label.grid(row=6, column=1,padx=10, pady=10)
#         self.image_label.image=self.image_display
        
#         #password show/hide button
#         self.register_pwd = Entry(self.reg_frame, font=f, show='*')
#         self.pwd_btn2=Button(self, text='Show', width=4, font=('Arial', 9),  cursor= "hand2", command=lambda:toggle_password(self.register_pwd, self.pwd_btn2))
#         self.pwd_btn2.place(x=1169, y=432)

#         self.pwd_again = Entry(self.reg_frame, font=f, show='*')
#         self.pwd_btn3=Button(self, text='Show', width=4, font=('Arial', 9), cursor= "hand2", command=lambda:toggle_password(self.pwd_again, self.pwd_btn3))
#         self.pwd_btn3.place(x=1169, y=480)

#         #reload button for captcha
#         self.reload_button = Button(self, text='Reload',font=('Arial', 9), cursor='hand2',command=lambda: createImage(1))
#         self.reload_button.place(x=1160, y=606)

#         #widgets
#         self.register_name = Entry(self.reg_frame, font=f)
#         self.register_userid = Entry(self.reg_frame,font=f)
#         self.register_email = Entry(self.reg_frame, font=f)
#         self.usertype_frame = LabelFrame(self.reg_frame,bg='#EEEEEE',padx=10, pady=10)
#         self.student_rb = Radiobutton(self.usertype_frame,text='Student',bg='#EEEEEE',variable=self.user_var,value='Student',font=('Arial',10))
#         self.lect_rb = Radiobutton(self.usertype_frame,text='Lecturer',bg='#EEEEEE',variable=self.user_var,value='Lecturer',font=('Arial',10))
#         self.register_pwd = Entry(self.reg_frame, font=f,show='*')
#         self.pwd_again = Entry(self.reg_frame, font=f,show='*')
#         self.reg_captcha= Entry(self.reg_frame, font=f)
#         self.register_btn = Button(self.reg_frame, width=15, text='Register', font=f, relief=SOLID,cursor='hand2',command= insert_record)

#         #widgets placement
#         self.register_name.grid(row=0, column=1, pady=10, padx=20)
#         self.register_userid.grid(row=1, column=1, pady=10, padx=20)
#         self.register_email.grid(row=2, column=1, pady=10, padx=20) 
#         self.register_pwd.grid(row=4, column=1, pady=10, padx=20)
#         self.pwd_again.grid(row=5, column=1, pady=10, padx=20)
#         self.reg_captcha.grid(row=7, column=1, pady=10, padx=20)
#         self.register_btn.grid(row=8, column=1, pady=10, padx=20)
#         self.reg_frame.place(x=780, y=205)

#         self.usertype_frame.grid(row=3, column=1, pady=10, padx=20)
#         self.student_rb.pack(expand=True, side=LEFT)
#         self.lect_rb.pack(expand=True, side=LEFT)

#         #default entry values for testing
#         self.register_name.insert(0, 'Tom')
#         self.register_userid.insert(0, 'P12345678')
#         self.register_email.insert(0, 'tom@gmail.com')
#         self.register_pwd.insert(0, 'Tom,1234')
#         self.pwd_again.insert(0, 'Tom,1234')
#         self.reg_captcha.insert(0, 'aaaaaa')


# class RegisterCourses(tk.Frame):
#     def __init__(self, parent=None, controller=None, name=None):
#         tk.Frame.__init__(self, parent)
#         self.controller=controller
#         self.name=name
#         self.parent=parent


#         #registercourses page bg
#         ui_bg(self, 'images\\Slide3.png')

#         #for testing
#         #direct to register page for users
#         def go_to_registerpage():
#             controller.show_frame(RegisterPage)
#         self.registerpage_link_btn = Button(self, text= "Go to Register Page", cursor= "hand2", font= ('Arial', 14), command=go_to_registerpage)
#         self.registerpage_link_btn.place(x=700,y=660)


#         #connect to database
#         con = mysql.connector.connect(host="localhost",
#                                       user="root",
#                                       password="rootpass",
#                                       database="all2")
#         cur=con.cursor()
#         cur.execute('''CREATE TABLE IF NOT EXISTS usersubjects(user_id varchar(45) ,
#                                                                level varchar(45) NOT NULL, 
#                                                                year varchar(45) NOT NULL , 
#                                                                school text NOT NULL, 
#                                                                program varchar(256) NOT NULL,
#                                                                semester varchar(256) NOT NULL,
#                                                                subject1 varchar(256) NOT NULL,
#                                                                subject2 varchar(256) NOT NULL,
#                                                                subject3 varchar(256) NOT NULL,
#                                                                subject4 varchar(256) NOT NULL,
#                                                                FOREIGN KEY (user_id) REFERENCES userdata(user_id))''')
#         con.commit()

#         #insert record into database
#         def insert_subjrecord():
#             check_counter=0
#             warn = " "
#             if self.userid_entry.get() == "":
#                 warn = 'Please enter a valid ID.'
#             else:
#                 check_counter += 1

#             if self.studylevel.get() == "Select":
#                 warn = 'Select study level.'
#             else:
#                 check_counter += 1

#             if self.studyyear.get() == "Select":
#                 warn = 'Select study year.'
#             else:
#                 check_counter += 1

#             if self.studysch.get() == "Select":
#                 warn = 'Select school.'
#             else:
#                 check_counter += 1

#             if self.studyprog.get() == "Select":
#                 warn = 'Select program.'
#             else:
#                 check_counter += 1

#             if self.studysem.get() == "Select":
#                 warn = 'Select semester.'
#             else:
#                 check_counter += 1
            
#             selected_subjects= [self.studysubj1.get(), self.studysubj2.get(), self.studysubj3.get(), self.studysubj4.get()]

#             if self.studysubj1.get() == "Select" and self.studysubj2.get() == "Select" and self.studysubj3.get() == "Select" and self.studysubj4.get() == "Select":
#                 warn = 'Select at least one subject.'
#             else:
#                 check_counter += 1

#             unique_subjects = set(selected_subjects)
#             unique_subjects.discard("Select")

#             if len(unique_subjects) < len(selected_subjects) - selected_subjects.count("Select"):
#                 warn = 'You have selected the same subject.'
#             else:
#                 check_counter += 1

#             if check_counter ==8:
#                 try:
#                     con = mysql.connector.connect(host="localhost",
#                                                   user="root",
#                                                   password="rootpass",
#                                                   database="all2")      
#                     cur = con.cursor()

#                     #get user entries
#                     user_id= self.userid_entry.get()
#                     level= self.studylevel.get()
#                     year= self.studyyear.get()
#                     school= self.studysch.get()
#                     program= self.studyprog.get()
#                     semester= self.studysem.get()
#                     subject1= self.studysubj1.get()
#                     subject2= self.studysubj2.get()
#                     subject3= self.studysubj3.get()
#                     subject4= self.studysubj4.get()

#                     insert_subjectrecord = ("INSERT INTO usersubjects(user_id, level, year, school, program, semester, subject1, subject2, subject3, subject4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
#                     data= (user_id, level, year, school, program, semester, subject1, subject2, subject3, subject4)
#                     cur.execute(insert_subjectrecord,data)

#                     con.commit()
#                     messagebox.showinfo('Register', 'Subjects Registered Successfully!')
#                     controller.show_frame(Homepage)

#                 except Exception as ep:
#                     messagebox.showerror('', ep)
#             else:
#                 messagebox.showerror('Error', warn)

#         #register courses frame
#         self.regcourses_frame = Frame(self, bd=2, bg='salmon',relief=SOLID, padx=10, pady=-1000)
#         Label(self.regcourses_frame, text="ID", bg='salmon',font=f).grid(row=0, column=0, sticky=W, pady=10, padx=10)
#         Label(self.regcourses_frame, text="Level", bg='salmon',font=f).grid(row=1, column=0, sticky=W, pady=10, padx=10)
#         Label(self.regcourses_frame, text="Year", bg='salmon',font=f).grid(row=2, column=0, sticky=W, pady=10, padx=10)
#         Label(self.regcourses_frame,text="School",bg='salmon',font=f).grid(row=3, column=0, sticky =W, pady=10, padx=10)
#         Label(self.regcourses_frame, text="Program", bg='salmon',font=f).grid(row=4, column=0, sticky=W, pady=10, padx=10)
#         Label(self.regcourses_frame, text="Semester", bg='salmon',font=f ).grid(row=5, column=0, sticky=W, pady=10)
#         Label(self.regcourses_frame, text="Subjects", bg='salmon',font=f ).grid(row=6, column=0, sticky=W, pady=10)
        
#         #optionmenu values
#         level=['Select','Degree']
#         year=['Select','1','2','3','4']
#         school=['Select','School of Computing']
#         program=['Select','BCSCUN','BCTCUN']
#         semester=['Select','1','2','3']
#         subjects=['Select','Computer Architecture & Networks', 'Objected Oriented Programming', 'Mathematics for Computer Science', 'Database Systems', 'Programming & Algorithms']
        
#         #default values for optionmenus
#         self.level_var=StringVar()
#         self.level_var.set(level[0])
#         self.year_var=StringVar()
#         self.year_var.set(year[0])
#         self.school_var=StringVar()
#         self.school_var.set(school[0])
#         self.program_var=StringVar()
#         self.program_var.set(program[0])
#         self.semester_var=StringVar()
#         self.semester_var.set(semester[0])
#         self.subject1_var=StringVar()
#         self.subject1_var.set('Select')
#         self.subject2_var=StringVar()
#         self.subject2_var.set('Select')
#         self.subject3_var=StringVar()
#         self.subject3_var.set('Select')
#         self.subject4_var=StringVar()
#         self.subject4_var.set('Select')

#         #widgets
#         self.userid_entry = Entry(self.regcourses_frame, font=f)
#         self.studylevel = ttk.Combobox(self.regcourses_frame, textvariable = self.level_var, values=level, state='readonly',  width=20, font=f)
#         self.studyyear = ttk.Combobox(self.regcourses_frame,textvariable = self.year_var, values=year, state='readonly', width=20, font=f)
#         self.studysch = ttk.Combobox(self.regcourses_frame, textvariable = self.school_var, values=school, state='readonly', width=20, font=f)
#         self.studyprog = ttk.Combobox(self.regcourses_frame,textvariable = self.program_var, values=program, state='readonly', width=20, font=f)
#         self.studysem = ttk.Combobox(self.regcourses_frame, textvariable = self.semester_var, values=semester, state='readonly', width=20, font=f)
#         self.studysubj1 = ttk.Combobox(self.regcourses_frame,textvariable = self.subject1_var, values=subjects, state='readonly', width=20, font=f)
#         self.studysubj2 = ttk.Combobox(self.regcourses_frame,textvariable = self.subject2_var, values=subjects, state='readonly', width=20, font=f)
#         self.studysubj3 = ttk.Combobox(self.regcourses_frame,textvariable = self.subject3_var, values=subjects, state='readonly', width=20, font=f)
#         self.studysubj4 = ttk.Combobox(self.regcourses_frame,textvariable = self.subject4_var, values=subjects, state='readonly', width=20, font=f)
#         self.register_btn = Button(self.regcourses_frame, width=15, text='Register', font=f, relief=SOLID,cursor='hand2', command=insert_subjrecord )
        
        
#         #remove blue highlight after selection in combobox
#         self.studylevel.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
#         self.studyyear.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
#         self.studysch.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
#         self.studyprog.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
#         self.studysem.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
#         self.studysubj1.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
#         self.studysubj2.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
#         self.studysubj3.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
#         self.studysubj4.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())

#         #widgets placement
#         self.userid_entry.grid(row=0, column=1, pady=10, padx=20)
#         self.studylevel.grid(row=1, column=1, pady=10, padx=20)
#         self.studyyear.grid(row=2, column=1, pady=10, padx=20)
#         self.studysch.grid(row=3, column=1, pady=10, padx=20)
#         self.studyprog.grid(row=4, column=1, pady=10, padx=20)
#         self.studysem.grid(row=5, column=1, pady=10, padx=20)
#         self.studysubj1.grid(row=6, column=1, pady=10, padx=20)
#         self.studysubj2.grid(row=7, column=1, pady=10, padx=20)
#         self.studysubj3.grid(row=8, column=1, pady=10, padx=20)
#         self.studysubj4.grid(row=9, column=1, pady=10, padx=20)
#         self.register_btn.grid(row=10, column=1, pady=10, padx=20)
#         self.regcourses_frame.place(x=75, y=210)