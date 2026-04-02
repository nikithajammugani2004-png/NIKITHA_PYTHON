import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("DIGITAL CLOCK")

def time():
    string = strftime('%I:%M:%S %p \n %D')
    label.config(text = string)
    label.after(1000,time)

label = tk.Label(root, font=('calibri', 50, 'bold'),background='skyblue', foreground='black')
label.pack(anchor = 'center')

time()

root.mainloop()