import tkinter as tk
from tkinter import *
from PIL import ImageGrab
from PIL import Image
import os
import subprocess
from xlsx import CSVArray
from tkinter import simpledialog
from openpyxl import Workbook, drawing
import openpyxl

canvas_width = 300
canvas_height = 300

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    c.create_oval(x1, y1, x2, y2, fill="red",outline="red")

def save_canvas():
    print("save")
    application_window = tk.Tk()
    answer = simpledialog.askstring("Input", "Enter image name",parent=application_window)
    if answer is not None:
        c.postscript(file=answer + ".ps", colormode="color")
        img = Image.open(answer + ".ps")
        img.save(answer+ ".jpg", "JPEG")
    else:
        print("You did not enter a name")

def submit_form():
    print("Hello")

def blackpaint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    c.create_oval(x1, y1, x2, y2, fill="black",outline="black")
def switchcolor():
    c.unbind("<B1-Motion>")
    c.bind("<B1-Motion>", blackpaint)

def whitepaint():
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    c.create_oval(x1, y1, x2, y2, fill="white",outline="white")


def switchcolor():
    c.unbind("<B1-Motion>")
    c.bind("<B1-Motion>", blackpaint)
    
def eraser():
    c.unbind("<B1-Motion>")
    c.bind("<B1-Motion>", whitepaint)

### Section

fields = 'Job', 'Type Of Work','Bill No','Element No','Slip No','Heading','Description','Unit','Quantity','Length','Width','Height','Taker Off'

def fetch(entries):
    num = 0
    username = ""
    password = ""
    application_window = tk.Tk()
 
    answer = simpledialog.askstring("Input", "Create New File. Enter File Name (.xlsx)",parent=application_window)
    if answer is not None:
        header = [u'Job', u'Type Of Work', u'Bill No', u'Element No', u'Slip No', u'Heading', u'Description', u'Unit', u'Quantity', u'Length', u'Width', u'Height', u'Taker Off']
        wb = Workbook()
        ws1 = wb.active
        ws1.title = "range names"
        ws1.append(header)
        dest_filename = answer

        #for entry in entries:
            #field = entry[0]
            #text  = entry[1].get()
            #print('%s: "%s"' % (field, text)) 
            #print(text)
        ars = []
        for row in entries:
            text = row[1].get()
            #print(text)
        
            ars.append(text)
        for x in ars:
            print(x)
        ws1.append(ars)
        wb.save(dest_filename)
        

    else:
        print("You did not enter a name")

     

    #print("Username is " + username)
    #print("Password is " + password)
    #try:
        #conn = sqlite3.connect('LoginUser.db')
        #print("sqlite open successfully")
        #try:
            #cur = conn.cursor()
            #cur.execute("INSERT INTO User (Username, Password) VALUES ('" + username + "', '" + password + "');")
            #messagebox.showinfo("Register", "Register Successful")
            #conn.commit()
        #except Exception as e:
            #print(e)
    #except:
        #print("An exception occurred")             

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
    b3 = tk.Button(root, text='Save Canvas', command=save_canvas)
    b3.pack(side=tk.TOP, padx=5, pady=5)
    b4 = tk.Button(root, text='Black', command=switchcolor)
    b4.pack(side=tk.TOP, padx=5, pady=5)
    b5 = tk.Button(root, text='Eraser', command=eraser)
    b5.pack(side=tk.TOP, padx=5, pady=5)
    ####
    #Canvas
    c = Canvas(master=root, width=canvas_width, height=canvas_height,bg="white")
    c.pack(expand=YES, fill=BOTH)
    c.bind("<B1-Motion>", paint)

    ###
    root.mainloop()
    root = tk.Tk()
   


