import bcrypt, re, random, textwrap, datetime
from tkcalendar import Calendar, DateEntry
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox, ttk, filedialog,  Label, Entry, Button, END, scrolledtext
import tkinter as tk
import tkinter.ttk as ttk
from time import strftime
from datetime import date
from dateutil.relativedelta import relativedelta
import mysql.connector
from mysql.connector import Error
from captcha.image import ImageCaptcha
from tktooltip import ToolTip
from tkPDFViewer import tkPDFViewer as pdf
from buttons import clockdate, ui_bg, log_out_btn, toggle_password, admin_btns, view_user, back_btn, expand_tv, collapse_tv, view_appt



f=('Arial', 14)
f2=('Arial', 12)
f3=('Arial', 16)
f4=('Arial', 18)
bgc='#F9D3B9'
empty_text='  '

img_file='images\Slide4.png'

#optionmenu values
level=['Select','Degree']
year=['Select','1','2','3','4']
school=['Select','School of Computing']
program=['Select','BCSCUN','BCTCUN']
semester=['Select','1','2','3']
subjects=['Select','Computer Architecture & Networks', 'Objected Oriented Programming', 'Mathematics for Computer Science', 'Database Systems', 'Programming & Algorithms']
weeks=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
questions=['5', '10', '15']
options=['A', 'B', 'C', 'D']
hours=['09', '10', '11', '12', '13', '14', '15', '16']
minutes=['00', '15', '30', '45']


#top buttons
def top_buttons(self, controller):
    image2=Image.open('images\home.png')
    img2=image2.resize((65,65))
    my_img2=ImageTk.PhotoImage(img2)
    homepage_icon=Label(image=my_img2)
    homepage_icon.image=my_img2

    image3=Image.open('images\\readbooks.png')
    img3=image3.resize((65,65))
    my_img3=ImageTk.PhotoImage(img3)
    books_icon=Label(image=my_img3)
    books_icon.image=my_img3

    image4=Image.open('images\\quiz.png')
    img4=image4.resize((65,65))
    my_img4=ImageTk.PhotoImage(img4)
    quiz_icon=Label(image=my_img4)
    quiz_icon.image=my_img4

    image5=Image.open('images\\calculator.png')
    img5=image5.resize((65,65))
    my_img5=ImageTk.PhotoImage(img5)
    calc_icon=Label(image=my_img5)
    calc_icon.image=my_img5

    image6=Image.open('images\\qa.png')
    img6=image6.resize((65,65))
    my_img6=ImageTk.PhotoImage(img6)
    chat_icon=Label(image=my_img6)
    chat_icon.image=my_img6

    image7=Image.open('images\\chatbot.png')
    img7=image7.resize((65,65))
    my_img7=ImageTk.PhotoImage(img7)
    chatbot_icon=Label(image=my_img7)
    chatbot_icon.image=my_img7

    image8=Image.open('images\\user.png')
    img8=image8.resize((50,50))
    my_img8=ImageTk.PhotoImage(img8)
    profile_icon=Label(image=my_img8)
    profile_icon.image=my_img8

    image9=Image.open('images\\game.png')
    img9=image9.resize((50,50))
    my_img9=ImageTk.PhotoImage(img9)
    game_icon=Label(image=my_img9)
    game_icon.image=my_img9

    button1=tk.Button(self, image=my_img2,cursor='hand2',command= lambda:controller.show_frame(Homepage))
    button1.place(x=3, y=90)
    ToolTip(button1, msg='Homepage')

    button2=tk.Button(self, image=my_img3, cursor='hand2',command= lambda:controller.show_frame(Books))
    button2.place(x=3, y=210)
    ToolTip(button2, msg='Books')

    button3=tk.Button(self, image=my_img4,cursor='hand2', command= lambda:controller.show_frame(Quiz))
    button3.place(x=3, y=330)
    ToolTip(button3, msg='Quiz')

    button4=tk.Button(self, image=my_img5,cursor='hand2',command= lambda:controller.show_frame(Calculator))
    button4.place(x=3, y=450)
    ToolTip(button4, msg='Calculator')

    button4=tk.Button(self, image=my_img6,cursor='hand2',command= lambda:controller.show_frame(Chat))
    button4.place(x=3, y=570)
    ToolTip(button4, msg='Discussions')

    button5=tk.Button(self, image=my_img7,cursor='hand2',command= lambda:controller.show_frame(Chatbot))
    button5.place(x=3, y=690)
    ToolTip(button5, msg='Chatbot')

    button6=tk.Button(self, image=my_img8, cursor='hand2',command=lambda: controller.show_frame(Profile))
    button6.place(x=1225, y=5)
    ToolTip(button6, msg='Profile')

    button7=tk.Button(self, image=my_img9, cursor='hand2',command=lambda: controller.show_frame(Games))
    button7.place(x=1075, y=5)
    ToolTip(button7, msg='Games')



class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global show_frame

        #create frame and assign it to container
        container = tk.Frame(self)

        container.pack(fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #create app icon
        iconpic = ImageTk.PhotoImage(file='images\inti_icon.png')
        self.iconphoto(False,iconpic)

        #create dictionary of frames
        self.frames={}

        for F in (Loginpage, RegisterPage, RegisterCourses,Homepage, Subject1, Books, Quiz, Calculator, Chat,Chatbot, Appointments, Games, Profile, StudentsView, BooksView, QuizAdmin, ChatAdmin, CourseMaterials, AdminAppointments):
            frame= F(container, self)
            #windows class act as root window for frames
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        #using a method to switch frames
        self.show_frame(Loginpage)

    #method to switch view frames
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


    def updateProfile(self, login_details):
        frame = self.frames[Profile]
        frame.profile_name_lbl.config(text='Name: '+login_details[1])
        frame.profile_id_lbl.config(text='ID: '+login_details[2])
        frame.profile_email_lbl.config(text='Email: '+login_details[3])
        frame.tkraise()


class Loginpage(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        #loginpage bg
        self.raw_image=Image.open("images\Slide1.png")
        self.background_image=ImageTk.PhotoImage(self.raw_image)
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=-215,y=-155)
        self.background_label.image = self.background_image


        #direct to register page for new users
        def go_to_register():
            controller.show_frame(RegisterPage)
        self.register_link_btn = Button(self, text= "New user? Go to Register Page", cursor= "hand2", font= ('Arial', 14), command=go_to_register)
        self.register_link_btn.place(x=860,y=500)
        
                
        def login_response():
            global login_details
            try:
                uname = self.email_tf.get()
                upwd = self.pwd_tf.get()

                con = mysql.connector.connect(host="localhost",
                                              user="root",
                                              password="rootpass",
                                              database="all2") 
                c = con.cursor()
                c.execute("SELECT * FROM userdata WHERE email=%s ",(uname,))
                
            except Exception as ep:
                messagebox.showerror('Error', ep)

            check_counter=0
            if uname == '':
                warn ='Please enter username.'
            else: 
                check_counter += 1
            if upwd == "":
                warn = "Please enter password."
            else:
                check_counter += 1
            if check_counter == 2:
                login_details=c.fetchone()
                if login_details is not None:
                    controller.updateProfile(login_details)
                    if bcrypt.checkpw(upwd.encode('utf-8'),login_details[5].encode('utf-8')) & (login_details[4]== 'Student'):
                        controller.show_frame(Homepage)
                    # controller.updateHomepage(login_details)
                    # controller.updateAdmin(login_details)
                    elif bcrypt.checkpw(upwd.encode('utf-8'),login_details[5].encode('utf-8')) & (login_details[4]== 'Lecturer'):
                        controller.show_frame(StudentsView)
                        
                    else:
                        messagebox.showerror('Login Status', 'invalid username or password')
            else:
                messagebox.showerror('Error', warn)

     
        # widgets
        self.left_frame = Frame(self, bd=2, bg='salmon',   relief=SOLID, padx=10, pady=-1000)
        Label(self.left_frame, text="Email", bg='salmon',font=f).grid(row=0, column=0, sticky=W, pady=10)
        Label(self.left_frame, text="Password", bg='salmon',font=f).grid(row=1, column=0, pady=10)
        self.email_tf = Entry(self.left_frame, font=f)
        self.email_tf.insert(0, 'lect1@gmail.com')   #default value for testing

        self.pwd_tf = Entry(self.left_frame, font=f, show='*')    #default value for testing
        self.pwd_tf.insert(0, 'Lect,1234')
        self.pwd_btn=Button(self, text='Show', width=4, font=('Arial', 9), cursor= "hand2",command=lambda:toggle_password(self.pwd_tf, self.pwd_btn))
        self.pwd_btn.place(x=1123, y=382)
        
        self.login_btn = Button(self.left_frame, width=15, text='Login', font=f, relief=SOLID,cursor='hand2',command=login_response)

        # widgets placement
        self.email_tf.grid(row=0, column=1, pady=10, padx=20)
        self.pwd_tf.grid(row=1, column=1, pady=10, padx=20)
        self.login_btn.grid(row=2, column=1, pady=10, padx=20)
        self.left_frame.place(x=815, y=320)
   

class RegisterPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        # registerpage bg
        self.raw_image=Image.open("images\Slide2.png")
        self.background_image=ImageTk.PhotoImage(self.raw_image)
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=-215,y=-155)
        self.background_label.image = self.background_image

        #direct to register page for new users
        def go_to_login():
            controller.show_frame(Loginpage)

        self.login_link_btn = Button(self, text= "Go to Login Page", cursor= "hand2", font= ('Arial', 14), command=go_to_login)
        self.login_link_btn.place(x=930,y=720)

        #for testing
        #direct to registercourses page for users
        def go_to_registercourses():
            controller.show_frame(RegisterCourses)
        self.registercourses_link_btn = Button(self, text= "Go to Register Courses Page", cursor= "hand2", font= ('Arial', 14), command=go_to_registercourses)
        self.registercourses_link_btn.place(x=400,y=720)    
        
        #connect to database
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="rootpass",
                                      database="all2")             
      
        cur=con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS userdata( iduserdata INT AUTO_INCREMENT UNIQUE,
                                                            name varchar(70) NOT NULL,
                                                            user_id varchar(45) NOT NULL PRIMARY KEY, 
                                                            email varchar(45) NOT NULL UNIQUE, 
                                                            usertype text NOT NULL, 
                                                            password varchar(256) NOT NULL)''')
        con.commit()

        self.user_var=StringVar()
        self.user_var.set(None)



        def createImage(flag=0):             
            # Generate new random string for captcha
            # self.random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            self.random_string = ''.join(random.choices('a', k=6))  #default value for testing, to be changed later

            # create captcha image
            self.image_captcha = ImageCaptcha(width=200, height=55)
            self.image_generated = self.image_captcha.generate(self.random_string)
            self.image_display = ImageTk.PhotoImage(Image.open(self.image_generated))
            
            #executed when pressed reload captcha button
            if flag == 1:
                # Remove previous Image (if present) and display new one
                self.image_label.config(image=self.image_display)


        def insert_record():
            check_counter=0
            warn = " "
            if self.register_name.get() == "":
                warn = 'Please enter a name.'
            else:
                check_counter += 1
            
            if self.register_userid.get() == "" or not re.match(r'^[Pp]\d{8}$', self.register_userid.get()):
                warn='Please enter a valid student ID.'
            else:
                check_counter += 1

            if self.register_email.get() == "" or not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", self.register_email.get()):
                warn = 'Please enter a valid email.'
            else:
                check_counter += 1

            if self.user_var.get() == 'None':
                warn = 'Select User Type'
            else:
                check_counter += 1

            if self.register_pwd.get() == "" or not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+}{":;\'?/>.<,])(?=.*[a-zA-Z]).{8,}$', self.register_pwd.get()):
                warn = 'Please enter a minimum 8-character password.\nPassword must contain at least 1 digit and 1 special character.'
            else:
                check_counter += 1

            if self.pwd_again.get() == "":
                warn = 'Please re-enter your password.'
            else:
                check_counter += 1

            if self.register_pwd.get() != self.pwd_again.get():
                warn = 'Your passwords do not match!'
            else:
                check_counter += 1

            if self.reg_captcha.get() != self.random_string:
                warn = 'Wrong captcha'
            else:
                check_counter += 1

            if check_counter == 8:
                try:
                    con = mysql.connector.connect(host="localhost",
                                                  user="root",
                                                  password="rootpass",
                                                  database="all2")      
                    cur = con.cursor()
                    
                    #get user entries
                    iduserdata= None
                    name= self.register_name.get()
                    user_id= self.register_userid.get()
                    email= self.register_email.get()
                    usertype= self.user_var.get()
                    password= self.register_pwd.get()
                    hashed_pw= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                    
                    insert_data = ("INSERT INTO userdata(iduserdata, name, user_id, email, usertype, password) VALUES (%s,%s,%s,%s,%s,%s);")
                    data= (iduserdata, name, user_id, email, usertype, hashed_pw)
                    cur.execute(insert_data,data)

                    con.commit()
                    con.close()
                    messagebox.showinfo('Register', 'Account Created Successfully!')
                    if self.user_var.get()== 'Lecturer':
                        controller.show_frame(StudentsView)
                    else:
                        controller.show_frame(RegisterCourses)

                except Exception as ep:
                    messagebox.showerror('', ep)
            else:
                messagebox.showerror('Error', warn)

        #captcha function
        createImage()

        #register frame
        self.reg_frame = Frame(self, bd=2, bg='salmon',relief=SOLID, padx=10, pady=-1000)
        Label(self.reg_frame, text="Name", bg='salmon',font=f).grid(row=0, column=0, sticky=W, pady=10, padx=10)
        Label(self.reg_frame, text="ID", bg='salmon',font=f).grid(row=1, column=0, sticky=W, pady=10, padx=10)
        Label(self.reg_frame, text="Email", bg='salmon',font=f).grid(row=2, column=0, sticky=W, pady=10, padx=10)
        Label(self.reg_frame,text="User Type",bg='salmon',font=f).grid(row=3, column=0, sticky =W, pady=10, padx=10)
        Label(self.reg_frame, text="Enter Password", bg='salmon',font=f).grid(row=4, column=0, sticky=W, pady=10, padx=10)
        Label(self.reg_frame, text="Re-Enter Password", bg='salmon',font=f ).grid(row=5, column=0, sticky=W, pady=10)
        Label(self.reg_frame, text="Enter Captcha", bg='salmon',font=f ).grid(row=6, column=0, sticky=W, pady=10)
        self.image_label = Label(self.reg_frame, image=self.image_display)
        self.image_label.grid(row=6, column=1,padx=10, pady=10)
        self.image_label.image=self.image_display
        
        #password show/hide button
        self.register_pwd = Entry(self.reg_frame, font=f, show='*')
        self.pwd_btn2=Button(self, text='Show', width=4, font=('Arial', 9),  cursor= "hand2", command=lambda:toggle_password(self.register_pwd, self.pwd_btn2))
        self.pwd_btn2.place(x=1169, y=432)

        self.pwd_again = Entry(self.reg_frame, font=f, show='*')
        self.pwd_btn3=Button(self, text='Show', width=4, font=('Arial', 9), cursor= "hand2", command=lambda:toggle_password(self.pwd_again, self.pwd_btn3))
        self.pwd_btn3.place(x=1169, y=480)

        #reload button for captcha
        self.reload_button = Button(self, text='Reload',font=('Arial', 9), cursor='hand2',command=lambda: createImage(1))
        self.reload_button.place(x=1160, y=606)

        #widgets
        self.register_name = Entry(self.reg_frame, font=f)
        self.register_userid = Entry(self.reg_frame,font=f)
        self.register_email = Entry(self.reg_frame, font=f)
        self.usertype_frame = LabelFrame(self.reg_frame,bg='#EEEEEE',padx=10, pady=10)
        self.student_rb = Radiobutton(self.usertype_frame,text='Student',bg='#EEEEEE',variable=self.user_var,value='Student',font=('Arial',10))
        self.lect_rb = Radiobutton(self.usertype_frame,text='Lecturer',bg='#EEEEEE',variable=self.user_var,value='Lecturer',font=('Arial',10))
        self.register_pwd = Entry(self.reg_frame, font=f,show='*')
        self.pwd_again = Entry(self.reg_frame, font=f,show='*')
        self.reg_captcha= Entry(self.reg_frame, font=f)
        self.register_btn = Button(self.reg_frame, width=15, text='Register', font=f, relief=SOLID,cursor='hand2',command= insert_record)

        #widgets placement
        self.register_name.grid(row=0, column=1, pady=10, padx=20)
        self.register_userid.grid(row=1, column=1, pady=10, padx=20)
        self.register_email.grid(row=2, column=1, pady=10, padx=20) 
        self.register_pwd.grid(row=4, column=1, pady=10, padx=20)
        self.pwd_again.grid(row=5, column=1, pady=10, padx=20)
        self.reg_captcha.grid(row=7, column=1, pady=10, padx=20)
        self.register_btn.grid(row=8, column=1, pady=10, padx=20)
        self.reg_frame.place(x=780, y=205)

        self.usertype_frame.grid(row=3, column=1, pady=10, padx=20)
        self.student_rb.pack(expand=True, side=LEFT)
        self.lect_rb.pack(expand=True, side=LEFT)

        #default entry values for testing
        self.register_name.insert(0, 'Tom')
        self.register_userid.insert(0, 'P12345678')
        self.register_email.insert(0, 'tom@gmail.com')
        self.register_pwd.insert(0, 'Tom,1234')
        self.pwd_again.insert(0, 'Tom,1234')
        self.reg_captcha.insert(0, 'aaaaaa')


class RegisterCourses(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #registercourses page bg
        self.raw_image=Image.open("images\Slide3.png")
        self.background_image=ImageTk.PhotoImage(self.raw_image)
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=-443,y=-155)
        self.background_label.image = self.background_image

        #for testing
        #direct to register page for users
        def go_to_registerpage():
            controller.show_frame(RegisterPage)
        self.registerpage_link_btn = Button(self, text= "Go to Register Page", cursor= "hand2", font= ('Arial', 14), command=go_to_registerpage)
        self.registerpage_link_btn.place(x=700,y=660)


        #connect to database
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="rootpass",
                                      database="all2")
        cur=con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS usersubjects(user_id varchar(45) ,
                                                               level varchar(45) NOT NULL, 
                                                               year varchar(45) NOT NULL , 
                                                               school text NOT NULL, 
                                                               program varchar(256) NOT NULL,
                                                               semester varchar(256) NOT NULL,
                                                               subject1 varchar(256) NOT NULL,
                                                               subject2 varchar(256) NOT NULL,
                                                               subject3 varchar(256) NOT NULL,
                                                               subject4 varchar(256) NOT NULL,
                                                               FOREIGN KEY (user_id) REFERENCES userdata(user_id))''')
        con.commit()

        #insert record into database
        def insert_subjrecord():
            check_counter=0
            warn = " "
            if self.userid_entry.get() == "":
                warn = 'Please enter a valid ID.'
            else:
                check_counter += 1

            if self.studylevel.get() == "Select":
                warn = 'Select study level.'
            else:
                check_counter += 1

            if self.studyyear.get() == "Select":
                warn = 'Select study year.'
            else:
                check_counter += 1

            if self.studysch.get() == "Select":
                warn = 'Select school.'
            else:
                check_counter += 1

            if self.studyprog.get() == "Select":
                warn = 'Select program.'
            else:
                check_counter += 1

            if self.studysem.get() == "Select":
                warn = 'Select semester.'
            else:
                check_counter += 1
            
            selected_subjects= [self.studysubj1.get(), self.studysubj2.get(), self.studysubj3.get(), self.studysubj4.get()]

            if self.studysubj1.get() == "Select" and self.studysubj2.get() == "Select" and self.studysubj3.get() == "Select" and self.studysubj4.get() == "Select":
                warn = 'Select at least one subject.'
            else:
                check_counter += 1

            unique_subjects = set(selected_subjects)
            unique_subjects.discard("Select")

            if len(unique_subjects) < len(selected_subjects) - selected_subjects.count("Select"):
                warn = 'You have selected the same subject.'
            else:
                check_counter += 1

            if check_counter ==8:
                try:
                    con = mysql.connector.connect(host="localhost",
                                                  user="root",
                                                  password="rootpass",
                                                  database="all2")      
                    cur = con.cursor()

                    #get user entries
                    user_id= self.userid_entry.get()
                    level= self.studylevel.get()
                    year= self.studyyear.get()
                    school= self.studysch.get()
                    program= self.studyprog.get()
                    semester= self.studysem.get()
                    subject1= self.studysubj1.get()
                    subject2= self.studysubj2.get()
                    subject3= self.studysubj3.get()
                    subject4= self.studysubj4.get()

                    insert_subjectrecord = ("INSERT INTO usersubjects(user_id, level, year, school, program, semester, subject1, subject2, subject3, subject4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
                    data= (user_id, level, year, school, program, semester, subject1, subject2, subject3, subject4)
                    cur.execute(insert_subjectrecord,data)

                    con.commit()
                    con.close()
                    messagebox.showinfo('Register', 'Subjects Registered Successfully!')
                    controller.show_frame(Homepage)

                except Exception as ep:
                    messagebox.showerror('', ep)
            else:
                messagebox.showerror('Error', warn)

        #register courses frame
        self.regcourses_frame = Frame(self, bd=2, bg='salmon',relief=SOLID, padx=10, pady=-1000)
        Label(self.regcourses_frame, text="ID", bg='salmon',font=f).grid(row=0, column=0, sticky=W, pady=10, padx=10)
        Label(self.regcourses_frame, text="Level", bg='salmon',font=f).grid(row=1, column=0, sticky=W, pady=10, padx=10)
        Label(self.regcourses_frame, text="Year", bg='salmon',font=f).grid(row=2, column=0, sticky=W, pady=10, padx=10)
        Label(self.regcourses_frame,text="School",bg='salmon',font=f).grid(row=3, column=0, sticky =W, pady=10, padx=10)
        Label(self.regcourses_frame, text="Program", bg='salmon',font=f).grid(row=4, column=0, sticky=W, pady=10, padx=10)
        Label(self.regcourses_frame, text="Semester", bg='salmon',font=f ).grid(row=5, column=0, sticky=W, pady=10)
        Label(self.regcourses_frame, text="Subjects", bg='salmon',font=f ).grid(row=6, column=0, sticky=W, pady=10)
        
        
        
        #default values for optionmenus
        self.level_var=StringVar()
        self.level_var.set(level[0])
        self.year_var=StringVar()
        self.year_var.set(year[0])
        self.school_var=StringVar()
        self.school_var.set(school[0])
        self.program_var=StringVar()
        self.program_var.set(program[0])
        self.semester_var=StringVar()
        self.semester_var.set(semester[0])
        self.subject1_var=StringVar()
        self.subject1_var.set('Select')
        self.subject2_var=StringVar()
        self.subject2_var.set('Select')
        self.subject3_var=StringVar()
        self.subject3_var.set('Select')
        self.subject4_var=StringVar()
        self.subject4_var.set('Select')

        #widgets
        self.userid_entry = Entry(self.regcourses_frame, font=f)
        self.studylevel = ttk.Combobox(self.regcourses_frame, textvariable = self.level_var, values=level, state='readonly',  width=20, font=f)
        self.studyyear = ttk.Combobox(self.regcourses_frame,textvariable = self.year_var, values=year, state='readonly', width=20, font=f)
        self.studysch = ttk.Combobox(self.regcourses_frame, textvariable = self.school_var, values=school, state='readonly', width=20, font=f)
        self.studyprog = ttk.Combobox(self.regcourses_frame,textvariable = self.program_var, values=program, state='readonly', width=20, font=f)
        self.studysem = ttk.Combobox(self.regcourses_frame, textvariable = self.semester_var, values=semester, state='readonly', width=20, font=f)
        self.studysubj1 = ttk.Combobox(self.regcourses_frame,textvariable = self.subject1_var, values=subjects, state='readonly', width=20, font=f)
        self.studysubj2 = ttk.Combobox(self.regcourses_frame,textvariable = self.subject2_var, values=subjects, state='readonly', width=20, font=f)
        self.studysubj3 = ttk.Combobox(self.regcourses_frame,textvariable = self.subject3_var, values=subjects, state='readonly', width=20, font=f)
        self.studysubj4 = ttk.Combobox(self.regcourses_frame,textvariable = self.subject4_var, values=subjects, state='readonly', width=20, font=f)
        self.register_btn = Button(self.regcourses_frame, width=15, text='Register', font=f, relief=SOLID,cursor='hand2', command=insert_subjrecord )
        
        
        #remove blue highlight after selection in combobox
        self.studylevel.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
        self.studyyear.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
        self.studysch.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
        self.studyprog.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
        self.studysem.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
        self.studysubj1.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
        self.studysubj2.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
        self.studysubj3.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())
        self.studysubj4.bind("<<ComboboxSelected>>",lambda e: self.regcourses_frame.focus())

        #widgets placement
        self.userid_entry.grid(row=0, column=1, pady=10, padx=20)
        self.studylevel.grid(row=1, column=1, pady=10, padx=20)
        self.studyyear.grid(row=2, column=1, pady=10, padx=20)
        self.studysch.grid(row=3, column=1, pady=10, padx=20)
        self.studyprog.grid(row=4, column=1, pady=10, padx=20)
        self.studysem.grid(row=5, column=1, pady=10, padx=20)
        self.studysubj1.grid(row=6, column=1, pady=10, padx=20)
        self.studysubj2.grid(row=7, column=1, pady=10, padx=20)
        self.studysubj3.grid(row=8, column=1, pady=10, padx=20)
        self.studysubj4.grid(row=9, column=1, pady=10, padx=20)
        self.register_btn.grid(row=10, column=1, pady=10, padx=20)
        self.regcourses_frame.place(x=75, y=210)


class StudentsView(tk.Frame):
    def __init__(self,parent=None, controller=None, name=None):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.name=name
        self.parent=parent

        #ui_bg and clock and logout btn
        ui_bg(self, 'images/Slide5.png')
        clockdate(self)
        view_user(self,Homepage, controller)
        log_out_btn(self, Loginpage, controller)
        admin_btns(self, StudentsView, BooksView, QuizAdmin, ChatAdmin, CourseMaterials, AdminAppointments,controller)

        self.show_students_frame=Frame(self, bg=bgc)
        self.show_students_frame.place(x=40, y=155)

        #student view label
        student_view_label=Label(self.show_students_frame, text='Student View', font=('Arial', 20, 'bold'), bg=bgc, fg='black')
        student_view_label.pack(pady=10)

        #show students treeview
        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', font=f)
        style.configure('Treeview', font=f2)

        self.tree_frame=Frame(self.show_students_frame)
        self.tree_frame.pack(pady=10)

        tree_scroll=Scrollbar(self.tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        my_tree=ttk.Treeview(self.tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended', height=7)
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

        #edit student record frame
        self.edit_frame=Frame(self, bd=2, relief=SOLID, bg=bgc)
        self.edit_frame.place(x=100, y=535)
        #entry boxes
        self.name_lbl= Label(self.edit_frame, text='Name', font=f3, bg=bgc)
        self.name_lbl.grid(row=0, column=0, sticky=W, pady=10, padx=10)
        self.name_entry= Entry(self.edit_frame, font=f3, width=20)
        self.name_entry.grid(row=0, column=1, pady=10, padx=10)

        self.id_lbl= Label(self.edit_frame, text='Student ID', font=f3, bg=bgc)
        self.id_lbl.grid(row=1, column=0, sticky=W, pady=10, padx=5)
        self.id_entry= Entry(self.edit_frame, font=f, width=20)
        self.id_entry.grid(row=1, column=1, pady=10, padx=10)

        self.email_lbl= Label(self.edit_frame, text='Email', font=f3, bg=bgc)
        self.email_lbl.grid(row=2, column=0, sticky=W, pady=10, padx=10)
        self.email_entry= Entry(self.edit_frame, font=f3, width=20)
        self.email_entry.grid(row=2, column=1, pady=10, padx=10)

        self.subj1_lbl= Label(self.edit_frame, text='Subject 1', font=f3, bg=bgc)
        self.subj1_lbl.grid(row=0, column=4, sticky=W, pady=10, padx=10)
        self.subj1_entry= ttk.Combobox(self.edit_frame, values=subjects,  width=20, font=f3)
        self.subj1_entry.grid(row=0, column=5, pady=10, padx=10)

        self.subj2_lbl= Label(self.edit_frame, text='Subject 2', font=f3, bg=bgc)
        self.subj2_lbl.grid(row=1, column=4, sticky=W, pady=10, padx=10)
        self.subj2_entry= ttk.Combobox(self.edit_frame, values=subjects,  width=20, font=f3)
        self.subj2_entry.grid(row=1, column=5, pady=10, padx=10)

        self.subj3_lbl= Label(self.edit_frame, text='Subject 3', font=f3, bg=bgc)
        self.subj3_lbl.grid(row=2, column=4, sticky=W, pady=10, padx=10)
        self.subj3_entry= ttk.Combobox(self.edit_frame, values=subjects,  width=20, font=f3)
        self.subj3_entry.grid(row=2, column=5, pady=10, padx=10)

        self.subj4_lbl= Label(self.edit_frame, text='Subject 4', font=f3, bg=bgc)
        self.subj4_lbl.grid(row=0, column=6, sticky=W, pady=10, padx=10)
        self.subj4_entry= ttk.Combobox(self.edit_frame, values=subjects,  width=20, font=f3)
        self.subj4_entry.grid(row=0, column=7, pady=10, padx=10)

        def show_stud_record(e):
            self.delete_btn.config(state='normal')
            self.update_btn.config(state='normal')

            #clear entries
            self.name_entry.delete(0, END)
            self.id_entry.config(state='normal')
            self.id_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.subj1_entry.set('')
            self.subj2_entry.set('')
            self.subj3_entry.set('')
            self.subj4_entry.set('')

            #grab record number and values
            selected=my_tree.focus()
            values=my_tree.item(selected, 'values')

            #output to entry boxes
            self.name_entry.insert(0, values[0])
            self.id_entry.insert(0, values[1])
            self.id_entry.config(state='disabled')
            self.email_entry.insert(0, values[2])
            self.subj1_entry.insert(0, values[3])
            self.subj2_entry.insert(0, values[4])
            self.subj3_entry.insert(0, values[5])
            self.subj4_entry.insert(0, values[6])
        
        #update student records
        def update_stud_record():
            selected=my_tree.focus()
            my_tree.item(selected, text='', values=(self.name_entry.get(), self.id_entry.get(), self.email_entry.get(), self.subj1_entry.get(), self.subj2_entry.get(), self.subj3_entry.get(), self.subj4_entry.get()))
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          password="rootpass",
                                          database="all2")      
            cur = con.cursor()
            cur.execute("UPDATE userdata, usersubjects SET userdata.name=%s, userdata.user_id=%s, userdata.email=%s, usersubjects.subject1=%s, usersubjects.subject2=%s, usersubjects.subject3=%s, usersubjects.subject4=%s WHERE usersubjects.user_id = userdata.user_id AND userdata.user_id = %s", (self.name_entry.get(), self.id_entry.get(), self.email_entry.get(), self.subj1_entry.get(), self.subj2_entry.get(), self.subj3_entry.get(), self.subj4_entry.get(), self.id_entry.get()))
            con.commit()
            con.close()

            #clear entries
            self.name_entry.delete(0, END)
            self.id_entry.config(state='normal')
            self.id_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.subj1_entry.delete(0, END)
            self.subj2_entry.delete(0, END)
            self.subj3_entry.delete(0, END)
            self.subj4_entry.delete(0, END)
        
        #Update student record btn
        self.update_btn=Button(self.edit_frame, text='Update Record', font=f, width=15, relief=SOLID, cursor='hand2', command=update_stud_record, state=DISABLED)
        self.update_btn.grid(row=1, column=6, pady=10, padx=10, columnspan=2)

        #delete student record
        def delete_stud_record():
            x=my_tree.selection()[0]
            my_tree.delete(x)
            con = mysql.connector.connect(host="localhost", 
                                          user="root",
                                          password="rootpass", 
                                          database="all2")
            cur = con.cursor()
            cur.execute("DELETE a, b FROM userdata a JOIN usersubjects b ON a.user_id = b.user_id WHERE a.user_id = %s", (self.id_entry.get(),))
            con.commit()
            con.close()

            #clear entries
            self.name_entry.delete(0, END)
            self.id_entry.config(state='normal')
            self.id_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.subj1_entry.delete(0, END)
            self.subj2_entry.delete(0, END)
            self.subj3_entry.delete(0, END)
            self.subj4_entry.delete(0, END)

        #delete student record btn
        self.delete_btn=Button(self.edit_frame, text='Delete Record', font=f, width=15, relief=SOLID, cursor='hand2', command=delete_stud_record, state=DISABLED)
        self.delete_btn.grid(row=2, column=6, pady=10, padx=10, columnspan=2)

        my_tree.bind('<ButtonRelease-1>', show_stud_record)

        #search bar for student records
        self.searchstud_lbl=Label(self, text='Search', font=f3, bg=bgc)
        self.searchstud_lbl.place(x=900, y=168)
        self.searchstud_entry=Entry(self, font=f3, width=18)
        self.searchstud_entry.place(x=975, y=168)
        self.searchstud_icon=Image.open('images\search.png')
        self.searchstud_icon=self.searchstud_icon.resize((25, 25))
        self.searchstud_icon=ImageTk.PhotoImage(self.searchstud_icon)

        def search_stud():
            if self.searchstud_entry !='':
                con = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="rootpass",
                                    database="all2")
                cur = con.cursor()
                my_tree.delete(*my_tree.get_children())
                s_set=cur.execute("SELECT a.name, a.user_id, a.email, b.subject1, b.subject2, b.subject3, b.subject4 FROM userdata a, usersubjects b WHERE a.user_id = b.user_id AND a.name LIKE %s", ('%'+(self.searchstud_entry.get())+'%',))
                s_set=cur.fetchall()
                for rec in s_set:
                    my_tree.insert('', tk.END, values=(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6]))
                con.commit()
                con.close()
            else:
                my_tree.delete(*my_tree.get_children())
                s_set=cur.execute("SELECT a.name, a.user_id, a.email, b.subject1, b.subject2, b.subject3, b.subject4 FROM userdata a, usersubjects b WHERE a.usertype='Student' AND a.user_id = b.user_id;")
                s_set=cur.fetchall()
                for rec in s_set:
                    my_tree.insert("", tk.END, values=row)
                con.commit()
                con.close()
        
        self.searchstud_btn=Button(self,image=self.searchstud_icon, cursor='hand2',command=search_stud)
        self.searchstud_btn.place(x=1195, y=168)
            

#add/delete /view books
class BooksView(tk.Frame):
    def __init__(self,parent=None, controller=None, name=None):
        global show_students_frame, show_books_frame
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.name=name
        self.parent=parent

        #ui_bg and clock and logout btn
        ui_bg(self, 'images/Slide5.png')
        clockdate(self)
        view_user(self,Homepage, controller)
        log_out_btn(self, Loginpage, controller)
        admin_btns(self, StudentsView, BooksView, QuizAdmin, ChatAdmin, CourseMaterials, AdminAppointments,controller)


        self.show_books_frame=Frame(self, bg=bgc)
        self.show_books_frame.place(x=40, y=155)

        
        #upload book pdf file path
        def upload_bookfile():
            self.bookfile_path=filedialog.askopenfilename(title='Select Book File', filetypes=(('PDF Files', '*.pdf'), ('All Files', '*.*')))
            #change btn name to uploaded
            if self.bookfile_path != "":
                self.bookfile_entry.config(text='Uploaded')

        #upload book cover image
        def upload_bookcover():
            self.bookcover_path=filedialog.askopenfilename( title='Select Book Cover', filetypes=(('PNG Files', '*.png'), ('All Files', '*.*')))
            #change btn name to uploaded
            if self.bookcover_path != "":
                self.bookcover_entry.config(text='Uploaded')

        #book view label
        self.book_view_lbl=Label(self.show_books_frame, text='Book View', font=('Arial', 20, 'bold'), bg=bgc, fg='black')
        self.book_view_lbl.grid(row=0, column=1, columnspan=2)

        #book image frame
        self.book_img_frame=Frame(self.show_books_frame, bg=bgc)
        self.book_img_frame.grid(row=1, column=0)
        self.book_img_frame.config(width=115, height=165)

        #show books treeview
        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', font=f)
        style.configure('Treeview', font=f2)
        style.configure('Treeview', rowheight=35)
        ttk.Style().configure("Custom.Treeview", rowheight=127) 

        tree_frame=Frame(self.show_books_frame)
        tree_frame.grid(row=1, column=1)

        tree_scroll=Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        my_tree=ttk.Treeview(tree_frame, style='Custom.Treeview', yscrollcommand=tree_scroll.set, selectmode='browse', height=2)
        my_tree.pack()

        tree_scroll.config(command=my_tree.yview)

        my_tree['columns']= ('ID', 'Book Name', 'Category', 'File')

        #format columns
        my_tree.column('#0', width=0, stretch=NO)
        my_tree.column('ID', width=60, anchor=CENTER, stretch=NO)
        my_tree.column('Book Name', width=210, anchor=CENTER, stretch=NO)
        my_tree.column('Category', width=145, anchor=CENTER, stretch=NO)
        my_tree.column('File', width=225, anchor=CENTER, stretch=NO)


        #column headings
        my_tree.heading('#0', text='', anchor=CENTER)
        my_tree.heading('ID', text='ID', anchor=CENTER)
        my_tree.heading('Book Name', text='Book Name', anchor=CENTER)
        my_tree.heading('Category', text='Category', anchor=CENTER)
        my_tree.heading('File', text='File', anchor=CENTER)


        #pdf viewer for books
        self.pdfview_frame=Frame(self, bg=bgc, width=485, height=565, bd=2, relief=SOLID)
        self.pdfview_frame.place(x=850, y=190)

        #zoom spinbox selector
        self.zoom_lbl=Label(self, text='Zoom', font=f2, bg=bgc)
        self.zoom_lbl.place(x=1235, y=150)
        zoom_var=IntVar()
        zoom_var.set(72)
        self.zoom_spin=Spinbox(self, textvariable= zoom_var, from_=20, to=500,increment=5, width=3, font=f3)
        self.zoom_spin.place(x=1285, y=150)


        #show records and view book pdf when pressing row
        def show_book_record(e):
            self.deletebook_btn.config(state=NORMAL)
            #clear entries
            self.bookid_entry.delete(0, END)
            self.bookname_entry.delete(0, END)
            self.bookcat_entry.delete(0, END)
            self.bookfile_entry.config(text='Upload File')
            self.bookcover_entry.config(text='Upload Cover')
            # self.pdf_viewer_label.place(x=1035, y=175)
            # self.clickpdf_lbl.destroy()
            


            #grab record number and values
            selected=my_tree.focus()
            values=my_tree.item(selected, 'values')

            #get data from database
            con = mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="rootpass",
                                        database="all2")
            cur = con.cursor()
            #get image from db
            data=cur.execute("SELECT bookcover,bookfile FROM books WHERE idbooks=%s", (values[0],))
            data= cur.fetchone()

            #show image upon clicking treeview row
            if data :
                self.book_img = Image.open(data[0])
                self.book_img = self.book_img.resize((115,165))
                self.book_img = ImageTk.PhotoImage(self.book_img)
                self.book_img_lbl=Label(self.book_img_frame, image=self.book_img, bg=bgc)
                self.book_img_lbl.grid(row=0,column=0)

                #showpdf
                self.bookview_pdf = pdf.ShowPdf()
                self.bookview_pdf.img_object_li.clear() #clear old pdf inside the frame
                self.bookview=self.bookview_pdf.pdf_view(self.pdfview_frame, bar=False, pdf_location=data[1], width=60, height=34, zoomDPI=zoom_var.get())
                self.bookview.grid(row=1, column=0, columnspan=3)
                
   

            #output to entry boxes
            self.bookid_entry.insert(0, values[0])
            self.bookname_entry.insert(0, values[1])
            self.bookcat_entry.insert(0, values[2])


        #get data from database
        con = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="rootpass",
                                    database="all2")
        cur = con.cursor()
        r_set=cur.execute("SELECT bookcover, idbooks, bookname, bookcategory, bookfile from books;")
        r_set=cur.fetchall()
        for row in r_set:
            wraptxt1= textwrap.fill(row[2], width=20)
            wraptxt2= textwrap.fill(row[4], width=22)
            my_tree.insert("", tk.END, values=(row[1], wraptxt1, row[3], wraptxt2))



        cur.execute('''CREATE TABLE IF NOT EXISTS books( idbooks INT AUTO_INCREMENT PRIMARY KEY, 
                                                         bookname varchar(200) NOT NULL,
                                                         bookcategory varchar(45) NOT NULL, 
                                                         bookfile longtext NOT NULL, 
                                                         bookcover longtext NOT NULL) ''')
        con.commit()
        #Add books
        def insert_books():
            check_counter=0
            warn=" "
            #check if entries are empty
            if self.bookname_entry.get() == "":
                warn = 'Please enter Book Name.'
            else:
                check_counter += 1

            if self.bookcat_entry.get() == "":
                warn = 'Please enter Book Category.'
            else:
                check_counter += 1

            if check_counter == 2:
                try:
                    #get user entries
                    book_id= self.bookid_entry.get()
                    book_name= self.bookname_entry.get()
                    book_cat= self.bookcat_entry.get()
                    book_file= self.bookfile_path
                    book_cover= self.bookcover_path

                    insert_bookrecord = ("INSERT INTO books(idbooks, bookname, bookcategory, bookfile, bookcover) VALUES (%s,%s,%s,%s,%s);")
                    data= (book_id, book_name, book_cat, book_file, book_cover)
                    cur.execute(insert_bookrecord,data)

                    con.commit()
                    con.close()
                    messagebox.showinfo('Register', 'Book Added Successfully!')
                    wraptxt1= textwrap.fill(book_name, width=20)
                    wraptxt2= textwrap.fill(book_file, width=22)
                    my_tree.insert("", tk.END, values=(book_id, wraptxt1, book_cat, wraptxt2))

                    #clear entries
                    self.bookid_entry.delete(0, END)
                    self.bookname_entry.delete(0, END)
                    self.bookcat_entry.delete(0, END)
        

                except Exception as ep:
                    messagebox.showerror('', ep)
            else:
                messagebox.showerror('Error', warn)


        #add delete books frame
        self.booksrec_frame=Frame(self, bg=bgc, bd=2, relief=SOLID)  
        self.booksrec_frame.place(x=55, y=500)

        bookcat=['Maths', 'Computer Science', 'Design']

        #entry boxes
        self.bookid_lbl= Label(self.booksrec_frame, text='Book ID', font=f3, bg=bgc)
        self.bookid_lbl.grid(row=0, column=0, sticky=W, pady=10, padx=10)
        self.bookid_entry= Entry(self.booksrec_frame, font=f3, width=10)
        self.bookid_entry.grid(row=0, column=1, pady=10, padx=10)

        self.bookname_lbl= Label(self.booksrec_frame, text='Book Name', font=f3, bg=bgc)
        self.bookname_lbl.grid(row=1, column=0, sticky=W, pady=10, padx=10)
        self.bookname_entry= Entry(self.booksrec_frame, font=f3, width=18)
        self.bookname_entry.grid(row=1, column=1, pady=10, padx=10)

        self.bookcat_lbl= Label(self.booksrec_frame, text='Book Category', font=f3, bg=bgc)
        self.bookcat_lbl.grid(row=2, column=0, sticky=W, pady=10, padx=10)
        self.bookcat_entry= ttk.Combobox(self.booksrec_frame, font=f3, values=bookcat, width=18)
        self.bookcat_entry.grid(row=2, column=1, pady=10, padx=10)


        self.bookfile_lbl= Label(self.booksrec_frame, text='Book File', font=f3, bg=bgc)
        self.bookfile_lbl.grid(row=0, column=2, sticky=W, pady=10, padx=10)
        self.bookfile_entry= Button(self.booksrec_frame, text='Upload File',font=f, width=12, cursor='hand2', command=upload_bookfile)
        self.bookfile_entry.grid(row=0, column=3, pady=10, padx=10)

        self.bookcover_lbl= Label(self.booksrec_frame, text='Book Cover', font=f3, bg=bgc)
        self.bookcover_lbl.grid(row=1, column=2, sticky=W, pady=10, padx=10)
        self.bookcover_entry= Button(self.booksrec_frame,text='Upload Cover', font=f, width=12, cursor='hand2', command=upload_bookcover)
        self.bookcover_entry.grid(row=1, column=3, pady=10, padx=10)

        my_tree.bind('<ButtonRelease-1>', show_book_record)

        def del_book_record():
            x=my_tree.selection()[0]
            my_tree.delete(x)

            con = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="rootpass",
                                    database="all2")
            cur = con.cursor()
            cur.execute('''DELETE FROM books WHERE idbooks=%s''', (self.bookid_entry.get(),))
            con.commit()
            con.close()

            #clear entries
            self.bookid_entry.delete(0, END)
            self.bookname_entry.delete(0, END)
            self.bookcat_entry.delete(0, END)
            self.bookfile_entry.config(text='Upload File')
            self.bookcover_entry.config(text='Upload Cover')
            
            #message box to show delete success
            messagebox.showinfo('Delete', 'Book Deleted Successfully!')


        self.addbook_btn= Button(self.booksrec_frame, text='Add Book', font=f3, relief=SOLID, cursor='hand2', command=insert_books)
        self.addbook_btn.grid(row=4, column=1, sticky=W, pady=10, padx=65)

        self.deletebook_btn= Button(self.booksrec_frame, text='Delete Book', font=f3, relief=SOLID ,cursor='hand2',command=del_book_record, state=DISABLED)
        self.deletebook_btn.grid(row=4, column=2, sticky=W, pady=10, padx=10)

        

class QuizAdmin(tk.Frame):
    def __init__(self,parent=None, controller=None, name=None):
        global show_students_frame, show_books_frame
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.name=name
        self.parent=parent

        #ui_bg and clock and logout btn
        ui_bg(self, 'images/Slide5.png')
        clockdate(self)
        view_user(self,Homepage, controller)
        log_out_btn(self, Loginpage, controller)
        admin_btns(self, StudentsView, BooksView, QuizAdmin, ChatAdmin, CourseMaterials, AdminAppointments,controller)

        #quiz admin label
        quiz_admin_label=Label(self, text='Quiz Admin', font=('Arial', 20, 'bold'), bg=bgc, fg='black')
        quiz_admin_label.place(x=40, y=155)

        #quiz subject selection frame
        self.quiz_subjsel_frame=Frame(self, bg=bgc, width=800, height=100)
        self.quiz_subjsel_frame.place(x=40, y=200)

        self.quiz_subjsel_lbl=Label(self.quiz_subjsel_frame, text='Subject', font=f3, bg=bgc)
        self.quiz_subjsel_lbl.grid(row=0, column=0, pady=10, padx=10)

        self.quiz_subjsel=ttk.Combobox(self.quiz_subjsel_frame, font=f3, width=26, values=['Select', 'Computer Architecture & Networks'], state='readonly')
        self.quiz_subjsel.current(1)
        self.quiz_subjsel.grid(row=0, column=1, pady=10)

        #quiz treeview list
        self.quiztv_frame=Frame(self, bg=bgc)
        self.quiztv_frame.place(x=40, y=255)

        #quiz treeview
        self.quiz_tv_scroll=Scrollbar(self.quiztv_frame)
        self.quiz_tv_scroll.pack(side=RIGHT, fill=Y)

        style=ttk.Style()
        style.configure('Quiz.Treeview', font=f)

        self.quiz_tv=ttk.Treeview(self.quiztv_frame, yscrollcommand=self.quiz_tv_scroll.set, style='Quiz.Treeview',height=10)
        self.quiz_tv.pack()

        self.quiz_tv_scroll.config(command=self.quiz_tv.yview)

        self.quiz_tv.column('#0', width=435, minwidth=435)
        self.quiz_tv.heading('#0', text='Quiz Chapters', anchor=W)

        #show distinct chapters in treeview
        def show_quizchp(e):
            if self.quiz_subjsel.get()=='Select':
                #show blank treeview
                self.quiz_tv.delete(*self.quiz_tv.get_children())

            else:
                #connect to db
                con = mysql.connector.connect(host='localhost', 
                                            user='root', 
                                            password='rootpass', 
                                            database='all2')
                cur = con.cursor()
                s_set=cur.execute('''SELECT DISTINCT chap_name FROM quiz WHERE subj_name=%s''', (self.quiz_subjsel.get(),))
                s_set=cur.fetchall()
                for row in s_set:
                    self.quiz_tv.insert('',tk.END, text='Chapter ' +(row[0]))
                con.commit()
                con.close()
        
        #show quiz chapters in treeview first
        show_quizchp(e=None)
        self.quiz_subjsel.bind('<<ComboboxSelected>>', show_quizchp)
        
        #quiz questions frame and add quiz frame func prototypes
        self.quizques_frame=Frame(self, bg='white',  width=720, height=420, relief=SOLID, bd=2)
        self.addquiz_frame=Frame(self, bg=bgc, width=450, height=300, relief=SOLID, bd=2)


        #fix frame row and column size
        self.quizques_frame.rowconfigure(1, weight=1)
        self.quizques_frame.columnconfigure(0, weight=1)
        self.quizques_frame.columnconfigure(1, weight=1)

        #radiobutton selected option variable definition
        selected_option=StringVar()
        
        #quiz chapter title, 1 question, 4 options, previous, next btns
        self.quiz_chapter_title=Label(self.quizques_frame, text=empty_text, font=('Arial', 19,'bold'), bg='white')   
        self.quiz_chapter_title.grid(row=0, column=0, pady=10, padx=10, columnspan=3)

        self.quiz_question=Label(self.quizques_frame, text=empty_text, font=f3, bg='white', wraplength=655)
        self.quiz_question.grid(row=1, column=0, pady=10, padx=10, columnspan=3)

        self.quiz_option1=Radiobutton(self.quizques_frame, text=empty_text, font=f, bg='white', cursor='hand2', variable=selected_option, value='A', tristatevalue=0)
        self.quiz_option1.grid(row=2, column=1, pady=10, padx=10, sticky=W, columnspan=3)

        self.quiz_option2=Radiobutton(self.quizques_frame, text=empty_text, font=f, bg='white', cursor='hand2', variable=selected_option, value='B', tristatevalue=0)
        self.quiz_option2.grid(row=3, column=1, pady=10, padx=10, sticky=W, columnspan=3)


        self.quiz_option3=Radiobutton(self.quizques_frame, text=empty_text, font=f, bg='white',  cursor='hand2', variable=selected_option, value='C', tristatevalue=0)
        self.quiz_option3.grid(row=4, column=1, pady=10, padx=10, sticky=W, columnspan=3)

        self.quiz_option4=Radiobutton(self.quizques_frame, text=empty_text, font=f, bg='white', cursor='hand2', variable=selected_option, value='D', tristatevalue=0)
        self.quiz_option4.grid(row=5, column=1, pady=10, padx=10, sticky=W, columnspan=3)


        #next question
        def next_ques():
            #count score first
            self.user_ans= selected_option.get()
            selected_option.set(None)

            if self.ques_num < (len(self.q_set)-1):
                self.ques_num+=1
            if self.ques_num == (len(self.q_set)-1):
                # self.quiz_next_btn.config(state=DISABLED)
                self.quiz_next_btn.config(text='Done')
                self.quiz_next_btn.config(command=quiz_result)
            else:
                self.quiz_next_btn.config(state=NORMAL)
                self.quiz_prev_btn.config(state=NORMAL)
            

            self.quiz_chapter_title.config(text=self.values)
            self.quiz_question.config(text='Question '+ str(self.ques_num+1) +': '+self.q_set[self.ques_num][0])
            self.quiz_option1.config(text=self.q_set[self.ques_num][1])
            self.quiz_option2.config(text=self.q_set[self.ques_num][2])
            self.quiz_option3.config(text=self.q_set[self.ques_num][3])
            self.quiz_option4.config(text=self.q_set[self.ques_num][4])
            self.quiz_ques_num.config(text='Question '+str(self.ques_num+1)+'/'+str(len(self.q_set)))


        def prev_ques():
            selected_option.set(None)
            if self.ques_num > 0:
                    self.ques_num -= 1
            if self.ques_num == 0:
                self.quiz_prev_btn.config(state=DISABLED)
            else:
                self.quiz_prev_btn.config(state=NORMAL)
                self.quiz_next_btn.config(state=NORMAL)
                self.quiz_next_btn.config(text='Next')
                self.quiz_next_btn.config(command=next_ques)

            self.quiz_chapter_title.config(text=self.values)
            self.quiz_question.config(text='Question '+ str(self.ques_num+1) +': '+self.q_set[self.ques_num][0])
            self.quiz_option1.config(text=self.q_set[self.ques_num][1])
            self.quiz_option2.config(text=self.q_set[self.ques_num][2])
            self.quiz_option3.config(text=self.q_set[self.ques_num][3])
            self.quiz_option4.config(text=self.q_set[self.ques_num][4])
            self.quiz_ques_num.config(text='Question '+str(self.ques_num+1)+'/'+str(len(self.q_set)))


        #bind event: user selects from treeview the quiz chapter, then quiz is shown in quiz frame, for loop  quiz questions from db, prev next btn
        #show quiz questions in quiz frame
        def show_quizques(e):
            selected=self.quiz_tv.focus()
            if selected:
                self.values=self.quiz_tv.item(selected, 'text')
                self.quizques_frame.place(x=583, y=240)
                self.quizques_frame.grid_propagate(False)
                self.addquiz_frame.place_forget()
                #connect to db
                con = mysql.connector.connect(host='localhost', 
                                            user='root', 
                                            password='rootpass', 
                                            database='all2')
                cur = con.cursor()
                self.q_set=cur.execute('''SELECT ques_title, opA, opB, opC, opD, correct_op FROM quiz WHERE chap_name=%s''', (self.values.replace("Chapter ", ""),))
                self.q_set=cur.fetchall()


                self.ques_num=0
                self.quiz_chapter_title.config(text=self.values)
                self.quiz_question.config(text='Question '+ str(self.ques_num+1) +': '+self.q_set[self.ques_num][0])
                self.quiz_option1.config(text=self.q_set[self.ques_num][1])
                self.quiz_option2.config(text=self.q_set[self.ques_num][2])
                self.quiz_option3.config(text=self.q_set[self.ques_num][3])
                self.quiz_option4.config(text=self.q_set[self.ques_num][4])
                con.commit()
            
            else: #show default
                self.values=self.quiz_tv.item(self.quiz_tv.get_children()[0], 'text')
                self.quizques_frame.place(x=583, y=240)
                self.quizques_frame.grid_propagate(False)

                con = mysql.connector.connect(host='localhost', 
                                            user='root', 
                                            password='rootpass', 
                                            database='all2')

                cur = con.cursor()
                self.q_set=cur.execute('''SELECT ques_title, opA, opB, opC, opD, correct_op FROM quiz WHERE chap_name=%s''', (self.values.replace("Chapter ", ""),))
                self.q_set=cur.fetchall()

                self.ques_num=0
                self.quiz_chapter_title.config(text=self.values)
                self.quiz_question.config(text='Question '+ str(self.ques_num+1) +': '+self.q_set[self.ques_num][0])
                self.quiz_option1.config(text=self.q_set[self.ques_num][1])
                self.quiz_option2.config(text=self.q_set[self.ques_num][2])
                self.quiz_option3.config(text=self.q_set[self.ques_num][3])
                self.quiz_option4.config(text=self.q_set[self.ques_num][4])
                con.commit()

            self.quiz_prev_btn=Button(self.quizques_frame, text='Previous', font=f3, relief=SOLID, cursor='hand2', width=10, command=prev_ques, state=DISABLED)
            self.quiz_prev_btn.grid(row=6, column=0, pady=10, padx=10, sticky=W)

            self.quiz_next_btn=Button(self.quizques_frame, text='Next', font=f3, relief=SOLID, cursor='hand2', width=10, command=next_ques)
            self.quiz_next_btn.grid(row=6, column=2, pady=10, padx=10)

            #show current question 1/5
            self.quiz_ques_num=Label(self.quizques_frame, text='Question '+str(self.ques_num+1)+'/'+str(len(self.q_set)), font=f3, bg='white')
            self.quiz_ques_num.grid(row=6, column=1, pady=10, padx=10, sticky=W)

        #show quiz by default
        show_quizques(e=None)
        self.quiz_tv.bind('<ButtonRelease-1>', show_quizques)

         

        self.quiz_score= 0
        ##show quiz results to user, show score, true false and percentage in messagebox
        def quiz_result():
            self.user_ans= selected_option.get()

            score = str(self.quiz_score)+'/'+str(len(self.q_set))

            tk.messagebox.showinfo('Quiz Result', 'Your score is: '+score+'\n')
            #reset quiz
            self.quiz_score=0
            self.ques_num=0
            self.quiz_chapter_title.config(text=self.values)
            self.quiz_question.config(text='Question '+ str(self.ques_num+1) +': '+self.q_set[self.ques_num][0])
            self.quiz_option1.config(text=self.q_set[self.ques_num][1])
            self.quiz_option2.config(text=self.q_set[self.ques_num][2])
            self.quiz_option3.config(text=self.q_set[self.ques_num][3])
            self.quiz_option4.config(text=self.q_set[self.ques_num][4])
            self.quiz_next_btn.config(text='Next')
            self.quiz_next_btn.config(command=next_ques)
            self.quiz_prev_btn.config(state=DISABLED)
            self.quiz_ques_num.config(text='Question '+str(self.ques_num+1)+'/'+str(len(self.q_set)))

        #add quiz frame
        def add_quiz_frame():
            self.addquiz_frame.place(x=685, y=153)
            self.quizques_frame.place_forget()

            #connect to db
            con = mysql.connector.connect(host='localhost', 
                                            user='root', 
                                            password='rootpass', 
                                            database='all2')
            cur = con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS quiz(idquiz INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                                                            subj_name VARCHAR(45) NOT NULL,
                                                            chap_name VARCHAR(85) NOT NULL,
                                                            ques_title VARCHAR(105) NOT NULL,
                                                            opA VARCHAR(45) NOT NULL,
                                                            opB VARCHAR(45) NOT NULL,
                                                            opC VARCHAR(45) NOT NULL,
                                                            opD VARCHAR(45) NOT NULL,
                                                            correct_op VARCHAR(45) NOT NULL)''')
            con.commit()


            self.addquizlabel=Label(self.addquiz_frame, text='Add Quiz', font=('Arial', 20, 'bold'), bg=bgc )
            self.addquizlabel.grid(row=0, column=0, pady=10, padx=10, columnspan=2, sticky=E)

            self.subjsel_label=Label(self.addquiz_frame, text='Subject', font=f3, bg=bgc)
            self.subjsel_label.grid(row=1, column=0, pady=10, padx=10, sticky=W)

            self.subjsel_combo=ttk.Combobox(self.addquiz_frame, font=f3, width=26, values=['Select', 'Computer Architecture & Networks'], state='readonly')
            self.subjsel_combo.current(1)
            self.subjsel_combo.grid(row=1, column=1, pady=10, columnspan=2)

            self.chapter_label=Label(self.addquiz_frame, text='Chapter', font=f3, bg=bgc)
            self.chapter_label.grid(row=2, column=0, pady=10, padx=10, sticky=W)

            self.chapter_entry=Entry(self.addquiz_frame, font=f, bd=2, width=26)
            self.chapter_entry.grid(row=2, column=1, pady=10, padx=10, sticky=W, columnspan=2)

            #get no. of questions from user then for loop to create entry boxes, then add into db
            self.noq_label=Label(self.addquiz_frame, text='No. of Questions', font=f3, bg=bgc)
            self.noq_label.grid(row=3, column=0, pady=10, padx=10, sticky=W)

            self.noq_cb=ttk.Combobox(self.addquiz_frame, font=f3, values=questions, width=8, state='readonly')
            self.noq_cb.grid(row=3, column=1, pady=10, padx=10, sticky=W, columnspan=2)

            #questiontitle with question counter
            self.questitle_lbl=Label(self.addquiz_frame, text='Question', font=f3, bg=bgc)
            self.questitle_lbl.grid(row=4, column=0, pady=10, padx=10, sticky=W)

            self.questitle_entry=Text(self.addquiz_frame, font=f, bd=2, height=3,width=26, wrap=WORD)
            self.questitle_entry.grid(row=4, column=1, pady=10, padx=10, sticky=W, columnspan=2)

            self.opA_label=Label(self.addquiz_frame, text='Option A', font=f3, bg=bgc)
            self.opA_label.grid(row=5, column=0, pady=10, padx=10, sticky=W)

            self.opA_entry=Entry(self.addquiz_frame, font=f3, bd=2)
            self.opA_entry.grid(row=5, column=1, pady=10, padx=10, sticky=W, columnspan=2)

            self.opB_label=Label(self.addquiz_frame, text='Option B', font=f3, bg=bgc)
            self.opB_label.grid(row=6, column=0, pady=10, padx=10, sticky=W)

            self.opB_entry=Entry(self.addquiz_frame, font=f3, bd=2)
            self.opB_entry.grid(row=6, column=1, pady=10, padx=10, sticky=W, columnspan=2)

            self.opC_label=Label(self.addquiz_frame, text='Option C', font=f3, bg=bgc)
            self.opC_label.grid(row=7, column=0, pady=10, padx=10, sticky=W)

            self.opC_entry=Entry(self.addquiz_frame, font=f3, bd=2)
            self.opC_entry.grid(row=7, column=1, pady=10, padx=10, sticky=W, columnspan=2)

            self.opD_label=Label(self.addquiz_frame, text='Option D', font=f3, bg=bgc)
            self.opD_label.grid(row=8, column=0, pady=10, padx=10, sticky=W)

            self.opD_entry=Entry(self.addquiz_frame, font=f3, bd=2)
            self.opD_entry.grid(row=8, column=1, pady=10, padx=10, sticky=W, columnspan=2)

            self.correctop_label=Label(self.addquiz_frame, text='Correct Option', font=f3, bg=bgc)
            self.correctop_label.grid(row=9, column=0, pady=10, padx=10, sticky=W)

            self.correctop_entry=ttk.Combobox(self.addquiz_frame, font=f3, values=options, width=8, state='readonly')
            self.correctop_entry.grid(row=9, column=1, pady=10, padx=10, sticky=W, columnspan=2)


            self.ques_titles=[]
            self.opA=[]
            self.opB=[]
            self.opC=[]
            self.opD=[]
            self.correctop=[]

            def ques_cb_selected(event):
                self.ques_no=1
                self.questitle_lbl.config(text='Question '+str(self.ques_no))

            #next btn to add quiz title (if questions more than user entry then disable btn)
            def next():
                
                if self.ques_no < (int(self.noq_cb.get())):
                    self.ques_no+=1
                if self.ques_no == (int(self.noq_cb.get())):
                    self.nextques_btn.config(state=DISABLED)
                else:
                    self.nextques_btn.config(state=NORMAL)
                    self.prevques_btn.config(state=NORMAL)

                self.questitle_lbl.config(text='Question '+str(self.ques_no))
                #get entries if previously entered by user, if not then append user entry to list
                if (self.ques_no < len(self.ques_titles)) :
                    #clear entries
                    self.questitle_entry.delete('1.0', END)
                    self.opA_entry.delete(0, END)
                    self.opB_entry.delete(0, END)
                    self.opC_entry.delete(0, END)
                    self.opD_entry.delete(0, END)
                    self.correctop_entry.set('')

                    self.questitle_entry.insert(1.0, self.ques_titles[self.ques_no-1])
                    self.opA.insert(0, self.opA[self.ques_no-1])
                    self.opB.insert(0, self.opB[self.ques_no-1])
                    self.opC.insert(0, self.opC[self.ques_no-1])
                    self.opD.insert(0, self.opD[self.ques_no-1])
                    self.correctop.insert(0, self.correctop[self.ques_no-1])

                else:
                    self.ques_titles.append(self.questitle_entry.get('1.0', 'end-1c'))
                    self.opA.append(self.opA_entry.get())
                    self.opB.append(self.opB_entry.get())
                    self.opC.append(self.opC_entry.get())
                    self.opD.append(self.opD_entry.get())
                    self.correctop.append(self.correctop_entry.get())
                
                    #clear entries
                    self.questitle_entry.delete('1.0', END)
                    self.opA_entry.delete(0, END)
                    self.opB_entry.delete(0, END)
                    self.opC_entry.delete(0, END)
                    self.opD_entry.delete(0, END)
                    self.correctop_entry.set('')
                

            #previous btn 
            def previous():
                if self.ques_no > 1:
                    self.ques_no -= 1
                if self.ques_no == 1:
                    self.prevques_btn.config(state=DISABLED)
                else:
                    self.prevques_btn.config(state=NORMAL)
                    self.nextques_btn.config(state=NORMAL)
                
                self.questitle_lbl.config(text='Question '+str(self.ques_no))
                #clear entries
                self.questitle_entry.delete('1.0', END)
                self.opA_entry.delete(0, END)
                self.opB_entry.delete(0, END)
                self.opC_entry.delete(0, END)
                self.opD_entry.delete(0, END)
                self.correctop_entry.set('')

                #get entries from list
                self.questitle_entry.insert('1.0', self.ques_titles[self.ques_no-1])
                self.opA_entry.insert(0, self.opA[self.ques_no-1])
                self.opB_entry.insert(0, self.opB[self.ques_no-1])
                self.opC_entry.insert(0, self.opC[self.ques_no-1])
                self.opD_entry.insert(0, self.opD[self.ques_no-1])
                self.correctop_entry.set(self.correctop[self.ques_no-1])
            
            #bind combo selected event
            self.noq_cb.bind('<<ComboboxSelected>>', ques_cb_selected)


            #previous question btn  #if first question then disable
            self.prevques_btn=Button(self.addquiz_frame, text='Previous', font=f, relief=SOLID, width=7,cursor='hand2', command=previous, state=DISABLED)
            self.prevques_btn.grid(row=10, column=0, pady=10, padx=10,  sticky=W)
            
            #next question btn
            self.nextques_btn=Button(self.addquiz_frame, text='Next', font=f, relief=SOLID, width=7,cursor='hand2', command=next)
            self.nextques_btn.grid(row=10, column=2, pady=10, padx=10,  sticky=W)

            def add_quiz():
                #add final entries into list
                self.ques_titles.append(self.questitle_entry.get('1.0', 'end-1c'))
                self.opA.append(self.opA_entry.get())
                self.opB.append(self.opB_entry.get())
                self.opC.append(self.opC_entry.get())
                self.opD.append(self.opD_entry.get())
                self.correctop.append(self.correctop_entry.get())
                print(self.ques_titles)
                print(self.opA)
                print(self.opB)
                print(self.opC)
                print(self.opD)
                print(self.correctop)



                if len(self.ques_titles) == len(self.opA) == len(self.opB) == len(self.opC) == len(self.opD) == len(self.correctop):
                    for i in range(len(self.ques_titles)):
                        insert_ques=('''INSERT INTO quiz(idquiz, subj_name, chap_name, ques_title, opA, opB, opC, opD, correct_op) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''')
                        ques_data=(None, 'Computer Architecture & Networks', self.chapter_entry.get(),self.ques_titles[i], self.opA[i], self.opB[i], self.opC[i], self.opD[i], self.correctop[i])
                        cur.execute(insert_ques, ques_data)
                        con.commit()
                # #clear list after database add
                    self.ques_titles.clear()
                    self.opA.clear()
                    self.opB.clear()
                    self.opC.clear()
                    self.opD.clear()
                    self.correctop.clear()

            self.addquiz_btn=Button(self.addquiz_frame, text='Add', font=f3, relief=SOLID, width=10,cursor='hand2', command=add_quiz)
            self.addquiz_btn.grid(row=10, column=1, pady=10, padx=10, sticky=W)

        #delete quiz popup

        #quiz add, delete btns
        self.quiz_btn_frame=Frame(self, bg=bgc, width=800, height=400)
        self.quiz_btn_frame.place(x=40, y=650)

        self.addquiz_btn=Button(self.quiz_btn_frame, text='Add Quiz', font=f3, relief=SOLID, cursor='hand2', command=add_quiz_frame)
        self.addquiz_btn.grid(row=0, column=0, sticky=W, pady=10, padx=65)

        self.deletequiz_btn=Button(self.quiz_btn_frame, text='Delete Quiz', font=f3, relief=SOLID, cursor='hand2')
        self.deletequiz_btn.grid(row=0, column=1, sticky=W, pady=10, padx=10)



class ChatAdmin(tk.Frame):
    def __init__(self,parent=None, controller=None, name=None):
        global show_students_frame, show_books_frame
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.name=name
        self.parent=parent

        #ui_bg and clock and logout btn
        ui_bg(self, 'images/Slide5.png')
        clockdate(self)
        view_user(self,Homepage, controller)
        log_out_btn(self, Loginpage, controller)
        admin_btns(self, StudentsView, BooksView, QuizAdmin, ChatAdmin, CourseMaterials, AdminAppointments,controller)

        #chat admin label
        chat_admin_label=Label(self, text='Chat Admin', font=('Arial', 20, 'bold'), bg=bgc, fg='black')
        chat_admin_label.place(x=585, y=155)

        #discussions server treeview scroll
        self.discussions_frame=Frame(self, width=300, height=500, bg=bgc)
        self.discussions_frame.place(x=125, y=225)


        self.discussions_tv_frame=Frame(self.discussions_frame, bg=bgc)
        self.discussions_tv_frame.grid(row=1, column=0)

        self.discussions_tv_scroll=Scrollbar(self.discussions_tv_frame)
        self.discussions_tv_scroll.pack(side=RIGHT, fill=Y)

        self.discussions_tv=ttk.Treeview(self.discussions_tv_frame, yscrollcommand=self.discussions_tv_scroll.set, height=13)
        self.discussions_tv.pack()

        self.discussions_tv_scroll.config(command=self.discussions_tv.yview)

        self.discussions_tv.column('#0', width=435, minwidth=435)
        self.discussions_tv.heading('#0', text='Discussion Servers', anchor=W)

        #insert server name
        self.discussions_tv.insert(parent='', index='end', iid=0, text='Computer Architecture & Networks')

        #chat msg screen
        self.chat_scrolledtxt=scrolledtext.ScrolledText(self,width=58,height=15,bg='white', relief=SOLID, bd=2, font=f, wrap=WORD)
        self.chat_scrolledtxt.place(x=650, y=225)

        #chat msg input entry
        #frame
        self.chat_entry_frame=Frame(self, width=675, height=50, bg=bgc)
        self.chat_entry_frame.place(x=641, y=600)

        self.chat_entry=Text(self.chat_entry_frame, height=5,width=52, font=f, wrap=WORD,relief=SOLID, bd=2)
        self.chat_entry.grid(row=0, column=0, padx=10, pady=5)

        #send btn
        self.send_btn=Button(self.chat_entry_frame, text='Send', font=f, relief=SOLID, bd=2, cursor='hand2')
        self.send_btn.grid(row=0, column=1, padx=10, pady=5)

        

class CourseMaterials(tk.Frame):
    def __init__(self,parent=None, controller=None, name=None):
        global show_students_frame, show_books_frame
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.name=name
        self.parent=parent

        #ui_bg and clock and logout btn
        ui_bg(self, 'images/Slide5.png')
        clockdate(self)
        view_user(self,Homepage, controller)
        log_out_btn(self, Loginpage, controller)
        admin_btns(self, StudentsView, BooksView, QuizAdmin, ChatAdmin, CourseMaterials, AdminAppointments,controller)

        #course materials label
        course_materials_label=Label(self, text='Course Materials', font=('Arial', 22, 'bold'), bg=bgc, fg='black')
        course_materials_label.place(x=525, y=155)

        #show course materials in hierarchy treeview
        #treeview frame
        self.material_tv_frame=Frame(self, bg=bgc)
        self.material_tv_frame.place(x=30, y=200)

        #vertical scrollbar
        tree_scroll=Scrollbar(self.material_tv_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        style=ttk.Style()
        style.configure('Book.Treeview', font=f, rowheight=45)

        tree = ttk.Treeview(self.material_tv_frame, yscrollcommand=tree_scroll.set, style='Book.Treeview', height=8, selectmode='browse')
        tree.pack()
        tree_scroll.config(command=tree.yview)

        tree.column('#0', width=480, stretch=False, minwidth=480)
        tree.heading('#0', text='Course Materials',  anchor=W)

        #for loop for showing parent and children node from db
        
        con = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="rootpass",
                                    database="all2")
        cur = con.cursor()
        w_set=cur.execute("SELECT DISTINCT week FROM coursematerials;")
        w_set=cur.fetchall()
        my_index=0
        #select distinct week from course_materials
        for wk in w_set:
            wk_id=tree.insert(parent='', text='Week '+str(wk[0]), index=my_index, open=True)
            my_index+=1
            #select material name from course_materials where week=week
            m_set=cur.execute("SELECT material_name FROM coursematerials WHERE week=%s;",(wk[0],))
            m_set=cur.fetchall()
            for mat in m_set:
                tree.insert(parent=wk_id, text=mat[0], index= my_index,open=False)
                my_index+=1
        con.commit()
        con.close()
        
        # #upload material frame
        self.upload_material_frame=Frame(self, bg=bgc, relief=SOLID, bd=2, width=800, height=500)
        self.upload_material_frame.place(x=537, y=200)

        # #view files, images, documents frame
        self.view_materials_frame=Frame(self, bg=bgc, relief=SOLID, bd=2, width=500, height=500)

        #zoom spinbox
        #zoom spinbox selector
        self.zoom_lbl_mat=Label(self, text='Zoom', font=f, bg=bgc)
        zoom_var2=IntVar()
        zoom_var2.set(72)
        self.zoom_spinmat=Spinbox(self, textvariable= zoom_var2, from_=20, to=500,increment=5, width=3, font=f2)
        
        
        #upload files, images, documents from database
        #files accepted only in pdf
        def uploadmaterial_frame():
            #forget place view material frame
            self.upload_material_frame.place(x=700, y=200)
            self.view_materials_frame.place_forget()
            self.zoom_lbl_mat.place_forget()
            self.zoom_spinmat.place_forget()
            
            #upload material label
            self.upload_material_label=Label(self.upload_material_frame, text='Upload Course Materials', font=('Arial', 20, 'bold'), bg=bgc)
            self.upload_material_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

            #subject, week, name, file
            self.subject_label=Label(self.upload_material_frame, text='Subject', font=f3, bg=bgc)
            self.subject_label.grid(row=1, column=0, padx=20, pady=20, sticky=W)

            self.subject_entry=ttk.Combobox(self.upload_material_frame, font=f3, width=28)
            self.subject_entry['values']=subjects
            self.subject_entry.current(1)
            self.subject_entry.grid(row=1, column=1, padx=20, pady=20, sticky=W, columnspan=2)

            self.week_label=Label(self.upload_material_frame, text='Week', font=f3, bg=bgc)
            self.week_label.grid(row=2, column=0, padx=20, pady=20, sticky=W)

            self.week_entry=ttk.Combobox(self.upload_material_frame, font=f3, width=7)
            self.week_entry['values']=weeks
            self.week_entry.grid(row=2, column=1, padx=20, pady=20, sticky=W, columnspan=2)

            self.name_label=Label(self.upload_material_frame, text='Name', font=f3, bg=bgc)
            self.name_label.grid(row=3, column=0, padx=20, pady=20, sticky=W)

            self.name_entry=Text(self.upload_material_frame, font=f, width=30, height=2, wrap=WORD)
            self.name_entry.grid(row=3, column=1, padx=20, pady=20, sticky=W, columnspan=2)

            self.file_label=Label(self.upload_material_frame, text='File', font=f3, bg=bgc)
            self.file_label.grid(row=4, column=0, padx=20, pady=20, sticky=W)

            self.file_entry=Text(self.upload_material_frame, font=f, width=30, height=5, wrap=WORD)
            self.file_entry.grid(row=4, column=1, padx=20, pady=20, sticky=W, columnspan=2)

            #connect to db
            con = mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="rootpass",
                                        database="all2")
            cur = con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS coursematerials( idcoursematerials INT AUTO_INCREMENT PRIMARY KEY,
                                                                                week INT NOT NULL,
                                                                                subj_name varchar(100) NOT NULL,
                                                                                material_name LONGTEXT NOT NULL,
                                                                                material_file LONGTEXT NOT NULL)''')
            con.commit()

            def upload_materialfile():
                self.upload_file_btn.config(text='Upload File')
                self.file_path = filedialog.askopenfilename(title="Select Course Material", filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
                #change btn name to uploaded
                if self.file_path != '' and not re.match(r'.*\.pdf', self.file_path):
                    self.upload_file_btn.config(text='Upload File')
                    self.file_entry.delete('1.0', END)
                    messagebox.showerror('Error', 'Please select a pdf file')
                elif self.file_path != '' and re.match(r'.*\.pdf', self.file_path):
                    self.upload_file_btn.config(text='Uploaded')
                    self.file_entry.insert(END, self.file_path)

            def add_material():
                check_counter =0
                warn=' '
                if self.subject_entry.get() == '':
                    warn='Please select a subject'
                else:
                    check_counter +=1

                if self.week_entry.get() == '':
                    warn='Please select a week'
                else:
                    check_counter +=1
                    
                if self.name_entry.get('1.0', END) == '':
                    warn='Please enter material name'
                else:
                    check_counter +=1
                    
                if self.file_entry.get('1.0', END) == '':
                    warn='Please select a file'
                else:
                    check_counter +=1
                    
                if check_counter == 4:
                    try:
                        con = mysql.connector.connect(host="localhost",
                                                        user="root",
                                                        password="rootpass",
                                                        database="all2")
                        cur=con.cursor()

                        #get user entry
                        idcoursematerials=None
                        subject=self.subject_entry.get()
                        week=self.week_entry.get()
                        name=self.name_entry.get('1.0', END)
                        file=self.file_entry.get('1.0', END)

                        insert_material = ("INSERT INTO  coursematerials(idcoursematerials, week, subj_name, material_name, material_file) VALUES (%s, %s, %s, %s, %s);")
                        data_material = (idcoursematerials, week, subject, name, file)
                        cur.execute(insert_material, data_material)
                        con.commit()
                        con.close()
                        messagebox.showinfo('Success', 'Course Material Added Successfully!')

                    except Exception as ep:
                        messagebox.showerror('', ep)
                else:
                    messagebox.showerror('', warn)

            #upload file buttom
            self.upload_file_btn=Button(self.upload_material_frame, text='Upload File', font=f3, cursor='hand2', command=upload_materialfile)
            self.upload_file_btn.grid(row=5, column=1, padx=20, pady=20, sticky=W)

            #add material btn
            self.add_material_btn=Button(self.upload_material_frame, text='Add Material', font=f3, cursor='hand2', command=add_material)
            self.add_material_btn.grid(row=5, column=2, padx=20, pady=20, sticky=W)

        def deletematerial():
            x=tree.selection()[0]
            value=tree.item(x)['text']
            tree.delete(x)
            con = mysql.connector.connect(host="localhost", 
                                          user="root",
                                          password="rootpass", 
                                          database="all2")
            cur = con.cursor()
            cur.execute("DELETE FROM coursematerials WHERE material_name=%s", (value,))
            con.commit()
            con.close()

            # clear pdf
            self.view_mat_pdf.img_object_li.clear()

        

        def show_material(e):
            self.delete_btn.config(state=NORMAL)

            #forget upload frame place
            self.view_materials_frame.place(x=535, y=200)    
            self.upload_material_frame.place_forget()     
            self.zoom_lbl_mat.place(x=1245, y=172)
            self.zoom_spinmat.place(x=1308, y=175)
            #grab material name
            selected=tree.selection()[0]
            values=tree.item(selected)['text']  
            

            #connect to db
            con = mysql.connector.connect(host="localhost", user="root", password="rootpass", database="all2")
            cur = con.cursor()
            file=cur.execute("SELECT material_file FROM coursematerials WHERE material_name=%s", (values,))
            file=cur.fetchone()         

            #show pdf
            if file:
                self.view_mat_pdf = pdf.ShowPdf()
                self.view_mat_pdf.img_object_li.clear()
                self.material=self.view_mat_pdf.pdf_view(self.view_materials_frame, pdf_location=file[0], width=100, height=31,bar=False, zoomDPI=zoom_var2.get())
                self.material.grid(row=0, column=0)
        tree.bind('<ButtonRelease-1>', show_material)

        #add materials button
        self.upload_btn=Button(self, text='Add Materials', font=f3, relief=SOLID, cursor='hand2', command=uploadmaterial_frame)
        self.upload_btn.place(x=70, y=600)

        #remove files, images, documents
        self.delete_btn=Button(self, text='Remove Materials', font=f3, relief=SOLID, cursor='hand2', command=deletematerial, state=DISABLED)
        self.delete_btn.place(x=250, y=600)

        #expand all nodes btn
        self.expandtv_btn=Button(self, text='Expand All', font=f3, relief=SOLID, cursor='hand2', command=lambda:expand_tv(tree))
        self.expandtv_btn.place(x=70, y=650)

        #colapse all nodes btn
        self.collapsetv_btn=Button(self, text='Collapse All', font=f3, relief=SOLID, cursor='hand2',command=lambda:collapse_tv(tree))
        self.collapsetv_btn.place(x=250, y=650)

class AdminAppointments(tk.Frame):
    def __init__(self,parent=None, controller=None, name=None):
        global show_students_frame, show_books_frame
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.name=name
        self.parent=parent

        #ui_bg and clock and logout btn
        ui_bg(self, 'images/Slide5.png')
        clockdate(self)
        view_user(self,Homepage, controller)
        log_out_btn(self, Loginpage, controller)
        admin_btns(self, StudentsView, BooksView, QuizAdmin, ChatAdmin, CourseMaterials, AdminAppointments,controller)


        #appointments treeview
        self.appt_frame=Frame(self, bg=bgc)
        self.appt_frame.place(x=45, y=150)

        self.appointments_lbl=Label(self.appt_frame, text='Appointments', font=('Arial', 20, 'bold'), bg=bgc)
        self.appointments_lbl.grid(row=0, column=0, padx=10)

        self.appt_tvframe=Frame(self.appt_frame, bg=bgc)
        self.appt_tvframe.grid(row=1, column=0, pady=10)

        self.appt_tv_scroll=Scrollbar(self.appt_tvframe)
        self.appt_tv_scroll.pack(side=RIGHT, fill=Y)

        self.appt_tv=ttk.Treeview(self.appt_tvframe,yscrollcommand=self.appt_tv_scroll.set, height=7)
        self.appt_tv.pack()

        self.appt_tv_scroll.config(command=self.appt_tv.yview)

        self.appt_tv['columns']=('Student', 'Date', 'Time', 'Topic', 'Status')

        self.appt_tv.column('#0', width=0, stretch=NO)
        self.appt_tv.column('Student', anchor=W, width=200, minwidth=200, stretch=NO)
        self.appt_tv.column('Date', anchor=W, width=100, minwidth=100, stretch=NO)
        self.appt_tv.column('Time', anchor=W, width=100, minwidth=100, stretch=NO)
        self.appt_tv.column('Topic', anchor=W, width=200, minwidth=200, stretch=NO)
        self.appt_tv.column('Status', anchor=W, width=100, minwidth=100, stretch=NO)

        self.appt_tv.heading('#0', text='', anchor=CENTER)
        self.appt_tv.heading('Student', text='Student', anchor=CENTER)
        self.appt_tv.heading('Date', text='Date', anchor=CENTER)
        self.appt_tv.heading('Time', text='Time', anchor=CENTER)
        self.appt_tv.heading('Topic', text='Topic', anchor=CENTER)
        self.appt_tv.heading('Status', text='Status', anchor=CENTER)


        #accept or reject appointment, leave a note if rejected, frame
        self.admin_response_frame=Frame(self, bg=bgc, bd=2, relief=SOLID)
        self.admin_response_frame.place(x=163, y=490)

        self.admin_response_lbl=Label(self.admin_response_frame, text='Appointment Response', font=('Arial', 20,'bold'), bg=bgc)
        self.admin_response_lbl.grid(row=0, column=0, padx=10, columnspan=3)

        #accept btn, reject btn
        self.accept_btn=Button(self.admin_response_frame, text='Accept', font=f3, relief=SOLID, cursor='hand2', width=10)
        self.accept_btn.grid(row=1, column=1, padx=10, pady=10)

        self.reject_btn=Button(self.admin_response_frame, text='Reject', font=f3, relief=SOLID, cursor='hand2', width=10)
        self.reject_btn.grid(row=1, column=2, padx=10, pady=10)

        #note if rejected
        self.note_lbl=Label(self.admin_response_frame, text='Note:', font=f3, bg=bgc)
        self.note_lbl.grid(row=2, column=0, padx=10, pady=10)

        self.note_entry=Text(self.admin_response_frame, font=f3, width=30, height=3)
        self.note_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        #send btn
        self.send_btn=Button(self.admin_response_frame, text='Send', font=f3, relief=SOLID, cursor='hand2')
        self.send_btn.grid(row=3, column=1, padx=10, pady=10, columnspan=3)



        
        #show questions from students treeview (another side to show images from students if any)
        self.stud_ques_frame=Frame(self, bg=bgc)
        self.stud_ques_frame.place(x=785, y=150)

        self.stud_ques_lbl=Label(self.stud_ques_frame, text='Questions from Students', font=('Arial', 20, 'bold'), bg=bgc)
        self.stud_ques_lbl.grid(row=0, column=0,  padx=10)

        self.stud_ques_tvframe=Frame(self.stud_ques_frame, bg=bgc)
        self.stud_ques_tvframe.grid(row=1, column=0, pady=10)

        self.stud_ques_tv_scroll=Scrollbar(self.stud_ques_tvframe)
        self.stud_ques_tv_scroll.pack(side=RIGHT, fill=Y)

        self.stud_ques_tv=ttk.Treeview(self.stud_ques_tvframe,yscrollcommand=self.stud_ques_tv_scroll.set, height=7)
        self.stud_ques_tv.pack()

        self.stud_ques_tv_scroll.config(command=self.stud_ques_tv.yview)

        self.stud_ques_tv['columns']=('Student', 'Question')

        self.stud_ques_tv.column('#0', width=0, stretch=NO)
        self.stud_ques_tv.column('Student', anchor=W, width=200, minwidth=200, stretch=NO)
        self.stud_ques_tv.column('Question', anchor=W, width=300, minwidth=300, stretch=NO)

        self.stud_ques_tv.heading('#0', text='', anchor=CENTER)
        self.stud_ques_tv.heading('Student', text='Student', anchor=CENTER)
        self.stud_ques_tv.heading('Question', text='Question', anchor=CENTER)

        #reply to questions from students
    
        self.reply_frame=Frame(self, bg=bgc, bd=2, relief=SOLID)
        self.reply_frame.place(x=835, y=490)

        self.reply_lbl=Label(self.reply_frame, text='Reply', font=('Arial', 20,'bold'), bg=bgc)
        self.reply_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.reply_tv=Text(self.reply_frame, width=30, height=4, padx=10, pady=10, wrap=WORD, font=f3)
        self.reply_tv.grid(row=1, column=0, padx=10, pady=10)

        self.reply_btn=Button(self.reply_frame, text='Reply', font=f3, relief=SOLID, cursor='hand2', width=10)
        self.reply_btn.grid(row=2, column=0, padx=10, pady=10)









class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller 
        global login_details

        # ui_bg
        ui_bg(self, img_file)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #appointments page btn
        view_appt(self, Appointments, controller)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #Recent Courses Title
        self.courses_lbl = Label(self, text ='Recent Courses', font = ('Arial', 28), bg=bgc)
        self.courses_lbl.pack()
        self.courses_lbl.place(x=380, y=100)

        #courses frame
        self.courses_frame = Frame(self, bg=bgc,relief=SOLID)
        self.courses_frame.place(x=99, y=155)


        #Courses button with images
        image9=Image.open('images\comp_arch.png')
        img9=image9.resize((170,150))
        my_img9=ImageTk.PhotoImage(img9)
        comp_arch_img=Label(image=my_img9)
        comp_arch_img.image=my_img9

        self.course1_btn = Button(self.courses_frame, image=my_img9, cursor='hand2', command=lambda: controller.show_frame(Subject1))
        self.course1_btn.grid(row=0, column=0, padx=10, pady=10)

        self.course1_lbl = Label(self.courses_frame, text ='Computer Architecture & Networks', wraplength=200,font = f, bg=bgc)
        self.course1_lbl.grid(row=1, column=0, padx=10)

        image10=Image.open('images\programming.png')
        img10=image10.resize((170,150))
        my_img10=ImageTk.PhotoImage(img10)
        oop_img=Label(image=my_img10)
        oop_img.image=my_img10

        self.course2_btn = Button(self.courses_frame, image=my_img10, cursor='hand2', state='disabled' )
        self.course2_btn.grid(row=0, column=1, padx=10, pady=10)

        self.course2_lbl = Label(self.courses_frame, text ='Programming & Algorithms', wraplength=200, font =f, bg=bgc)
        self.course2_lbl.grid(row=1, column=1, padx=10)

        image11=Image.open('images\maths_for_cs.png')
        img11=image11.resize((170,150))
        my_img11=ImageTk.PhotoImage(img11)
        maths_img=Label(image=my_img11)
        maths_img.image=my_img11

        self.course3_btn = Button(self.courses_frame, image=my_img11, cursor='hand2', state='disabled' )
        self.course3_btn.grid(row=0, column=2, padx=10, pady=10)

        self.course3_lbl = Label(self.courses_frame, text ='Mathematics for Computer Science',  wraplength=200, font =f, bg=bgc)
        self.course3_lbl.grid(row=1, column=2, padx=10)

        image12=Image.open('images\database.png')
        img12=image12.resize((170,150))
        my_img12=ImageTk.PhotoImage(img12)
        db_img=Label(image=my_img12)
        db_img.image=my_img12

        self.course4_btn = Button(self.courses_frame, image=my_img12, cursor='hand2', state='disabled' )
        self.course4_btn.grid(row=0, column=3, padx=10, pady=10)

        self.course4_lbl = Label(self.courses_frame, text ='Database Systems',  wraplength=200, font =f, bg=bgc)
        self.course4_lbl.grid(row=1, column=3, padx=10)


        #Recent Books Title
        self.books_lbl = Label(self, text ='Recent Books', font = ('Arial', 28), bg=bgc)
        self.books_lbl.pack()
        self.books_lbl.place(x=385, y=420)

        #books frame
        self.books_frame = Frame(self, bg=bgc,relief=SOLID)
        self.books_frame.place(x=99, y=475)

        #Books button with images (books need to be taken from db)
        image13=Image.open('books\computer-organization-and-architecture.png')
        img13=image13.resize((150,180))
        my_img13=ImageTk.PhotoImage(img13)
        book1_img=Label(image=my_img13)
        book1_img.image=my_img13

        self.book1_btn = Button(self.books_frame,image= my_img13, cursor='hand2')
        self.book1_btn.grid(row=0, column=0, padx=10, pady=10)

        self.book1_lbl=Label(self.books_frame, text='Computer Organization & Architecture', wraplength=195, font=f, bg=bgc)
        self.book1_lbl.grid(row=1, column=0, padx=10)

        image14=Image.open('books\ObjectOrientedProgramminginC4thEdition.png')
        img14=image14.resize((150,180))
        my_img14=ImageTk.PhotoImage(img14)
        book2_img=Label(image=my_img14)
        book2_img.image=my_img14

        self.book2_btn = Button(self.books_frame, image=my_img14, cursor='hand2')
        self.book2_btn.grid(row=0, column=1, padx=10, pady=10)

        self.book2_lbl = Label(self.books_frame, text ='Objected Oriented Programming', wraplength=195, font =f, bg=bgc)
        self.book2_lbl.grid(row=1, column=1, padx=10)

        image15=Image.open('books\\rosen_discrete_mathematics_and_its_applications_7th_edition.png')
        img15=image15.resize((150,180))
        my_img15=ImageTk.PhotoImage(img15)
        book3_img=Label(image=my_img15)
        book3_img.image=my_img15

        self.book3_btn = Button(self.books_frame, image=my_img15, cursor='hand2')
        self.book3_btn.grid(row=0, column=2, padx=10, pady=10)

        self.book3_lbl = Label(self.books_frame, text ='Discrete Mathematics and its Applications', wraplength=195, font =f, bg=bgc)
        self.book3_lbl.grid(row=1, column=2, padx=10)

        image16=Image.open('books\Computer Architecture, Sixth Edition_ A_Quantitative_Approach.png')
        img16=image16.resize((150,180))
        my_img16=ImageTk.PhotoImage(img16)
        book4_img=Label(image=my_img16)
        book4_img.image=my_img16

        self.book4_btn = Button(self.books_frame,image=my_img16, cursor='hand2')
        self.book4_btn.grid(row=0, column=3, padx=10, pady=10)

        self.book4_lbl = Label(self.books_frame, text ='Computer Architecture', wraplength=195, font =f, bg=bgc)
        self.book4_lbl.grid(row=1, column=3, padx=10)

        #take books from database
        


        #calendar for appointment
        
        #calendar title
        self.calendar_lbl = Label(self, text ='Calendar', font = ('Arial', 28), bg=bgc)
        self.calendar_lbl.pack()
        self.calendar_lbl.place(x=1015, y=100)

        #calendar frame
        self.calendar_frame = Frame(self, bg=bgc,relief=SOLID)
        self.calendar_frame.place(x=965, y=155)

        today = datetime.date.today()
        #calendar widget
        self.cal = Calendar(self.calendar_frame, selectmode="day", year=today.year, month=today.month, day=today.day, date_pattern='dd/mm/yyyy', font=('Arial', 10))
        self.cal.pack(pady=20, padx=20)


        #post a question label
        self.post_lbl = Label(self, text ='Post a Question', font = ('Arial', 28), bg=bgc)
        self.post_lbl.pack()
        self.post_lbl.place(x=985, y=425)

        #post a question frame
        self.post_frame = Frame(self, bg=bgc,relief=SOLID)
        self.post_frame.place(x=934, y=465)

        #question textbox
        self.question_txt = Text(self.post_frame, width=35, height=10, wrap='word',font=f)
        self.question_txt.insert(INSERT, 'Type your question here...')
        self.question_txt.grid(row=0, column=0,columnspan=3, padx=10, pady=10)

        #post question btn
        self.post_btn = Button(self.post_frame, width=15, text='Post', font=f, relief=SOLID,cursor='hand2')
        self.post_btn.grid(row=1, column=1, padx=10, pady=10)


class Subject1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ui_bg
        ui_bg(self, img_file)
       
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #back btn
        back_btn(self, Homepage, controller)
        #appointments page btn
        view_appt(self, Appointments, controller)
        #logout btn
        log_out_btn(self,Loginpage, controller)

        #Subject title
        self.subj1_title = Label(self, text ='Computer Architecture & Networks', font = ('Arial', 28), bg=bgc )
        self.subj1_title.pack()
        self.subj1_title.place(x=400, y=100)

         #show course materials in hierarchy treeview
        #treeview frame
        self.subj1_tv_frame=Frame(self, bg=bgc)
        self.subj1_tv_frame.place(x=100, y=200)

        #vertical scrollbar
        tree_scroll=Scrollbar(self.subj1_tv_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        subj_tree = ttk.Treeview(self.subj1_tv_frame,style='Book.Treeview', yscrollcommand=tree_scroll.set,  height=10)
        subj_tree.pack()
        tree_scroll.config(command=subj_tree.yview)

        subj_tree.column('#0',  width=480, stretch=False, minwidth=480)
        subj_tree.heading('#0', text='Course Materials',  anchor=W)

        #for loop for showing parent and children node from db
        
        con = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="rootpass",
                                    database="all2")
        cur = con.cursor()
        w_set=cur.execute("SELECT DISTINCT week FROM coursematerials;")
        w_set=cur.fetchall()
        my_index=0
        #select distinct week from course_materials
        for wk in w_set:
            wk_id=subj_tree.insert(parent='', text='Week '+str(wk[0]), index=my_index, open=True)
            my_index+=1
            #select material name from course_materials where week=week
            m_set=cur.execute("SELECT material_name FROM coursematerials WHERE week=%s;",(wk[0],))
            m_set=cur.fetchall()
            for mat in m_set:
                subj_tree.insert(parent=wk_id, text=mat[0], index= my_index,open=False)
                my_index+=1
        con.close()

        #expand all nodes btn
        self.expand_btn=Button(self, text='Expand All', font=f, relief=SOLID, cursor='hand2', command=lambda:expand_tv(subj_tree))
        self.expand_btn.place(x=150, y=700)

        #colapse all nodes btn
        self.collapse_btn=Button(self, text='Collapse All', font=f, relief=SOLID, cursor='hand2',command=lambda:collapse_tv(subj_tree))
        self.collapse_btn.place(x=350, y=700)

        #view pdf files
        self.view_subj1_frame=Frame(self, bg=bgc, width=750, height=500, relief=SOLID, bd=2)
        self.view_subj1_frame.place(x=615, y=200)

        #zoom spinbox
        self.zoom_lbl_subj1=Label(self, text='Zoom', font=f, bg=bgc)
        self.zoom_lbl_subj1.place(x=1265, y=172)
        zoom_var2=IntVar()
        zoom_var2.set(72)
        self.zoom_spinsubj1=Spinbox(self, textvariable= zoom_var2, from_=20, to=500,increment=5, width=3, font=f2)
        self.zoom_spinsubj1.place(x=1319, y=174)

        def show_material(e):

            #grab material name
            selected=subj_tree.selection()[0]
            values=subj_tree.item(selected)['text']  

            #connect to db
            con = mysql.connector.connect(host="localhost", user="root", password="rootpass", database="all2")
            cur = con.cursor()
            file=cur.execute("SELECT material_file FROM coursematerials WHERE material_name=%s", (values,))
            file=cur.fetchone()
            con.close()
            #show pdf
            if file:
                self.view_subj1_pdf = pdf.ShowPdf()
                self.view_subj1_pdf.img_object_li.clear()
                self.subj1=self.view_subj1_pdf.pdf_view(self.view_subj1_frame, pdf_location=file[0], width=91, height=31,bar=False, zoomDPI=zoom_var2.get())
                self.subj1.grid(row=0, column=0)
        subj_tree.bind('<ButtonRelease-1>', show_material)
        

class Books(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ui_bg
        ui_bg(self, img_file)
       
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #appointments page btn
        view_appt(self, Appointments, controller)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #Books Title
        w = Label(self, text ='Books', font = ('Arial', 28), bg=bgc )
        w.pack()
        w.place(x=610, y=90)

        #search books
        #frame for search button and icon
        self.searchbtn_frame=Frame(self, bg=bgc, bd=1, relief=SOLID)
        self.searchbtn_frame.place(x=165, y=135)

        self.searchbk_lbl=Label(self.searchbtn_frame, text='Search', font=('Arial', 18), bg=bgc)
        self.searchbk_lbl.grid(row=0, column=0)
        self.searchbk_entry=Entry(self.searchbtn_frame, font=f3, width=18)
        self.searchbk_entry.grid(row=0, column=1)

        #search icon
        self.search_icon=Image.open('images\search.png')
        self.search_icon=self.search_icon.resize((25,25))
        self.search_icon=ImageTk.PhotoImage(self.search_icon)
        

        #show available books treeview
        self.bk_tree_frame=Frame(self, bg=bgc, bd=2, relief=SOLID)
        self.bk_tree_frame.place(x=115, y=180)

        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', font=f)
        style.configure('Treeview', font=f2)
        ttk.Style().configure('Books.Treeview', rowheight=60)

        self.tree_frame=Frame(self.bk_tree_frame)
        self.tree_frame.grid(row=0, column=0)

        tree_scroll=Scrollbar(self.tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        my_tree=ttk.Treeview(self.tree_frame, style='Books.Treeview',yscrollcommand=tree_scroll.set, selectmode='browse', height=9)
        my_tree.pack()

        tree_scroll.config(command=my_tree.yview)

        my_tree['columns']= ('ID', 'Book Name', 'Category')

        #format columns
        my_tree.column('#0', width=0, stretch=NO)
        my_tree.column('ID', width=60, anchor=CENTER, stretch=False, minwidth=60)
        my_tree.column('Book Name', width=250, anchor=CENTER, stretch=NO, minwidth=250)
        my_tree.column('Category', width=155, anchor=CENTER, stretch=NO, minwidth=155)

        #column headings
        my_tree.heading('#0', text='', anchor=CENTER)
        my_tree.heading('ID', text='ID', anchor=CENTER)
        my_tree.heading('Book Name', text='Book Name', anchor=CENTER)
        my_tree.heading('Category', text='Category', anchor=CENTER)

        #view book label
        self.view_bk_lbl=Label(self, text='View Book', font=('Arial', 20, 'bold'), bg=bgc, fg='black')
        self.view_bk_lbl.place(x=955, y=135)

        #pdf viewer for books
        self.pdf_frame=Frame(self, bg=bgc)
        self.pdf_frame.place(x=675, y=180)

        
        #zoom spinbox selector
        self.zoom_lbl=Label(self, text='Zoom', font=f, bg=bgc)
        self.zoom_lbl.place(x=1245, y=152)
        zoom_var=IntVar()
        zoom_var.set(72)
        self.zoom_spin=Spinbox(self, textvariable= zoom_var, from_=20, to=500,increment=5, width=3, font=f2)
        self.zoom_spin.place(x=1308, y=155)

        #showpdf
        self.book_pdf = pdf.ShowPdf()
        self.book_pdf.img_object_li.clear() #clear old pdf inside the frame
        self.book=self.book_pdf.pdf_view(self.pdf_frame, bar=False, pdf_location=None, width=82, height=35, zoomDPI=zoom_var.get())
        self.book.grid(row=1, column=0, columnspan=3)


        #view books
        con = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="rootpass",
                                    database="all2")
        cur = con.cursor()
        r_set=cur.execute("SELECT idbooks, bookname, bookcategory FROM books;")
        r_set=cur.fetchall()
        for row in r_set:
            wraptxt1= textwrap.fill(row[1], width=30)
            my_tree.insert("", tk.END, values=(row[0], wraptxt1, row[2]))

        #show pdf when click on treeview row
        def show_book_record(e):
            #grab record number and values
            selected=my_tree.focus()
            values=my_tree.item(selected, 'values')

            #get data from database
            con = mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="rootpass",
                                        database="all2")
            cur = con.cursor()
            #get image from db
            data=cur.execute("SELECT bookfile FROM books WHERE idbooks=%s", (values[0],))
            data= cur.fetchone()

            #show image upon clicking treeview row
            if data :
                self.book_pdf.img_object_li.clear() #clear old pdf inside the frame
                self.book=self.book_pdf.pdf_view(self.pdf_frame, bar=False, pdf_location=data[0], width=82, height=35, zoomDPI=zoom_var.get())
                self.book.grid(row=1, column=0, columnspan=3)

        my_tree.bind('<ButtonRelease-1>', show_book_record)

        #search bar function 
        #by category
        def search_book():
            if self.searchbk_entry.get() != "":
                con = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="rootpass",
                                    database="all2")
                cur = con.cursor()
                my_tree.delete(*my_tree.get_children())
                r_set=cur.execute('''SELECT idbooks, bookname, bookcategory FROM books WHERE bookname LIKE %s OR bookcategory LIKE %s''' , ('%'+(self.searchbk_entry.get())+'%', '%'+(self.searchbk_entry.get())+'%'))
                r_set = cur.fetchall()
                for row in r_set:
                    wraptxt1= textwrap.fill(row[1], width=30)
                    my_tree.insert("", tk.END, values=(row[0], wraptxt1, row[2]))
            else:
                con = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="rootpass",
                                    database="all2")
                cur = con.cursor()
                my_tree.delete(*my_tree.get_children())
                r_set=cur.execute("SELECT idbooks, bookname, bookcategory FROM books;")
                r_set=cur.fetchall()
                for row in r_set:
                    wraptxt1= textwrap.fill(row[1], width=30)
                    my_tree.insert("", tk.END, values=(row[0], wraptxt1, row[2]))
        
        self.searchbk_btn=Button(self.searchbtn_frame, image=self.search_icon , cursor='hand2', command=search_book)
        self.searchbk_btn.grid(row=0, column=2)


class Quiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ui_bg
        ui_bg(self, img_file)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #appointments page btn
        view_appt(self, Appointments, controller)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #Quiz title
        self.quiz_lbl = Label(self, text ='Quiz', font = ('Arial', 28) , bg=bgc)
        self.quiz_lbl.pack()
        self.quiz_lbl.place(x=610, y=90)

        #view quiz
        #list down all 
        #quiz subject selection frame
        self.quiz_subjsel_frame=Frame(self, bg=bgc, width=800, height=100)
        self.quiz_subjsel_frame.place(x=100, y=200)

        self.quiz_subjsel_lbl=Label(self.quiz_subjsel_frame, text='Subject', font=f3, bg=bgc)
        self.quiz_subjsel_lbl.grid(row=0, column=0, pady=10, padx=10)

        self.quiz_subjsel=ttk.Combobox(self.quiz_subjsel_frame, font=f3, width=26, values=['Select', 'Computer Architecture & Networks'], state='readonly')
        self.quiz_subjsel.current(1)
        self.quiz_subjsel.grid(row=0, column=1, pady=10)

        #quiz treeview list
        self.quiztv_frame=Frame(self, bg=bgc)
        self.quiztv_frame.place(x=100, y=255)

        #quiz treeview
        self.quiz_tv_scroll=Scrollbar(self.quiztv_frame)
        self.quiz_tv_scroll.pack(side=RIGHT, fill=Y)

        style=ttk.Style()
        style.configure('Quiz.Treeview', font=f)

        self.quiz_tv=ttk.Treeview(self.quiztv_frame, yscrollcommand=self.quiz_tv_scroll.set, style='Quiz.Treeview',height=10)
        self.quiz_tv.pack()

        self.quiz_tv_scroll.config(command=self.quiz_tv.yview)

        self.quiz_tv.column('#0', width=435, minwidth=435)
        self.quiz_tv.heading('#0', text='Quiz Chapters', anchor=W)

        #show distinct chapters in treeview
        def show_quizchp(e):
            if self.quiz_subjsel.get()=='Select':
                #show blank treeview
                self.quiz_tv.delete(*self.quiz_tv.get_children())

            else:
                #connect to db
                con = mysql.connector.connect(host='localhost', 
                                            user='root', 
                                            password='rootpass', 
                                            database='all2')
                cur = con.cursor()
                s_set=cur.execute('''SELECT DISTINCT chap_name FROM quiz WHERE subj_name=%s''', (self.quiz_subjsel.get(),))
                s_set=cur.fetchall()
                for row in s_set:
                    self.quiz_tv.insert('',tk.END, text='Chapter ' +(row[0]))
                con.commit()
                con.close()
        
        #show quiz chapters in treeview first
        show_quizchp(e=None)
        self.quiz_subjsel.bind('<<ComboboxSelected>>', show_quizchp)
        
        #quiz questions frame and add quiz frame func prototypes
        self.quizques_frame=Frame(self, bg='white',  width=720, height=420, relief=SOLID, bd=2)
        self.addquiz_frame=Frame(self, bg=bgc, width=450, height=300, relief=SOLID, bd=2)


        #fix frame row and column size
        self.quizques_frame.rowconfigure(1, weight=1)
        self.quizques_frame.columnconfigure(0, weight=1)
        self.quizques_frame.columnconfigure(1, weight=1)

        #radiobutton selected option variable definition
        selected_option=StringVar()
        
        #quiz chapter title, 1 question, 4 options, previous, next btns
        self.quiz_chapter_title=Label(self.quizques_frame, text=empty_text, font=('Arial', 19,'bold'), bg='white')   
        self.quiz_chapter_title.grid(row=0, column=0, pady=10, padx=10, columnspan=3)

        self.quiz_question=Label(self.quizques_frame, text=empty_text, font=f3, bg='white', wraplength=655)
        self.quiz_question.grid(row=1, column=0, pady=10, padx=10, columnspan=3)

        self.quiz_option1=Radiobutton(self.quizques_frame, text=empty_text, font=f, bg='white', cursor='hand2', variable=selected_option, value='A', tristatevalue=0)
        self.quiz_option1.grid(row=2, column=1, pady=10, padx=10, sticky=W, columnspan=3)

        self.quiz_option2=Radiobutton(self.quizques_frame, text=empty_text, font=f, bg='white', cursor='hand2', variable=selected_option, value='B', tristatevalue=0)
        self.quiz_option2.grid(row=3, column=1, pady=10, padx=10, sticky=W, columnspan=3)


        self.quiz_option3=Radiobutton(self.quizques_frame, text=empty_text, font=f, bg='white',  cursor='hand2', variable=selected_option, value='C', tristatevalue=0)
        self.quiz_option3.grid(row=4, column=1, pady=10, padx=10, sticky=W, columnspan=3)

        self.quiz_option4=Radiobutton(self.quizques_frame, text=empty_text, font=f, bg='white', cursor='hand2', variable=selected_option, value='D', tristatevalue=0)
        self.quiz_option4.grid(row=5, column=1, pady=10, padx=10, sticky=W, columnspan=3)


        #next question
        def next_ques():
            #count score first
            self.user_ans= selected_option.get()
            selected_option.set(None)

            if self.ques_num < (len(self.q_set)-1):
                self.ques_num+=1
            if self.ques_num == (len(self.q_set)-1):
                # self.quiz_next_btn.config(state=DISABLED)
                self.quiz_next_btn.config(text='Done')
                self.quiz_next_btn.config(command=quiz_result)
            else:
                self.quiz_next_btn.config(state=NORMAL)
                self.quiz_prev_btn.config(state=NORMAL)
            

            self.quiz_chapter_title.config(text=self.values)
            self.quiz_question.config(text='Question '+ str(self.ques_num+1) +': '+self.q_set[self.ques_num][0])
            self.quiz_option1.config(text=self.q_set[self.ques_num][1])
            self.quiz_option2.config(text=self.q_set[self.ques_num][2])
            self.quiz_option3.config(text=self.q_set[self.ques_num][3])
            self.quiz_option4.config(text=self.q_set[self.ques_num][4])
            self.quiz_ques_num.config(text='Question '+str(self.ques_num+1)+'/'+str(len(self.q_set)))


        def prev_ques():
            selected_option.set(None)
            if self.ques_num > 0:
                    self.ques_num -= 1
            if self.ques_num == 0:
                self.quiz_prev_btn.config(state=DISABLED)
            else:
                self.quiz_prev_btn.config(state=NORMAL)
                self.quiz_next_btn.config(state=NORMAL)
                self.quiz_next_btn.config(text='Next')
                self.quiz_next_btn.config(command=next_ques)

            self.quiz_chapter_title.config(text=self.values)
            self.quiz_question.config(text='Question '+ str(self.ques_num+1) +': '+self.q_set[self.ques_num][0])
            self.quiz_option1.config(text=self.q_set[self.ques_num][1])
            self.quiz_option2.config(text=self.q_set[self.ques_num][2])
            self.quiz_option3.config(text=self.q_set[self.ques_num][3])
            self.quiz_option4.config(text=self.q_set[self.ques_num][4])
            self.quiz_ques_num.config(text='Question '+str(self.ques_num+1)+'/'+str(len(self.q_set)))


        #bind event: user selects from treeview the quiz chapter, then quiz is shown in quiz frame, for loop  quiz questions from db, prev next btn
        #show quiz questions in quiz frame
        def show_quizques(e):
            selected=self.quiz_tv.focus()
            if selected:
                self.values=self.quiz_tv.item(selected, 'text')
                self.quizques_frame.place(x=583, y=240)
                self.quizques_frame.grid_propagate(False)
                self.addquiz_frame.place_forget()
                #connect to db
                con = mysql.connector.connect(host='localhost', 
                                            user='root', 
                                            password='rootpass', 
                                            database='all2')
                cur = con.cursor()
                self.q_set=cur.execute('''SELECT ques_title, opA, opB, opC, opD, correct_op FROM quiz WHERE chap_name=%s''', (self.values.replace("Chapter ", ""),))
                self.q_set=cur.fetchall()


                self.ques_num=0
                self.quiz_chapter_title.config(text=self.values)
                self.quiz_question.config(text='Question '+ str(self.ques_num+1) +': '+self.q_set[self.ques_num][0])
                self.quiz_option1.config(text=self.q_set[self.ques_num][1])
                self.quiz_option2.config(text=self.q_set[self.ques_num][2])
                self.quiz_option3.config(text=self.q_set[self.ques_num][3])
                self.quiz_option4.config(text=self.q_set[self.ques_num][4])
                con.commit()
            
            else: #show default
                self.values=self.quiz_tv.item(self.quiz_tv.get_children()[0], 'text')
                self.quizques_frame.place(x=583, y=240)
                self.quizques_frame.grid_propagate(False)

                con = mysql.connector.connect(host='localhost', 
                                            user='root', 
                                            password='rootpass', 
                                            database='all2')

                cur = con.cursor()
                self.q_set=cur.execute('''SELECT ques_title, opA, opB, opC, opD, correct_op FROM quiz WHERE chap_name=%s''', (self.values.replace("Chapter ", ""),))
                self.q_set=cur.fetchall()

                self.ques_num=0
                self.quiz_chapter_title.config(text=self.values)
                self.quiz_question.config(text='Question '+ str(self.ques_num+1) +': '+self.q_set[self.ques_num][0])
                self.quiz_option1.config(text=self.q_set[self.ques_num][1])
                self.quiz_option2.config(text=self.q_set[self.ques_num][2])
                self.quiz_option3.config(text=self.q_set[self.ques_num][3])
                self.quiz_option4.config(text=self.q_set[self.ques_num][4])
                con.commit()

            self.quiz_prev_btn=Button(self.quizques_frame, text='Previous', font=f3, relief=SOLID, cursor='hand2', width=10, command=prev_ques, state=DISABLED)
            self.quiz_prev_btn.grid(row=6, column=0, pady=10, padx=10, sticky=W)

            self.quiz_next_btn=Button(self.quizques_frame, text='Next', font=f3, relief=SOLID, cursor='hand2', width=10, command=next_ques)
            self.quiz_next_btn.grid(row=6, column=2, pady=10, padx=10)

            #show current question 1/5
            self.quiz_ques_num=Label(self.quizques_frame, text='Question '+str(self.ques_num+1)+'/'+str(len(self.q_set)), font=f3, bg='white')
            self.quiz_ques_num.grid(row=6, column=1, pady=10, padx=10, sticky=W)

        #show quiz by default
        show_quizques(e=None)
        self.quiz_tv.bind('<ButtonRelease-1>', show_quizques)

         

        self.quiz_score= 0
        ##show quiz results to user, show score, true false and percentage in messagebox
        def quiz_result():
            self.user_ans= selected_option.get()

            score = str(self.quiz_score)+'/'+str(len(self.q_set))

            tk.messagebox.showinfo('Quiz Result', 'Your score is: '+score+'\n')
            #reset quiz
            self.quiz_score=0
            self.ques_num=0
            self.quiz_chapter_title.config(text=self.values)
            self.quiz_question.config(text='Question '+ str(self.ques_num+1) +': '+self.q_set[self.ques_num][0])
            self.quiz_option1.config(text=self.q_set[self.ques_num][1])
            self.quiz_option2.config(text=self.q_set[self.ques_num][2])
            self.quiz_option3.config(text=self.q_set[self.ques_num][3])
            self.quiz_option4.config(text=self.q_set[self.ques_num][4])
            self.quiz_next_btn.config(text='Next')
            self.quiz_next_btn.config(command=next_ques)
            self.quiz_prev_btn.config(state=DISABLED)
            self.quiz_ques_num.config(text='Question '+str(self.ques_num+1)+'/'+str(len(self.q_set)))


       
        


class Calculator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ui_bg
        ui_bg(self, img_file)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #appointments page btn
        view_appt(self, Appointments, controller)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #Calculator title
        w = Label(self, text ='Calculator', font = ('Arial', 28) , bg=bgc)
        w.pack()
        w.place(x=585, y=90)

        #calculator webview



class Chat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ui_bg
        ui_bg(self, img_file)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #appointments page btn
        view_appt(self, Appointments, controller)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #discussions server treeview scroll
        self.discussions_frame=Frame(self, width=300, height=500, bg=bgc)
        self.discussions_frame.place(x=125, y=100)

        self.discussions_txt=Label(self.discussions_frame, text='Discussions', font=('Arial', 29), bg=bgc)
        self.discussions_txt.grid(row=0, column=0, pady=10)

        self.discussions_tv_frame=Frame(self.discussions_frame, bg=bgc)
        self.discussions_tv_frame.grid(row=1, column=0)

        self.discussions_tv_scroll=Scrollbar(self.discussions_tv_frame)
        self.discussions_tv_scroll.pack(side=RIGHT, fill=Y)

        self.discussions_tv=ttk.Treeview(self.discussions_tv_frame, yscrollcommand=self.discussions_tv_scroll.set, height=15)
        self.discussions_tv.pack()

        self.discussions_tv_scroll.config(command=self.discussions_tv.yview)

        self.discussions_tv.column('#0', width=435, minwidth=435)
        self.discussions_tv.heading('#0', text='Discussion Servers', anchor=W)

        #insert server name
        self.discussions_tv.insert(parent='', index='end', iid=0, text='Computer Architecture & Networks')

        #chat msg screen
        self.chat_scrolledtxt=scrolledtext.ScrolledText(self,width=58,height=21,bg='white', relief=SOLID, bd=2, font=f, wrap=WORD)
        self.chat_scrolledtxt.place(x=650, y=115)

        #chat msg input entry
        #frame
        self.chat_entry_frame=Frame(self, width=675, height=50, bg=bgc)
        self.chat_entry_frame.place(x=641, y=600)

        self.chat_entry=Text(self.chat_entry_frame, height=5,width=52, font=f, wrap=WORD,relief=SOLID, bd=2)
        self.chat_entry.grid(row=0, column=0, padx=10, pady=5)

        #send btn
        self.send_btn=Button(self.chat_entry_frame, text='Send', font=f, relief=SOLID, bd=2, cursor='hand2')
        self.send_btn.grid(row=0, column=1, padx=10, pady=5)


class Chatbot(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ui_bg
        ui_bg(self, img_file)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #appointments page btn
        view_appt(self, Appointments, controller)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #chatbot title
        self.chtbot_lbl = Label(self, text ='Chatbot', font = ('Arial', 28), bg=bgc)
        self.chtbot_lbl.place(x=600, y=90)



class Appointments(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ui_bg
        ui_bg(self, img_file)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #appointments page btn
        view_appt(self, Appointments, controller)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #Appointments Title
        self.appt_lbl = Label(self, text ='Appointments', font = ('Arial', 28), bg=bgc)
        self.appt_lbl.place(x=600, y=100)

        #make an appointment frame
        #name, email, student id, date, time, lecturer, description
        self.make_appt_frame=Frame(self, width=500, height=500, bg=bgc, relief=SOLID, bd=2)
        self.make_appt_frame.place(x=175, y=180)

        self.make_appt_lbl=Label(self.make_appt_frame, text='Create Appointment', font=('Arial', 20), bg=bgc)
        self.make_appt_lbl.grid(row=0, column=1, pady=10, padx=10, sticky=W, columnspan=5)

        self.name_lbl=Label(self.make_appt_frame, text='Name', font=f, bg=bgc)
        self.name_lbl.grid(row=1, column=0, pady=10, padx=10, sticky=W)

        self.name_entry=Entry(self.make_appt_frame, font=f,  width=22)
        self.name_entry.grid(row=1, column=1, pady=10, padx=10, sticky=W, columnspan=4)

        self.email_lbl=Label(self.make_appt_frame, text='Email', font=f, bg=bgc)
        self.email_lbl.grid(row=2, column=0, pady=10, padx=10, sticky=W)

        self.email_entry=Entry(self.make_appt_frame, font=f,  width=22)
        self.email_entry.grid(row=2, column=1, pady=10, padx=10, sticky=W, columnspan=4)

        self.student_id_lbl=Label(self.make_appt_frame, text='Student ID', font=f, bg=bgc)
        self.student_id_lbl.grid(row=3, column=0, pady=10, padx=10, sticky=W)

        self.student_id_entry=Entry(self.make_appt_frame, font=f, width=22)
        self.student_id_entry.grid(row=3, column=1, pady=10, padx=10, sticky=W, columnspan=4)

        self.date_lbl=Label(self.make_appt_frame, text='Date', font=f, bg=bgc)
        self.date_lbl.grid(row=4, column=0, pady=10, padx=10, sticky=W)

        self.date_entry=DateEntry(self.make_appt_frame, font=f, relief=SOLID, bd=2,state='readonly', background='darkblue', foreground='white', mindate=date.today(), maxdate=date.today()+relativedelta(months=6), date_pattern='dd/mm/yyyy')
        self.date_entry.grid(row=4, column=1, pady=10, padx=10, sticky=W, columnspan=4)

        self.time_lbl=Label(self.make_appt_frame, text='Time', font=f, bg=bgc)
        self.time_lbl.grid(row=5, column=0, pady=10, padx=10, sticky=W)

        self.hr_entry=ttk.Combobox(self.make_appt_frame, font=f,width=5, state='readonly', values=hours)
        self.hr_entry.grid(row=5, column=1, pady=10, padx=5)

        self.hr_lbl=Label(self.make_appt_frame, text='Hours', font=f, bg=bgc)
        self.hr_lbl.grid(row=5, column=2, pady=10, padx=5,sticky=W)

        self.min_entry=ttk.Combobox(self.make_appt_frame, font=f,width=5, state='readonly', values=minutes)
        self.min_entry.grid(row=5, column=3, pady=10, padx=5,sticky=W)

        self.min_lbl=Label(self.make_appt_frame, text='Minutes', font=f, bg=bgc)
        self.min_lbl.grid(row=5, column=4, pady=10, padx=5,sticky=W)

        self.lecturer_lbl=Label(self.make_appt_frame, text='Lecturer', font=f, bg=bgc)
        self.lecturer_lbl.grid(row=6, column=0, pady=10, padx=10, sticky=W)

        self.lecturer_entry=ttk.Combobox(self.make_appt_frame, font=f, width=22, values=['Lect1', 'Lect2'], state='readonly')
        self.lecturer_entry.grid(row=6, column=1, pady=10, padx=10, sticky=W, columnspan=4)

        self.description_lbl=Label(self.make_appt_frame, text='Description', font=f, bg=bgc)
        self.description_lbl.grid(row=7, column=0, pady=10, padx=10, sticky=W)

        self.description_entry=Text(self.make_appt_frame, font=f, width=22, height=4, wrap=WORD)
        self.description_entry.grid(row=7, column=1, pady=10, padx=10, sticky=W, columnspan=4)

        self.submit_btn=Button(self.make_appt_frame, text='Submit', font=f, relief=SOLID, bd=2, cursor='hand2')
        self.submit_btn.grid(row=8, column=2, pady=10, padx=10, columnspan=3, sticky=W)

        #view appointments status frame, treeview
        self.apptstat_lbl=Label(self, text='Appointment Status', font=('Arial', 20), bg=bgc)
        self.apptstat_lbl.place(x=823, y=185)
        
        self.apptstat_frame=Frame(self, bg=bgc)
        self.apptstat_frame.place(x=655, y=235)

        #scrollbar
        self.apptstat_scroll=Scrollbar(self.apptstat_frame)
        self.apptstat_scroll.pack(side=RIGHT, fill=Y)

        self.apptstat_tree=ttk.Treeview(self.apptstat_frame, yscrollcommand=self.apptstat_scroll.set, height=4)
        self.apptstat_tree.pack()

        self.apptstat_scroll.config(command=self.apptstat_tree.yview)

        self.apptstat_tree['columns']= ('Date', 'Time', 'Lecturer', 'Status')

        #format columns
        self.apptstat_tree.column('#0', width=0, stretch=NO)
        self.apptstat_tree.column('Date', anchor=CENTER, width=150, stretch=NO, minwidth=100)
        self.apptstat_tree.column('Time', anchor=CENTER, width=100, stretch=NO, minwidth=100)
        self.apptstat_tree.column('Lecturer', anchor=CENTER, width=200, stretch=NO, minwidth=200)
        self.apptstat_tree.column('Status', anchor=CENTER, width=150, stretch=NO, minwidth=235)

        #column headings
        self.apptstat_tree.heading('#0', text='', anchor=CENTER)
        self.apptstat_tree.heading('Date', text='Date', anchor=CENTER)
        self.apptstat_tree.heading('Time', text='Time', anchor=CENTER)
        self.apptstat_tree.heading('Lecturer', text='Lecturer', anchor=CENTER)
        self.apptstat_tree.heading('Status', text='Status', anchor=CENTER)


        #view lecturer response from post a question in homepage
        self.lec_res_lbl=Label(self, text='Lecturer Response', font=('Arial', 20), bg=bgc)
        self.lec_res_lbl.place(x=823, y=425)

        self.lec_res_frame=Frame(self, bg=bgc)
        self.lec_res_frame.place(x=655, y=471)

        #edit style of treeview
        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Response.Treeview', rowheight=65)
        style.configure('Response.Treeview', font=f)

        #treeview
        self.lec_res_scroll=Scrollbar(self.lec_res_frame)
        self.lec_res_scroll.pack(side=RIGHT, fill=Y)

        self.lec_res_tree=ttk.Treeview(self.lec_res_frame, yscrollcommand=self.lec_res_scroll.set, height=3, style='Response.Treeview')
        self.lec_res_tree.pack()

        self.lec_res_scroll.config(command=self.lec_res_tree.yview)

        self.lec_res_tree['columns']= ('Question', 'Response from Lecturer')

        #format columns
        self.lec_res_tree.column('#0', width=0, stretch=NO)
        self.lec_res_tree.column('Question', anchor=CENTER, width=250, stretch=NO, minwidth=250)
        self.lec_res_tree.column('Response from Lecturer', anchor=CENTER, width=350, stretch=NO, minwidth=350)

        #column headings
        self.lec_res_tree.heading('#0', text='', anchor=CENTER)
        self.lec_res_tree.heading('Question', text='Question', anchor=CENTER)
        self.lec_res_tree.heading('Response from Lecturer', text='Response from Lecturer', anchor=CENTER)

        


class Games(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ui_bg
        ui_bg(self, img_file)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #appointments page btn
        view_appt(self, Appointments, controller)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #games title
        self.games_lbl=Label(self, text='Games', font=('Arial', 28), bg=bgc)
        self.games_lbl.place(x=600, y=100)
        
        #game gif
        gif_file = 'images\games.gif'
        openImage= Image.open(gif_file)

        frames = openImage.n_frames
        imageObj = [PhotoImage(file=gif_file,format=f"gif -index {i}") for i in range(frames)]
        count = 0
        self.showAnimation = None

        def animation(count):
            new_image = imageObj[count]

            self.game_gif_lbl.config(image=new_image)
            count +=1
            if count == frames:
                count = 0
            self.showAnimation = self.after(100,lambda :animation(count))

        self.game_gif_lbl=Label(self, image="")
        self.game_gif_lbl.place(x=150, y=204)

        #start animation for gif
        animation(count)


        #snake game
        # Constants
        WIDTH = 600
        HEIGHT = 400
        DELAY = 100
        SIZE = 20
        DIRECTIONS = {
            "Up": (-1, 0),
            "Down": (1, 0),
            "Left": (0, -1),
            "Right": (0, 1)
        }

        # Game variables
        self.score = 0
        self.direction = "Right"
        self.snake = [(HEIGHT // 2, WIDTH // 2)]
        self.food = ()

        # Function to generate new food
        def generate_food():
            while True:
                x = random.randint(0, HEIGHT // SIZE - 1) * SIZE
                y = random.randint(0, WIDTH // SIZE - 1) * SIZE
                if (x, y) not in self.snake:
                    self.food = (x, y)
                    break

        # Function to update the snake's position
        def move_snake():
            self.start_btn.config(state=DISABLED)
            head_x, head_y = self.snake[0]
            dx, dy = DIRECTIONS[self.direction]
            new_head = ((head_x + dx * SIZE) % HEIGHT, (head_y + dy * SIZE) % WIDTH)

            if new_head in self.snake[1:]:
                game_over()
                return

            self.snake.insert(0, new_head)

            if new_head == self.food:
                self.score += 1
                generate_food()
            else:
                self.snake.pop()

            draw_snake()
            draw_food()
            draw_score()

            self.after(DELAY, move_snake)

        # Function to handle keypress events
        def handle_keypress(event):
            new_direction = event.keysym
            opposites = {
                "Up": "Down",
                "Down": "Up",
                "Left": "Right",
                "Right": "Left"
            }
            if new_direction != opposites[self.direction]:
                self.direction = new_direction

        # Function to draw the snake
        def draw_snake():
            canvas.delete("snake")
            for segment in self.snake:
                x, y = segment
                canvas.create_rectangle(
                    y, x, y + SIZE, x + SIZE, fill="blue", tags="snake"
                )

        # Function to draw the food
        def draw_food():
            canvas.delete("food")
            x, y = self.food
            canvas.create_oval(
                y, x, y + SIZE, x + SIZE, fill="red", tags="food"
            )

        # Function to draw the score
        def draw_score():
            score_label.config(text="Score: " + str(self.score))

        # Function to handle game over
        def game_over(event=None):
            
            # Reset game variables
            self.score = 0
            self.direction = "Right"
            self.snake = [(HEIGHT // 2, WIDTH // 2)]
            generate_food()

            # Clear canvas
            canvas.delete("all")

            # Bind keypress events to handle_keypress function
            canvas.bind("<Key>", handle_keypress)
            canvas.focus_set()

            self.start_btn.config(state=NORMAL)

        
        # Create and pack the canvas
        canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg="white")
        canvas.place(x=685, y=200)

        # Create and pack the score label
        score_label = tk.Label(self, text="Score: 0", font=f3, fg="white", bg="black")
        score_label.place(x=950, y=604)

        # Bind keypress events to handle_keypress function
        canvas.bind("<Key>", handle_keypress)
        canvas.focus_set()

        # button to start game or stop game
        generate_food()
        self.start_btn=Button(self, text='Start Game', font=f3, bg='white', command=move_snake)
        self.start_btn.place(x=929, y=635)



class Profile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global login_details

        # ui_bg
        ui_bg(self, img_file)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #appointments page btn
        view_appt(self, Appointments, controller)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #Profile Title
        self.profile_lbl = Label(self, text ='Profile', font = ('Arial', 28), bg=bgc)
        self.profile_lbl.place(x=600, y=100)

        
        #view profile details
        self.profile_frame=Frame(self, width=500, height=500, bg=bgc, relief=SOLID, bd=2)
        self.profile_frame.place(x=300, y=200)

        #user details: name, id, email
        self.userdetails_lbl = Label(self.profile_frame, text ='User Details', font = ('Arial', 25), bg=bgc)
        self.userdetails_lbl.grid(row=0, column=1, padx=10, pady=10, sticky=W, columnspan=3)

        self.profile_name_lbl=Label(self.profile_frame, text='Name: ', font=f4, bg=bgc)
        self.profile_name_lbl.grid(row=1, column=0, padx=20, pady=10, sticky=W)

        self.profile_id_lbl=Label(self.profile_frame, text='ID: ', font=f4, bg=bgc)
        self.profile_id_lbl.grid(row=1, column=1, padx=20, pady=10, sticky=W)


        self.profile_email_lbl=Label(self.profile_frame, text='Email: ', font=f4, bg=bgc)
        self.profile_email_lbl.grid(row=1, column=2, padx=20, pady=10, sticky=W)


        #change password btn
        self.change_pass_btn=Button(self.profile_frame, text='Change Password', font=f, relief=SOLID, bd=2, cursor='hand2')
        self.change_pass_btn.grid(row=2, column=1, padx=10, pady=10, sticky=W, columnspan=3)


        #view subjects
        self.subjects_frame=Frame(self, width=500, height=500, bg=bgc, relief=SOLID, bd=2)
        self.subjects_frame.place(x=215, y=400)

        self.subjects_lbl=Label(self.subjects_frame, text='Subjects', font=('Arial', 25), bg=bgc)
        self.subjects_lbl.grid(row=0, column=0, padx=10, pady=10,columnspan=2)

        self.year_lbl=Label(self.subjects_frame, text='Year: Diploma Year 1', font=f4, bg=bgc)
        self.year_lbl.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.sem_lbl=Label(self.subjects_frame, text='Semester: 1', font=f4, bg=bgc)
        self.sem_lbl.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        self.sch_lbl = Label(self.subjects_frame, text='School: School of Computing', font=f4, bg=bgc)
        self.sch_lbl.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.programme_lbl = Label(self.subjects_frame, text='Programme: BCSCUN', font=f4, bg=bgc)
        self.programme_lbl.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        self.subj1_lbl = Label(self.subjects_frame, text='Subject 1: Computer Architecture & Networks', font=f4, bg=bgc)
        self.subj1_lbl.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        self.subj2_lbl = Label(self.subjects_frame, text='Subject 2: Programming Fundamentals', font=f4, bg=bgc)
        self.subj2_lbl.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        self.subj3_lbl = Label(self.subjects_frame, text='Subject 3: Web Programming', font=f4, bg=bgc)
        self.subj3_lbl.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        self.subj4_lbl = Label(self.subjects_frame, text='Subject 4: Discrete Mathematics', font=f4, bg=bgc)
        self.subj4_lbl.grid(row=4, column=1, padx=10, pady=10, sticky=W)



        #change password????
        def chg_pw():
            pass




#window
ws=App()
ws.title("INTI Study Helpdesk")
ws.geometry('1380x773+80+5')
ws.resizable(False,False)
ws.mainloop()