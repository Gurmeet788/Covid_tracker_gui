import tkinter as tk
from api import country_covid_data 
from tkinter import ttk



root = tk.Tk()
root.title("Covid 19 tracker")
root.geometry("15000x15000")
root.configure(background="lightblue")

label = tk.Label(root,text = "Welcome to Covid 19 Tracker",font=("Arial Black",14),background="red")
label.pack(pady = 20)

ttk.Label(root,text="Country Names",font=("Arial Black",14),background="black",foreground ="white").pack(pady=20)
select_country = tk.StringVar()
select_country.set("Select an option") 
country = ttk.Combobox(root,width=27,textvariable=select_country)
country['values'] = (
    "Pakistan",
    "USA",
    "Brazil",
    "Russia",
    "France",
    "UK",
    "Germany",
    "Italy",
    "Canada",
    "India",
    "Bangladesh",
    "Australia",
    "China",
    "Japan",
    "South Korea",
    "Mexico",
    "South Africa",
    "Indonesia",
    "Argentina",
    "Spain"
)
country.pack(pady = 10)
country.current()

def current_country():
    country_covid_data(select_country.get())

fetch_butt = tk.Button(root,text = "Fetch Data",command = current_country)
fetch_butt.pack(pady = 20)


exit_butt = tk.Button(root, text = "Exit", command = root.destroy)
exit_butt.pack(pady = 20)


root.mainloop()