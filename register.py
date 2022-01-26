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



#def sql_register():
    #try:
        #conn = sqlite3.connect('LoginUser.db')
        #print("sqlite open successfully")
        #print(registerUser.get())
        #print(registerPassword.get())
    #except:
        #print("An exception occurred")
    #cur = conn.cursor()
    #print(txt1)
    #print(txt2)
    #inp = txt1
    #inp2 = txt2
    #try:
        #cur.execute("INSERT OR IGNORE INTO User (Username, Password) VALUES ('" + inp + "', '" + inp2 + "');")
    #except:
        #print("An exception occurred")
    #print("Hello")


fields = 'Username', 'Password'

def fetch(entries):
    num = 0
    username = ""
    password = ""
    for entry in entries:
        #field = entry[0]
        text  = entry[1].get()
        #print('%s: "%s"' % (field, text)) 
        #print(text)
        if(num % 2 == 0):
            username = text
        else:
            password = text

        num = num + 1

    print("Username is " + username)
    print("Password is " + password)
    try:
        conn = sqlite3.connect('LoginUser.db')
        print("sqlite open successfully")
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO User (Username, Password) VALUES ('" + username + "', '" + password + "');")
            messagebox.showinfo("Register", "Register Successful")
            conn.commit()
        except Exception as e:
            print(e)
    except:
        print("An exception occurred")             

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = tk.Button(root, text='Register',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()