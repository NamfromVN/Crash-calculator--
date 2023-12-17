import tkinter as tk
from tkinter import messagebox

import time

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_operator(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + operator)

def button_clear():
    entry.delete(0, tk.END)

def crash_event():
    time.sleep(100)
    window.destroy()

def button_equal():
    entry.delete(0, tk.END)
    entry.insert(tk.END, "idk")
    window.after(1, crash_event)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create number buttons
for i in range(9):
    button = tk.Button(window, text=str(i+1), padx=20, pady=10, command=lambda i=i: button_click(i+1))
    button.grid(row=(i//3)+1, column=i%3)

# Create operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, padx=20, pady=10, command=lambda operator=operator: button_operator(operator))
    button.grid(row=i+1, column=3)

# Create other buttons
button_clear = tk.Button(window, text="C", padx=20, pady=10, command=button_clear)
button_clear.grid(row=4, column=0)

button_zero = tk.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))
button_zero.grid(row=4, column=1)

button_equal = tk.Button(window, text="=", padx=20, pady=10, command=button_equal)
button_equal.grid(row=4, column=2)

window.mainloop()