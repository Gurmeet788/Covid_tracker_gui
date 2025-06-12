# 🦠 COVID-19 Tracker GUI with MySQL & Visualization

A desktop application to fetch, store, and visualize COVID-19 data using Python. It uses a GUI built with Tkinter, connects to a MySQL database, and visualizes stored data using Matplotlib.

---

## 📌 Features

- 🌍 Fetch global & country-wise COVID-19 data using [disease.sh API](https://disease.sh)
- 🗃️ Insert country-wise data into a MySQL database
- 📊 Visualize COVID-19 trends from stored data (not directly from API)
- 💻 Simple and intuitive Tkinter GUI
- 🖼️ Optional background image support for GUI
- ⚠️ Error handling with user-friendly messageboxes

---

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **GUI**: Tkinter
- **Database**: MySQL (via `mysql-connector-python` or `SQLAlchemy`)
- **Visualization**: Matplotlib
- **Data Handling**: Pandas
- **Image Support**: Pillow
- **API Source**: [disease.sh](https://disease.sh)

---

## 🧱 Database Schema

**Database**: `covid_tracker`  
**Table**: `daily_stats`

| Column          | Data Type |
|------------------|-----------|
| `id`             | INT (PK, AUTO_INCREMENT) |
| `country`        | VARCHAR   |
| `total_cases`    | INT       |
| `total_deaths`   | INT       |
| `total_recovered`| INT       |
| `report_date`    | DATE      |

---

## 🖥️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/covid-tracker-gui.git
   cd covid-tracker-gui
   ```
2. **Install dependencies**
```bash
pip install requests pandas matplotlib pillow mysql-connector-python sqlalchemy
```
3. **Set up MySQL**

- Ensure MySQL is installed and running.

- Create a database named covid_tracker.

- Create a table daily_stats using the schema above.
  
4. Run the application
```bash
python main.py
```
---
![image](https://github.com/user-attachments/assets/955a9164-1389-4802-a82c-75ee77803aaa)

**🧠 Usage Tips**
- Use the "Fetch Data" button to get COVID-19 stats and insert them into MySQL.

- Use the "Visualize" feature to display a graph from the stored data.

- GUI supports dropdowns for countries and shows results in a popup.



