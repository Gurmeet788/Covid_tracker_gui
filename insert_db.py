from db_connect import get_connection
import datetime
def insert_data(country,total_cases,total_deaths,report_date):
    try:
        con = get_connection()
        cur = con.cursor() #.cursor() creates a cursor object (cur) → it allows you to:
        today = datetime.date.today()
        quary = "insert into daily_stats(country,total_cases,total_deaths,total_recovered,report_date) Values (%s,%s,%s,%s,%s)"
        Values = (country,total_cases,total_deaths,report_date,today)
        cur.execute(quary,Values)
        con.commit() #commit() → saves all changes made during the current transaction permanently to the database.
        print("Succuful insert")
    except Exception as e:
        print("Sql error can not insert")
    finally:
        if con and con.is_connected():
            con.close()