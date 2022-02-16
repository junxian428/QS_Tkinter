import tkinter as tk
from subprocess import call

root = tk.Tk()

def column():
   print("Hello Column")
   call(["python", "Column.py"])

def beam():
    print("Hello Beam")
    call(["python", "Beam.py"])


A = tk.Button(root, text ="Beam", command = column).pack()
B = tk.Button(root, text ="Column", command = beam).pack()
C = tk.Button(root, text ="Back", command = quit).pack()

root.mainloop()