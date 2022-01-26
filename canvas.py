import tkinter as tk
from tkinter import *
from PIL import ImageGrab
from PIL import Image
import os
import subprocess

canvas_width = 300
canvas_height = 300

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    c.create_oval(x1, y1, x2, y2, fill="red",outline="red")

def save_canvas():
    print("save")
    c.postscript(file="canvas.ps", colormode="color")
    img = Image.open("canvas.ps")
    img.save("canvas.jpg", "JPEG")

def submit_form():
    print("Hello")




### Section

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
    b1 = tk.Button(root, text='Write into Excel',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    ####
    #Canvas
    c = Canvas(master=root, width=canvas_width, height=canvas_height,bg="white")
    c.pack(expand=YES, fill=BOTH)
    c.bind("<B1-Motion>", paint)

    #Save Canvas
    Save = tk.Button(root, text ="Save Canvas", command = save_canvas)
    Save.pack()

    ###
    root.mainloop()
    root = tk.Tk()
   


