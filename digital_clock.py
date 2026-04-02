import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%I:%M:%S %p')
    current_date = strftime('%A, %B %d, %Y')
    
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    time_label.after(1000, update_time)

root = tk.Tk()
root.title("Modern Digital Clock")
root.geometry("600x300")
root.configure(bg='#1a1a1a') 

main_frame = tk.Frame(root, bg='#2d2d2d', bd=0, highlightthickness=2, highlightbackground='#404040')
main_frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.9, relheight=0.7)

time_label = tk.Label(
    main_frame, 
    font=('Segoe UI', 65, 'bold'), 
    bg='#2d2d2d', 
    fg='#00ffcc'  
)
time_label.pack(pady=(20, 0))

date_label = tk.Label()
main_frame, 
font=('Segoe UI', 18), 
bg='#2d2d2d', 
fg='#aaaaaa'  
date_label.pack(pady=(0, 20))

footer_bar = tk.Frame(main_frame, bg='#00ffcc', height=4)
footer_bar.pack(fill='x', side='bottom')

update_time()

root.mainloop()
