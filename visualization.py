from read_data_db import read_data
import sqlalchemy
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import messagebox

def visualization(country):
    try:
        engine = sqlalchemy.create_engine("mysql+pymysql://root:root@localhost/covid_tracker")
        quary = f"Select * from daily_stats where country = '{country}'"
        data = read_data(quary= quary,con=engine)
        if country == "Select an option":
            messagebox.showwarning("warning",str("Please Select country first"))

        elif isinstance(data,pd.DataFrame) and not data.empty:
            print(data)
            plt.figure(figsize=(10,6))
            plt.plot(data["report_date"],data["total_cases"], marker='o', linestyle='-', color='blue')
            plt.title(f"COVID-19 Cases Over Time ({country})")
            plt.xlabel("Dates")
            plt.ylabel("Total Cases")
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        else:
            messagebox.showerror("Error", str(f"{country} not found in data base"))
    except Exception as e:
        messagebox.showerror("Exception occurred:", str(e))