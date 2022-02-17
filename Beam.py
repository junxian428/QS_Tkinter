import tkinter as tk
from subprocess import call

root = tk.Tk()

def concrete():
   print("Hello Column")
   call(["python", "beam-widget.py"])


def formwork():
    print("Hello Beam")
    call(["python", "Beam_Formwork.py"])

  
def reinforcement():
    print("Hello Reinforcement")
    call(["python", "Beam_Reinforcement.py"])


A = tk.Button(root, text ="Concrete", command = concrete).pack()
B = tk.Button(root, text ="Formwork", command = formwork).pack()
C = tk.Button(root, text ="Reinforcement", command = reinforcement).pack()
D = tk.Button(root, text ="Back", command = quit).pack()

root.mainloop()