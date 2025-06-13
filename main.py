import tkinter as tk
from api import country_covid_data 
from tkinter import ttk
from visualization import visualization
from PIL import Image,ImageTk

root = tk.Tk()
root.title("Covid 19 tracker")
root.geometry("600x442")

image = Image.open("covid_19.jpg")
image = image.resize((600,442),Image.Resampling.LANCZOS)
covid_image = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=covid_image)
image_label.place(x=0, y=0, relwidth=1, relheight=1)
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
country.pack(pady = 20)
country.current() #.current(index) Sets the default selected item (by index) in the dropdown.

def current_country():
    country_covid_data(select_country.get())

def vil():
    visualization(select_country.get())


fetch_butt = tk.Button(root,text = "Fetch Data",command = current_country)
fetch_butt.pack(pady = 20)

visualization_butt = tk.Button(root,text="Visualization",command = vil)
visualization_butt.pack(pady=20)

exit_butt = tk.Button(root, text = "Exit", command = root.destroy)
exit_butt.pack(pady = 20)


root.mainloop()