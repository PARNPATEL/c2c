import tkinter as tk
import math

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x500")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10, sticky="nsew")

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('sqrt(',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('**',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('(',3,4),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3), (')',4,4),
    ('sin(',5,0), ('cos(',5,1), ('tan(',5,2), ('pi',5,3), ('C',5,4),
    ('log10(',6,0), ('log(',6,1)
]

env = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "pi": math.pi,
    "log10": math.log10,
    "log": math.log
}

for (text, row, col) in buttons:
    if text == "=":
        cmd = lambda: calculate_with_env()
    elif text == "C":
        cmd = clear
    else:
        cmd = lambda t=text: click(t)

    tk.Button(root, text=text, width=8, height=2,
              command=cmd).grid(row=row, column=col, padx=2, pady=2)

def calculate_with_env():
    try:
        result = eval(entry.get(), {"__builtins__": None}, env)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root.mainloop()
