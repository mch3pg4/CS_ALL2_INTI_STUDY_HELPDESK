import bcrypt, re, random, io, string
import datetime
from tkcalendar import Calendar
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox, ttk, filedialog, Tk, Label, Entry, Button, END
import tkinter as tk
import tkinter.ttk as ttk
from time import strftime
from datetime import date
import mysql.connector
from mysql.connector import Error
from captcha.image import ImageCaptcha
from tktooltip import ToolTip
from admin import AdminPage
from buttons import clockdate, ui_bg, log_out_btn, toggle_password



f=('Arial', 14)
f2=('Arial', 12)
bgc='#F9D3B9'
img_file='images\Slide4.png'




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

    image7=Image.open('images\\user.png')
    img7=image7.resize((50,50))
    my_img7=ImageTk.PhotoImage(img7)
    profile_icon=Label(image=my_img7)
    profile_icon.image=my_img7

    button1=tk.Button(self, image=my_img2,cursor='hand2',command= lambda:controller.show_frame(Homepage))
    button1.place(x=3, y=100)
    ToolTip(button1, msg='Homepage')

    button2=tk.Button(self, image=my_img3, cursor='hand2',command= lambda:controller.show_frame(Books))
    button2.place(x=3, y=242)
    ToolTip(button2, msg='Books')

    button3=tk.Button(self, image=my_img4,cursor='hand2', command= lambda:controller.show_frame(Quiz))
    button3.place(x=3, y=384)
    ToolTip(button3, msg='Quiz')

    button4=tk.Button(self, image=my_img5,cursor='hand2',command= lambda:controller.show_frame(Calculator))
    button4.place(x=3, y=384+142)
    ToolTip(button4, msg='Calculator')

    button4=tk.Button(self, image=my_img6,cursor='hand2',command= lambda:controller.show_frame(Chat))
    button4.place(x=3, y=384+284)
    ToolTip(button4, msg='Discussions')

    button5=tk.Button(self, image=my_img7, cursor='hand2',command=lambda: controller.show_frame(Profile))
    button5.place(x=1225, y=5)
    ToolTip(button5, msg='Profile')



# #logout button 
# def log_out_btn(self, controller):
#     def logout():
#         controller.show_frame(Loginpage)
#         messagebox.showinfo('Logout Status', 'Logged out successfully!')

#     image8=Image.open('images\\logout.png')
#     img8=image8.resize((50,50))
#     my_img8=ImageTk.PhotoImage(img8)
#     logout_icon=Label(image=my_img8)
#     logout_icon.image=my_img8

#     logout_btn=tk.Button(self, image=my_img8,cursor='hand2', command=logout)
#     logout_btn.place(x=1300,y=5)
#     ToolTip(logout_btn, msg='Logout')




class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

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

        for F in (Loginpage, RegisterPage, RegisterCourses, AdminPage,Homepage, Subject1, Books, Quiz, Calculator, Chat, Profile):
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


    # def updateProfile(self, login_details):
    #     frame = self.frames[Profile]
    #     frame.lbl_welcome.config(text='Welcome, '+ login_details[0])
    #     frame.lbl_name.config(text=login_details[0])
    #     frame.lbl_email.config(text=login_details[2])
    #     frame.lbl_contact.config(text=str(login_details[3]))
    #     frame.lbl_gender.config(text=login_details[5])
    #     frame.tkraise()


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
                    if bcrypt.checkpw(upwd.encode('utf-8'),login_details[5].encode('utf-8')) & (login_details[4]== 'Student'):
                        controller.show_frame(Homepage)
                    # messagebox.showinfo('Login Status', 'Logged in Successfully!')
                    # controller.updateProfile( login_details)
                    # controller.updateHomepage(login_details)
                    # controller.updateAdmin(login_details)
                    elif bcrypt.checkpw(upwd.encode('utf-8'),login_details[5].encode('utf-8')) & (login_details[4]== 'Lecturer'):
                        controller.show_frame(AdminPage)
                    else:
                        messagebox.showerror('Login Status', 'invalid username or password')
            else:
                messagebox.showerror('Error', warn)

     
        # widgets
        self.left_frame = Frame(self, bd=2, bg='salmon',   relief=SOLID, padx=10, pady=-1000)
        Label(self.left_frame, text="Email", bg='salmon',font=f).grid(row=0, column=0, sticky=W, pady=10)
        Label(self.left_frame, text="Password", bg='salmon',font=f).grid(row=1, column=0, pady=10)
        self.email_tf = Entry(self.left_frame, font=f)
        self.email_tf.insert(0, 'brad@gmail.com')   #default value for testing

        self.pwd_tf = Entry(self.left_frame, font=f, show='*')    #default value for testing
        self.pwd_tf.insert(0, 'Brad,123')
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
        global image_display, image_label
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
            global image_display, image_label
            
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
                    messagebox.showinfo('Register', 'Account Created Successfully!')
                    if self.user_var.get()== 'Lecturer':
                        controller.show_frame(AdminPage)
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
        
        #optionmenu values
        level=['Select','Degree']
        year=['Select','1','2','3','4']
        school=['Select','School of Computing']
        program=['Select','BCSCUN','BCTCUN']
        semester=['Select','1','2','3']
        subjects=['Select','Computer Architecture & Networks', 'Objected Oriented Programming', 'Mathematics for Computer Science', 'Database Systems', 'Programming & Algorithms']
        
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
        #logout btn
        log_out_btn(self,Loginpage, controller)

        #Subject title
        self.subj1_title = Label(self, text ='Computer Architecture & Networks', font = ('Arial', 28), bg=bgc )
        self.subj1_title.pack()
        self.subj1_title.place(x=350, y=100)


        
        
    

class Books(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ui_bg
        ui_bg(self, img_file)
       
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #Books Title
        w = Label(self, text ='Books', font = ('Arial', 28), bg='antique white' )
        w.pack()
        w.place(x=445, y=120)

        #view books
        #list down available books
        #recent books
        #search books 
        #by category



class Quiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ui_bg
        ui_bg(self, img_file)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #Quiz title
        w = Label(self, text ='Quiz', font = ('Arial', 28) , bg='antique white')
        w.pack()
        w.place(x=480, y=100)

        #view quiz
        #list down all quiz


class Calculator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ui_bg
        ui_bg(self, img_file)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #Calculator title
        w = Label(self, text ='Calculator', font = ('Arial', 28) , bg='antique white')
        w.pack()
        w.place(x=465, y=100)

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
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #Calculator title
        w = Label(self, text ='Chat', font = ('Arial', 28) , bg='antique white')
        w.pack()
        w.place(x=465, y=100)

        #websockets chat server



class Profile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='antique white')
        global login_details

        # ui_bg
        ui_bg(self, img_file)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #logout btn
        log_out_btn(self, Loginpage, controller)

        #Profile Title
        w = Label(self, text ='Profile', font = ('Arial', 28), bg='antique white')
        w.pack()
        w.place(x=500, y=100)

        #edit profile details
        #view profile details
        #change password????




#window
ws=App()
ws.title("INTI Study Helpdesk")
ws.geometry('1380x773+80+5')
ws.resizable(False,False)
ws.mainloop()