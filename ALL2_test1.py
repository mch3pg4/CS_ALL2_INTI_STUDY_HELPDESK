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



f=('Arial', 14)


#inti logo
def inti_logo(self):
    image=Image.open('images\INTI_Logo.png')
    img=image.resize((220,50))
    my_img=ImageTk.PhotoImage(img)
    intilogo = tk.Label(self, image=my_img)
    intilogo.place(x=0, y=5)
    intilogo.image = my_img


#clock and date day
def clockdate(self):
    
    def my_time():
        time_string = strftime('%H:%M:%S %p %a %d/%m/%Y') # time format 
        l1.config(text=time_string)
        l1.after(1000,my_time) # time delay of 1000 milliseconds 

    l1=tk.Label(self,font=('Arial', 19, 'bold'),bg='antique white', foreground='black')
    l1.place(x=750, y=12)
    my_time()



#top buttons
def top_buttons(self, controller):
    button1=tk.Button(self, height=1, width= 12, text="Homepage", font=f,command= lambda:controller.show_frame(Homepage))
    button1.place(x=230, y=75)

    button2=tk.Button(self, height=1, width=12, text="Announcements", font=f, command= lambda:controller.show_frame(Announcements))
    button2.place(x=230*1.75, y=75)

    button3=tk.Button(self, height=1, width=12, text="Events", font=f,command= lambda:controller.show_frame(Events))
    button3.place(x=230*2.5, y=75)

    button4=tk.Button(self, height=1, width=12, text="Competitions", font=f,command= lambda:controller.show_frame(Competitions))
    button4.place(x=230*3.25, y=75)

    button5=tk.Button(self, height=1, width=12, text="Profile", font=f, command=lambda: controller.show_frame(Profile))
    button5.place(x=230*4, y=75)

#toggle show/hide password function
def toggle_password(pwd_tf, pwd_btn):
    if pwd_tf.cget('show') == '':
        pwd_tf.config(show='*')
        pwd_btn.config(text='Show',cursor= "hand2")
    else:
        pwd_tf.config(show='')
        pwd_btn.config(text='Hide',cursor= "hand2")





#logout button 
def log_out_btn(self, controller):
    def logout():
        controller.show_frame(Loginpage)
        messagebox.showinfo('Logout Status', 'Logged out successfully!')
    logout_btn=tk.Button(self, height=1, width=7, font=f, command=logout, text='Logout')
    logout_btn.place(x=1120 ,y=10)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #create frame and assign it to container
        container = tk.Frame(self)

        container.pack(fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #create app icon
        iconpic = PhotoImage(file='images\inti_icon.png')
        self.iconphoto(False,iconpic)

        #create dictionary of frames
        self.frames={}

        for F in (Loginpage, RegisterPage, Adminpage,Homepage, Announcements, Events, Competitions, Profile):
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
        self.register_link_btn.place(x=830,y=500)
        
                
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
                    if bcrypt.checkpw(upwd.encode('utf-8'),login_details[5].encode('utf-8')):
                        controller.show_frame(Homepage)
                    # messagebox.showinfo('Login Status', 'Logged in Successfully!')
                    # controller.updateProfile( login_details)
                    # controller.updateHomepage(login_details)
                    # controller.updateAdmin(login_details)
                    # if login_details[4]== 'Lecturer':
                    #     controller.show_frame(Adminpage)
                    # else:
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
        self.pwd_btn.place(x=1093, y=382)
        
        self.login_btn = Button(self.left_frame, width=15, text='Login', font=f, relief=SOLID,cursor='hand2',command=login_response)

        # widgets placement
        self.email_tf.grid(row=0, column=1, pady=10, padx=20)
        self.pwd_tf.grid(row=1, column=1, pady=10, padx=20)
        self.login_btn.grid(row=2, column=1, pady=10, padx=20)
        self.left_frame.place(x=785, y=320)
   

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
        self.login_link_btn.place(x=900,y=720)
        
        #connect to database
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="rootpass",
                                      database="all2")             
      
        cur=con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS userdata( iduserdata INT AUTO_INCREMENT PRIMARY KEY,
                                                            name varchar(70) NOT NULL,
                                                            user_id varchar(45) NOT NULL UNIQUE, 
                                                            email varchar(45) NOT NULL, 
                                                            usertype text NOT NULL, 
                                                            password varchar(256) NOT NULL)''')
        con.commit()

        self.user_var=StringVar()
        self.user_var.set(None)



        def createImage(flag=0): 
            global image_display, image_label
            
            # Generate new random string for captcha
            self.random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

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
                    controller.show_frame(Loginpage)

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
        self.pwd_btn2.place(x=1139, y=432)

        self.pwd_again = Entry(self.reg_frame, font=f, show='*')
        self.pwd_btn3=Button(self, text='Show', width=4, font=('Arial', 9), cursor= "hand2", command=lambda:toggle_password(self.pwd_again, self.pwd_btn3))
        self.pwd_btn3.place(x=1139, y=480)

        #reload button for captcha
        self.reload_button = Button(self, text='Reload',font=('Arial', 9), cursor='hand2',command=lambda: createImage(1))
        self.reload_button.place(x=1130, y=606)

        #widgets
        self.usertype_frame = LabelFrame(self.reg_frame,bg='#CCCCCC',padx=10, pady=10)
        self.register_name = Entry(self.reg_frame, font=f)
        self.register_userid = Entry(self.reg_frame,font=f)
        self.register_email = Entry(self.reg_frame, font=f)
        self.student_rb = Radiobutton(self.usertype_frame,text='Student',bg='#CCCCCC',variable=self.user_var,value='Student',font=('Arial',10))
        self.lect_rb = Radiobutton(self.usertype_frame,text='Lecturer',bg='#CCCCCC',variable=self.user_var,value='Lecturer',font=('Arial',10))
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
        self.reg_frame.place(x=750, y=205)

        self.usertype_frame.grid(row=3, column=1, pady=10, padx=20)
        self.student_rb.pack(expand=True, side=LEFT)
        self.lect_rb.pack(expand=True, side=LEFT)


        
class Adminpage(tk.Frame):
    def __init__(self,parent, controller):
        global login_details
        tk.Frame.__init__(self,parent,bg='AntiqueWhite1')
    
        #inti logo
        # inti_logo(self)

        #show admin date and clock
        # adminclock(self)

        #admin view as normal user
        def view_user():
            controller.show_frame(Homepage)
        self.viewuser_btn=tk.Button(self,height=1, width=10, font=f, command=view_user, text='View as User')
        self.viewuser_btn.place(x=945, y=135)

        #Logout
        def log_out():
            controller.show_frame(Loginpage)
            messagebox.showinfo('Logout Status', 'Logged out successfully!')
        self.logout_btn=tk.Button(self, height=1, width=9, font=f, command=log_out, text='Logout')
        self.logout_btn.place(x=950 ,y=180)
        


class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='antique white')
        self.controller=controller 
        global login_details

        #inti logo
        inti_logo(self)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #logout btn
        log_out_btn(self,controller)

        #Homepage
        #Homepage title
        w = Label(self, text ='Homepage', font = ('Arial', 28) , bg='antique white')
        w.pack()
        w.place(x=480, y=100)
        
    

class Announcements(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='antique white')


        #inti logo
        inti_logo(self)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #logout btn
        log_out_btn(self,controller)

        #Announcements Title
        w = Label(self, text ='Announcements', font = ('Arial', 28), bg='antique white' )
        w.pack()
        w.place(x=445, y=100)



class Events(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='antique white')
        
        #inti logo
        inti_logo(self)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #logout btn
        log_out_btn(self,controller)

        #Events title
        w = Label(self, text ='Events', font = ('Arial', 28) , bg='antique white')
        w.pack()
        w.place(x=480, y=100)



class Competitions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='antique white')


        #inti logo
        inti_logo(self)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #logout btn
        log_out_btn(self,controller)

        #Competitions title
        w = Label(self, text ='Competitions', font = ('Arial', 28) , bg='antique white')
        w.pack()
        w.place(x=465, y=100)

        

class Profile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='antique white')
        global login_details

        #inti logo
        inti_logo(self)
        #top buttons
        top_buttons(self,controller)
        #show date and clock
        clockdate(self)
        #logout btn
        log_out_btn(self,controller)

        #Profile Title
        w = Label(self, text ='Profile', font = ('Arial', 28), bg='antique white')
        w.pack()
        w.place(x=500, y=100)

        
        





#window
ws=App()
ws.title("INTI Study Helpdesk")
ws.geometry('1240x773+150+5')
ws.resizable(False,False)

ws.mainloop()