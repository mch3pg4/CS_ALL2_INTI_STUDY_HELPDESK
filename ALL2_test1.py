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
import random, io, string
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
        raw_image=Image.open("images\Slide1.png")
        background_image=ImageTk.PhotoImage(raw_image)
        background_label = tk.Label(self, image=background_image)
        background_label.place(x=-215,y=-155)
        background_label.image = background_image


        #direct to register page for new users
        def go_to_register():
            controller.show_frame(RegisterPage)
        register_link_btn = Button(self, text= "New user? Go to Register Page", cursor= "hand2", font= ('Arial', 14), command=go_to_register)
        register_link_btn.place(x=830,y=500)
        
                
        def login_response():
            global login_details
            try:
                uname = email_tf.get()
                upwd = pwd_tf.get()
                con = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="rootpass",
                                    database="all2") 
                c = con.cursor()
                c.execute("SELECT * FROM userdata WHERE email=%s AND password=%s",(uname,upwd))
                
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
                    # messagebox.showinfo('Login Status', 'Logged in Successfully!')
                    # controller.updateProfile( login_details)
                    # controller.updateHomepage(login_details)
                    # controller.updateAdmin(login_details)
                    # if login_details[4]== 'Lecturer':
                    #     controller.show_frame(Adminpage)
                    # else:
                        controller.show_frame(Homepage)
                
                else:
                    messagebox.showerror('Login Status', 'invalid username or password')
            else:
                messagebox.showerror('Error', warn)

     
        # widgets
        left_frame = Frame(self, bd=2, bg='salmon',   relief=SOLID, padx=10, pady=-1000)
        Label(left_frame, text="Email", bg='salmon',font=f).grid(row=0, column=0, sticky=W, pady=10)
        Label(left_frame, text="Password", bg='salmon',font=f).grid(row=1, column=0, pady=10)
        email_tf = Entry(left_frame, font=f)
        email_tf.insert(0, 'm')   #default value for testing
        #show/hide password
        def toggle_password():
            if pwd_tf.cget('show') == '':
                pwd_tf.config(show='*')
                pwd_btn.config(text='Show',cursor= "hand2")
            else:
                pwd_tf.config(show='')
                pwd_btn.config(text='Hide',cursor= "hand2")

        pwd_tf = Entry(left_frame, font=f, show='*')    #default value for testing
        pwd_tf.insert(0, 'm')
        pwd_btn=Button(self, text='Show', width=4, font=('Arial', 9), cursor= "hand2",command=toggle_password)
        pwd_btn.place(x=1093, y=382)
        
        login_btn = Button(left_frame, width=15, text='Login', font=f, relief=SOLID,cursor='hand2',command=login_response)

        # widgets placement
        email_tf.grid(row=0, column=1, pady=10, padx=20)
        pwd_tf.grid(row=1, column=1, pady=10, padx=20)
        login_btn.grid(row=2, column=1, pady=10, padx=20)
        left_frame.place(x=785, y=320)
   

class RegisterPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        global image_display, image_label
        # registerpage bg
        raw_image=Image.open("images\Slide2.png")
        background_image=ImageTk.PhotoImage(raw_image)
        background_label = tk.Label(self, image=background_image)
        background_label.place(x=-215,y=-155)
        background_label.image = background_image

        #direct to register page for new users
        def go_to_login():
            controller.show_frame(Loginpage)

        login_link_btn = Button(self, text= "Go to Login Page", cursor= "hand2", font= ('Arial', 14), command=go_to_login)
        login_link_btn.place(x=900,y=720)
        
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
                                                            password varchar(45) NOT NULL)''')
        con.commit()

        var1=StringVar()
        var1.set(None)



        def createImage(flag=0): 
            global image_display, image_label
            
            # Generate new random string for captcha
            self.random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

            # create captcha image
            image_captcha = ImageCaptcha(width=200, height=55)
            image_generated = image_captcha.generate(self.random_string)
            image_display = ImageTk.PhotoImage(Image.open(image_generated))
            
            #executed when pressed reload captcha button
            if flag == 1:
                # Remove previous Image (if present) and display new one
                image_label.config(image=image_display)


        def insert_record():

            check_counter=0
            warn = " "
            if register_name.get() == "":
                warn = 'Please enter a name.'
            else:
                check_counter += 1
            
            if register_userid.get() == "":
                warn='Please enter student ID.'
            else:
                check_counter += 1

            if register_email.get() == "":
                warn = 'Please enter a valid email.'
            else:
                check_counter += 1

            if var1.get() == 'None':
                warn = 'Select User Type'
            else:
                check_counter += 1

            if register_pwd.get() == "":
                warn = 'Please enter a password.'
            else:
                check_counter += 1

            if pwd_again.get() == "":
                warn = 'Please re-enter your password.'
            else:
                check_counter += 1

            if register_pwd.get() != pwd_again.get():
                warn = 'Your passwords do not match!'
            else:
                check_counter += 1

            if reg_captcha.get() != self.random_string:
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
                    name= register_name.get()
                    user_id= register_userid.get()
                    email= register_email.get()
                    usertype= var1.get()
                    password= register_pwd.get() 
                    
                    insert_data = ("INSERT INTO userdata(iduserdata, name, user_id, email, usertype, password) VALUES (%s,%s,%s,%s,%s,%s);")
                    data= (iduserdata, name, user_id, email, usertype, password)
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
        reg_frame = Frame(self, bd=2, bg='salmon',relief=SOLID, padx=10, pady=-1000)
        Label(reg_frame, text="Name", bg='salmon',font=f).grid(row=0, column=0, sticky=W, pady=10, padx=10)
        Label(reg_frame, text="ID", bg='salmon',font=f).grid(row=1, column=0, sticky=W, pady=10, padx=10)
        Label(reg_frame, text="Email", bg='salmon',font=f).grid(row=2, column=0, sticky=W, pady=10, padx=10)
        Label(reg_frame,text="User Type",bg='salmon',font=f).grid(row=3, column=0, sticky =W, pady=10, padx=10)
        Label(reg_frame, text="Enter Password", bg='salmon',font=f).grid(row=4, column=0, sticky=W, pady=10, padx=10)
        Label(reg_frame, text="Re-Enter Password", bg='salmon',font=f ).grid(row=5, column=0, sticky=W, pady=10)
        Label(reg_frame, text="Enter Captcha", bg='salmon',font=f ).grid(row=6, column=0, sticky=W, pady=10)
        image_label = Label(reg_frame, image=image_display)
        image_label.grid(row=6, column=1,padx=10, pady=10)
        image_label.image=image_display
        
        
        #show/hide password
        def toggle_password2():
            if register_pwd.cget('show') == '':
                register_pwd.config(show='*')
                pwd_btn2.config(text='Show')
            else:
                register_pwd.config(show='')
                pwd_btn2.config(text='Hide')

        register_pwd = Entry(reg_frame, font=f, show='*')
        pwd_btn2=Button(self, text='Show', width=4, font=('Arial', 9),  cursor= "hand2", command=toggle_password2)
        pwd_btn2.place(x=1139, y=432)

        def toggle_password3():
            if pwd_again.cget('show') == '':
                pwd_again.config(show='*')
                pwd_btn3.config(text='Show')
            else:
                pwd_again.config(show='')
                pwd_btn3.config(text='Hide')

        pwd_again = Entry(reg_frame, font=f, show='*')
        pwd_btn3=Button(self, text='Show', width=4, font=('Arial', 9), cursor= "hand2", command=toggle_password3)
        pwd_btn3.place(x=1139, y=480)

        

        #reload button for captcha
        reload_button = Button(self, text='Reload',font=('Arial', 9), cursor='hand2',command=lambda: createImage(1))
        reload_button.place(x=1130, y=606)

        
        usertype_frame = LabelFrame(reg_frame,bg='#CCCCCC',padx=10, pady=10)
        register_name = Entry(reg_frame, font=f)
        register_userid = Entry(reg_frame,font=f)
        register_email = Entry(reg_frame, font=f)
        student_rb = Radiobutton(usertype_frame,text='Student',bg='#CCCCCC',variable=var1,value='Student',font=('Arial',10))
        lect_rb = Radiobutton(usertype_frame,text='Lecturer',bg='#CCCCCC',variable=var1,value='Lecturer',font=('Arial',10))
        register_pwd = Entry(reg_frame, font=f,show='*')
        pwd_again = Entry(reg_frame, font=f,show='*')
        reg_captcha= Entry(reg_frame, font=f)
        register_btn = Button(reg_frame, width=15, text='Register', font=f, relief=SOLID,cursor='hand2',command= insert_record)

        #widgets placement
        register_name.grid(row=0, column=1, pady=10, padx=20)
        register_userid.grid(row=1, column=1, pady=10, padx=20)
        register_email.grid(row=2, column=1, pady=10, padx=20) 
        register_pwd.grid(row=4, column=1, pady=10, padx=20)
        pwd_again.grid(row=5, column=1, pady=10, padx=20)
        reg_captcha.grid(row=7, column=1, pady=10, padx=20)
        register_btn.grid(row=8, column=1, pady=10, padx=20)
        reg_frame.place(x=750, y=205)

        usertype_frame.grid(row=3, column=1, pady=10, padx=20)
        student_rb.pack(expand=True, side=LEFT)
        lect_rb.pack(expand=True, side=LEFT)


        
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
        viewuser_btn=tk.Button(self,height=1, width=10, font=f, command=view_user, text='View as User')
        viewuser_btn.place(x=945, y=135)

        #Logout
        def log_out():
            controller.show_frame(Loginpage)
            messagebox.showinfo('Logout Status', 'Logged out successfully!')
        logout_btn=tk.Button(self, height=1, width=9, font=f, command=log_out, text='Logout')
        logout_btn.place(x=950 ,y=180)
        


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
ws.geometry('1240x773')
ws.resizable(False,False)

ws.mainloop()