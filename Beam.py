import tkinter as tk
from subprocess import call

root = tk.Tk()

def concrete():
   print("Hello Column")
   

def formwork():
    print("Hello Beam")
  
def reinforcement():
    print("Hello Reinforcement")


A = tk.Button(root, text ="Concrete", command = concrete).pack()
B = tk.Button(root, text ="Formwork", command = formwork).pack()
C = tk.Button(root, text ="Reinforcement", command = reinforcement).pack()
D = tk.Button(root, text ="Back", command = quit).pack()

root.mainloop()