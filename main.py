import sqlite3
#import mysql.connector
import tkinter as tk
from tkinter import *
import datetime
import threading
import time
import logging
from tkinter import ttk
from subprocess import call
from tkinter import messagebox
from time import sleep, perf_counter
from PIL import ImageTk, Image
from openpyxl import Workbook, drawing
import openpyxl
import os
from xlsx import Read
import pandas as pd
import numpy as np
from tkinter import simpledialog

global Login_Username
#Database Connection
try:
   print("sqlite open successfully")
   conn = sqlite3.connect('LoginUser.db')
except:
  print("An exception occurred")

#mydb = mysql.connector.connect(
  #host="localhost",
  #user="root",
  #password="",
  #database="posjavafx"
#)
global c
canvas_width = 300
canvas_height = 300


    #call(["python", "main.py"])
def firstOption():
    call(["python", "canvas.py"])

def secondOption():
    #print(os.getcwd())
    #path = os.getcwd + "/" + "measurement.xlsx"
    #path = "C:\\Users\\USer\\Downloads\\TkinterProject-main\\TkinterProject-main\\measurement.xlsx"
    #wb_obj = openpyxl.load_workbook(path)
    #sheet_obj = wb_obj.active
    #cell_obj = sheet_obj.cell(row = 1, column = 1)
    #print(cell_obj.value)
    
    application_window = tk.Tk()

    answer = simpledialog.askstring("Input", "Enter the File Name",parent=application_window)
    if answer is not None:
        #print("Your first name is ", answer)
        try:
            #p1 = Read.Read("CSV.csv") 
            p1 = Read.Read(answer)
            #p1.read()
            #print(p1.returnfilename())
            pd.options.display.max_rows = 9999
            #df = pd.read_csv(p1.returnfilename(),encoding='latin-1', on_bad_lines='skip')
            df = pd.read_csv(p1.returnfilename(), quotechar='"', delimiter=';')
            print(df)
            ReadTk = tk.Tk()
            ReadTk.title("Read CSV")
            ReadTk.geometry("500x500")
            tk.Label(ReadTk, text= "CSV File Name: " + answer).pack()
            tk.Label(ReadTk, text= "CSV File Data: ").pack()
            tk.Label(ReadTk, text= "_______________________________________").pack()
            tk.Label(ReadTk, text= df).pack()
            tk.Label(ReadTk, text= "_______________________________________").pack()
            ReadTk.mainloop()
        except Exception as ex:
            print("Error: " + str(ex))
            messagebox.showinfo("Error", "Error: " + str(ex))
    else:
        print("You did not enter a name")

    

def thirdOption():
    ExampleOfWork = Tk()
    image1 = Image.open('canvas.jpg')
    image1 = image1.resize((450, 350), Image. ANTIALIAS)
    img_1 = ImageTk.PhotoImage(image1)
    first_image= Label(root,image = img_1)
    first_image.pack()
    ExampleOfWork.mainloop()

def logout(): 
    repeated = False
    openNewWindow("",repeated)
    MainProgram.destroy()
    messagebox.showinfo("Log Out", "Log Out Successful") 
    frame.lift()



def openNewWindow(Login_Username,arugement):
    repeated = arugement
    if(repeated):
        # creates a Tk() object
        global MainProgram
        MainProgram = tk.Tk()   
        # sets the title of the
        # Toplevel widget
        MainProgram.title("New Window")
 
        # sets the geometry of toplevel
        MainProgram.geometry("200x200")
 
        # A Label widget to show in toplevel
    
        #Time
      

    
     
        #global updateTime
        #updateTime = Label( MainProgram, text =x).pack() 
        # use global variable
        global my_text
        global my_label
        my_text = datetime.datetime.now()
        # configure
        my_label = Label(MainProgram, text=my_text)
        my_label.config(text = my_text)
        #ThreadForUpdatingTime = threading.Thread(target=thread_function, args=(1,))
        #ThreadForUpdatingTime.start()

        tk.Label(MainProgram, text= "Current Username: " + Login_Username).pack()

        A = tk.Button(MainProgram, text ="Create CSV & Canvas", command = firstOption)
        A.pack()

       
        B = tk.Button(MainProgram, text ="Read CSV File", command = secondOption)
        B.pack()
    
       
        C = tk.Button(MainProgram, text ="Update CSV", command = thirdOption)
        C.pack()

         
        D = tk.Button(MainProgram, text ="Delete CSV", command = thirdOption)
        D.pack()

        E = tk.Button(MainProgram, text ="Exit", command = quit)
        E.pack()

        F = tk.Button(MainProgram, text ="Log Out", command = logout)
        F.pack()

        #start_time = perf_counter()
        #task()
        #end_time = perf_counter()

       
 
   

def sql_login():
    #mycursor.execute("SELECT * FROM `products`")
    #print(mycursor.fetchall())
    login = "false"
    conn = sqlite3.connect('LoginUser.db')
    cur = conn.cursor()
    inp = inputtxt.get(1.0, "end-1c")
    inp2 = inputtxt2.get()
    #Get Username & Password
    cur.execute("SELECT * FROM User where Username = '" + inp +"'AND Password = '" +inp2 +"';")
    SQL_username = conn.cursor()
    SQL_username.execute("SELECT Username FROM User where Username = '" + inp +"'AND Password = '" +inp2 +"';")
    username = SQL_username.fetchone()
 
    #Validation
    #rows = cur.fetchall()
    #print(rows)
    row = cur.fetchone()
    if row == None:
        print("There are no such users")
        messagebox.showinfo("Error", "Invalid Username or Password")
    else:
        txtUsername = str(username)
        txtUsername = txtUsername.replace("('", "")
        txtUsername = txtUsername.removesuffix("',)")
        Login_Username = txtUsername
        print(txtUsername)
        print("Global Variable User:" + Login_Username)
        msg = "Login Successful"
        messagebox.showinfo('message', msg)
        #frame.destroy() 
        openNewWindow(txtUsername,True)

    #if(rows == "[]"):
        #print(rows)
        #print("Password Error")
    #else:
        #msg = "Login Successful"
        #messagebox.showinfo('message', msg)
        #frame.destroy() 
        #openNewWindow()
      

    
    #for row in rows:
        #print(row)
        

    #inp = inputtxt.get(1.0, "end-1c")
    #print(inp)

    
    

def Register():
    call(["python", "register.py"])
    

    
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
tk.Label(frame, text="Username").pack()

# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt.pack()

tk.Label(frame, text="Password").pack()
inputtxt2 = tk.Entry(frame,
                   width = 20)
inputtxt2.config(show="*")
inputtxt2.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Login",
                   command=sql_login)
slogan.pack(side=tk.LEFT)
printButton = tk.Button(frame,
                        text = "Register", 
                        command = Register)
printButton.pack()
# Label Creation
#lbl = tk.Label(frame, text = "")
#lbl.pack()
root.mainloop()

