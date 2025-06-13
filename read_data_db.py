import pandas as pd

def read_data(quary,con):
    try:
        data = pd.read_sql_query(quary,con)
        return data
    except Exception as e:
        print("conot read the data",e)