import tkinter as tk
from subprocess import call

root = tk.Tk()

def concrete():
   print("Hello Column")
   call(["python", "widget.py"])


def formwork():
    print("Hello Formwork")
    call(["python", "Column_Formwork.py"])

  
def reinforcement():
    print("Hello Reinforcement")
    call(["python", "Column_Reinforcement.py"])



A = tk.Button(root, text ="Concrete", command = concrete).pack()
B = tk.Button(root, text ="Formwork", command = formwork).pack()
C = tk.Button(root, text ="Reinforcement", command = reinforcement).pack()
D = tk.Button(root, text ="Back", command = quit).pack()

root.mainloop()