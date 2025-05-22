import requests as req
import pandas as pd
from tkinter import messagebox

def covid_data():
    url = "https://disease.sh/v3/covid-19/all"
    try:
        response = req.get(url)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame([data])
            result = df[["cases","deaths","recovered"]].to_string(index=False)
            messagebox.showinfo("🌍 Global COVID-19 Stats", result)
        else:
            messagebox.showerror("Falid to Fetch data error:",response)
    except Exception as e:
            messagebox.showerror("Exception occurred:", e)
            return None