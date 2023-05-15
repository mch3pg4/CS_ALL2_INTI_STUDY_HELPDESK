# import bcrypt, re, random, io, string
# import datetime
# from tkcalendar import Calendar
# from tkinter import *
# from PIL import Image,ImageTk
# from tkinter import messagebox, ttk, filedialog, Tk, Label, Entry, Button, END
# import tkinter as tk
# import tkinter.ttk as ttk
# from time import strftime
# from datetime import date
# import mysql.connector
# from mysql.connector import Error
# from captcha.image import ImageCaptcha
# from buttons import clockdate, ui_bg, log_out_btn
# from ALL2_test1 import top_buttons, Subject1, Loginpage

# f=('Arial', 14)
# f2=('Arial', 12)
# bgc='#F9D3B9'
# img_file='images\Slide4.png'


# class Homepage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller=controller 
#         global login_details

#         # ui_bg
#         ui_bg(self, img_file)
#         #top buttons
#         top_buttons(self,controller)
#         #show date and clock
#         clockdate(self)
#         #logout btn
#         log_out_btn(self, Loginpage, controller)

#         #Recent Courses Title
#         self.courses_lbl = Label(self, text ='Recent Courses', font = ('Arial', 28), bg=bgc)
#         self.courses_lbl.pack()
#         self.courses_lbl.place(x=380, y=100)

#         #courses frame
#         self.courses_frame = Frame(self, bg=bgc,relief=SOLID)
#         self.courses_frame.place(x=99, y=155)


#         #Courses button with images
#         image9=Image.open('images\comp_arch.png')
#         img9=image9.resize((170,150))
#         my_img9=ImageTk.PhotoImage(img9)
#         comp_arch_img=Label(image=my_img9)
#         comp_arch_img.image=my_img9

#         self.course1_btn = Button(self.courses_frame, image=my_img9, cursor='hand2', command=lambda: controller.show_frame(Subject1))
#         self.course1_btn.grid(row=0, column=0, padx=10, pady=10)

#         self.course1_lbl = Label(self.courses_frame, text ='Computer Architecture & Networks', wraplength=200,font = f, bg=bgc)
#         self.course1_lbl.grid(row=1, column=0, padx=10)

#         image10=Image.open('images\programming.png')
#         img10=image10.resize((170,150))
#         my_img10=ImageTk.PhotoImage(img10)
#         oop_img=Label(image=my_img10)
#         oop_img.image=my_img10

#         self.course2_btn = Button(self.courses_frame, image=my_img10, cursor='hand2', state='disabled' )
#         self.course2_btn.grid(row=0, column=1, padx=10, pady=10)

#         self.course2_lbl = Label(self.courses_frame, text ='Programming & Algorithms', wraplength=200, font =f, bg=bgc)
#         self.course2_lbl.grid(row=1, column=1, padx=10)

#         image11=Image.open('images\maths_for_cs.png')
#         img11=image11.resize((170,150))
#         my_img11=ImageTk.PhotoImage(img11)
#         maths_img=Label(image=my_img11)
#         maths_img.image=my_img11

#         self.course3_btn = Button(self.courses_frame, image=my_img11, cursor='hand2', state='disabled' )
#         self.course3_btn.grid(row=0, column=2, padx=10, pady=10)

#         self.course3_lbl = Label(self.courses_frame, text ='Mathematics for Computer Science',  wraplength=200, font =f, bg=bgc)
#         self.course3_lbl.grid(row=1, column=2, padx=10)

#         image12=Image.open('images\database.png')
#         img12=image12.resize((170,150))
#         my_img12=ImageTk.PhotoImage(img12)
#         db_img=Label(image=my_img12)
#         db_img.image=my_img12

#         self.course4_btn = Button(self.courses_frame, image=my_img12, cursor='hand2', state='disabled' )
#         self.course4_btn.grid(row=0, column=3, padx=10, pady=10)

#         self.course4_lbl = Label(self.courses_frame, text ='Database Systems',  wraplength=200, font =f, bg=bgc)
#         self.course4_lbl.grid(row=1, column=3, padx=10)


#         #Recent Books Title
#         self.books_lbl = Label(self, text ='Recent Books', font = ('Arial', 28), bg=bgc)
#         self.books_lbl.pack()
#         self.books_lbl.place(x=385, y=420)

#         #books frame
#         self.books_frame = Frame(self, bg=bgc,relief=SOLID)
#         self.books_frame.place(x=99, y=475)

#         #Books button with images (books need to be taken from db)
#         image13=Image.open('books\computer-organization-and-architecture.png')
#         img13=image13.resize((150,180))
#         my_img13=ImageTk.PhotoImage(img13)
#         book1_img=Label(image=my_img13)
#         book1_img.image=my_img13

#         self.book1_btn = Button(self.books_frame,image= my_img13, cursor='hand2')
#         self.book1_btn.grid(row=0, column=0, padx=10, pady=10)

#         self.book1_lbl=Label(self.books_frame, text='Computer Organization & Architecture', wraplength=195, font=f, bg=bgc)
#         self.book1_lbl.grid(row=1, column=0, padx=10)

#         image14=Image.open('books\ObjectOrientedProgramminginC4thEdition.png')
#         img14=image14.resize((150,180))
#         my_img14=ImageTk.PhotoImage(img14)
#         book2_img=Label(image=my_img14)
#         book2_img.image=my_img14

#         self.book2_btn = Button(self.books_frame, image=my_img14, cursor='hand2')
#         self.book2_btn.grid(row=0, column=1, padx=10, pady=10)

#         self.book2_lbl = Label(self.books_frame, text ='Objected Oriented Programming', wraplength=195, font =f, bg=bgc)
#         self.book2_lbl.grid(row=1, column=1, padx=10)

#         image15=Image.open('books\\rosen_discrete_mathematics_and_its_applications_7th_edition.png')
#         img15=image15.resize((150,180))
#         my_img15=ImageTk.PhotoImage(img15)
#         book3_img=Label(image=my_img15)
#         book3_img.image=my_img15

#         self.book3_btn = Button(self.books_frame, image=my_img15, cursor='hand2')
#         self.book3_btn.grid(row=0, column=2, padx=10, pady=10)

#         self.book3_lbl = Label(self.books_frame, text ='Discrete Mathematics and its Applications', wraplength=195, font =f, bg=bgc)
#         self.book3_lbl.grid(row=1, column=2, padx=10)

#         image16=Image.open('books\Computer Architecture, Sixth Edition_ A_Quantitative_Approach.png')
#         img16=image16.resize((150,180))
#         my_img16=ImageTk.PhotoImage(img16)
#         book4_img=Label(image=my_img16)
#         book4_img.image=my_img16

#         self.book4_btn = Button(self.books_frame,image=my_img16, cursor='hand2')
#         self.book4_btn.grid(row=0, column=3, padx=10, pady=10)

#         self.book4_lbl = Label(self.books_frame, text ='Computer Architecture', wraplength=195, font =f, bg=bgc)
#         self.book4_lbl.grid(row=1, column=3, padx=10)

#         #take books from database
        


#         #calendar for appointment
        
#         #calendar title
#         self.calendar_lbl = Label(self, text ='Calendar', font = ('Arial', 28), bg=bgc)
#         self.calendar_lbl.pack()
#         self.calendar_lbl.place(x=1015, y=100)

#         #calendar frame
#         self.calendar_frame = Frame(self, bg=bgc,relief=SOLID)
#         self.calendar_frame.place(x=965, y=155)

#         today = datetime.date.today()
#         #calendar widget
#         self.cal = Calendar(self.calendar_frame, selectmode="day", year=today.year, month=today.month, day=today.day, date_pattern='dd/mm/yyyy', font=('Arial', 10))
#         self.cal.pack(pady=20, padx=20)


#         #post a question label
#         self.post_lbl = Label(self, text ='Post a Question', font = ('Arial', 28), bg=bgc)
#         self.post_lbl.pack()
#         self.post_lbl.place(x=985, y=425)

#         #post a question frame
#         self.post_frame = Frame(self, bg=bgc,relief=SOLID)
#         self.post_frame.place(x=934, y=465)

#         #question textbox
#         self.question_txt = Text(self.post_frame, width=35, height=10, wrap='word',font=f)
#         self.question_txt.insert(INSERT, 'Type your question here...')
#         self.question_txt.grid(row=0, column=0,columnspan=3, padx=10, pady=10)

#         #post question btn
#         self.post_btn = Button(self.post_frame, width=15, text='Post', font=f, relief=SOLID,cursor='hand2')
#         self.post_btn.grid(row=1, column=1, padx=10, pady=10)