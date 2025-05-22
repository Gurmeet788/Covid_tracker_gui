import tkinter as tk
from api import covid_data 

root = tk.Tk()
root.title("Covid 19 tracker")
root.geometry("15000x15000")


label = tk.Label(root,text = "Welcome to Covid 19 Tracker",font=("Arial",14))
label.pack(pady = 20)

fetch_butt = tk.Button(root,text = "Fetch Data",command= covid_data)
fetch_butt.pack(pady = 20)

exit_butt = tk.Button(root, text = "Exit", command = root.destroy)
exit_butt.pack(pady = 20)

root.mainloop()