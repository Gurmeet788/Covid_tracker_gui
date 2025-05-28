import requests as req
import pandas as pd
from tkinter import messagebox
from insert_db import insert_data
def country_covid_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    try:
        response = req.get(url)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame([data])
            result = df[["cases","deaths","recovered"]].to_string(index=False)
            messagebox.showinfo( f"{country} COVID-19 Stats", result)
            print("Befor sql")
            total_cases = int(data["cases"])
            total_deaths = int(data["deaths"])
            total_recovered = int(data["recovered"])
            insert_data(country, total_cases, total_deaths, total_recovered)
        else:
            messagebox.showerror("Falid to Fetch data error:",response)
    except Exception as e:
            messagebox.showerror("Exception occurred:", e)
            return None