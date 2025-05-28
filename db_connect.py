import mysql.connector as sql

def get_connection():
    try:
        connection = sql.connect(
            host="localhost",
            user="root",     
            password="root",
            database="covid_tracker"
        )
        return connection
    except sql.Error as err:
        print("❌ Connection error:", err)
        return None