from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox, Label
import tkinter as tk
from time import strftime
from tktooltip import ToolTip


f=('Arial', 14)
f2=('Arial', 12)
f3=('Arial', 16)
bgc='#F9D3B9'

#clock and date
def clockdate(self):
    
    def my_time():
        time_string = strftime('%H:%M:%S %p %a %d/%m/%Y') # time format 
        l1.config(text=time_string)
        l1.after(1000,my_time) # time delay of 1000 milliseconds 

    
    l1=tk.Label(self,font=('Arial', 19, 'bold'),bg=bgc, foreground='black')
    l1.place(x=605, y=12)
    my_time()

#ui background with inti logo
def ui_bg(self, image_file):
    self.raw_image=Image.open(image_file)
    self.img=self.raw_image.resize((1240,773),Image.LANCZOS)
    self.background_image=ImageTk.PhotoImage(self.raw_image)
    self.background_label = tk.Label(self, image=self.background_image)
    self.background_label.place(x=-5,y=-5)
    self.background_label.image = self.background_image


#toggle show/hide password function
def toggle_password(pwd_tf, pwd_btn):
    if pwd_tf.cget('show') == '':
        pwd_tf.config(show='*')
        pwd_btn.config(text='Show',cursor= "hand2")
    else:
        pwd_tf.config(show='')
        pwd_btn.config(text='Hide',cursor= "hand2")

#admin buttons
def admin_btns(self, frame1, frame2, frame3, frame4, frame5, frame6, controller):
    #admin page title
    self.admin_title=tk.Label(self, text='Lecturer Page', font=('Helvetica', 18, 'bold'), bg=bgc)
    self.admin_title.place(x=410, y=13)

    #show list of students from db
    #show list of students btn
    self.showstudents_btn=tk.Button(self, text='Students', font=f3, width=14,  cursor='hand2', command=lambda:controller.show_frame(frame1)) 
    self.showstudents_btn.place(x=47, y=100)

    #add/delete/view books
    #books button
    self.books_btn=tk.Button(self, text='Books', font=f3, width=14,  cursor='hand2', command=lambda:controller.show_frame(frame2))
    self.books_btn.place(x=47*5.5, y=100)


    #add/edit/delete quiz
    #quiz button
    self.quiz_btn=tk.Button(self, text='Quiz', font=f3,width=14,   cursor='hand2', command=lambda:controller.show_frame(frame3))
    self.quiz_btn.place(x=47*10, y=100)

    #chat discussions
    #chat button
    self.chat_btn=tk.Button(self, text='Discussions', font=f3, width=14,  cursor='hand2', command=lambda:controller.show_frame(frame4))
    self.chat_btn.place(x=47*14.5, y=100)

    #add/delete/view course materials
    #course materials button
    self.coursematerials_btn=tk.Button(self, text='Course Materials', font=f3,width=14,   cursor='hand2', command=lambda:controller.show_frame(frame5))
    self.coursematerials_btn.place(x=47*19.15, y=100)

    #view appointments
    #appointments button
    self.appointments_btn=tk.Button(self, text='Appointments', font=f3,width=14,   cursor='hand2', command=lambda:controller.show_frame(frame6))
    self.appointments_btn.place(x=47*23.75, y=100)

#back button
def back_btn(self,frame, controller):
    controller.show_frame(frame)

    self.back_btn=tk.Button(self, text='< Back', font=f, width=7, cursor='hand2', command=lambda:controller.show_frame(frame))
    self.back_btn.place(x=90, y=105)

#expand, collapse treeview children nodes
def expand_tv(tree):
    for node in tree.get_children():
        tree.item(node, open=True)

def collapse_tv(tree):
    for node in tree.get_children():
        tree.item(node, open=False)

#appointments page btn
def view_appt(self, frame, controller):
    image=Image.open('images\\notification.png')
    img=image.resize((50,50))
    my_img=ImageTk.PhotoImage(img)
    noti_icon=Label(image=my_img)
    noti_icon.image=my_img

    appt_btn=tk.Button(self,image=my_img, cursor='hand2', command=lambda:controller.show_frame(frame))
    appt_btn.place(x=1150, y=5)
    ToolTip(appt_btn, msg='Appointments & Notifications')


#view as student button
def view_user(self, frame, controller):
    image=Image.open('images\\student.png')
    img=image.resize((50,50))
    my_img=ImageTk.PhotoImage(img)
    student_icon=Label(image=my_img)
    student_icon.image=my_img

    viewuser_btn=tk.Button(self,image=my_img, cursor='hand2', command=lambda:controller.show_frame(frame))
    viewuser_btn.place(x=1225, y=5)
    ToolTip(viewuser_btn, msg='View as Student')



#logout button 
def log_out_btn(self, frame, controller):
    def logout():
        controller.show_frame(frame)
        messagebox.showinfo('Logout Status', 'Logged out successfully!')

    image8=Image.open('images\\logout.png')
    img8=image8.resize((50,50))
    my_img8=ImageTk.PhotoImage(img8)
    logout_icon=Label(image=my_img8)
    logout_icon.image=my_img8

    logout_btn=tk.Button(self, image=my_img8,cursor='hand2', command=logout)
    logout_btn.place(x=1300,y=5)
    ToolTip(logout_btn, msg='Logout')