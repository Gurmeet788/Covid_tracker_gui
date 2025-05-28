from read_data_db import read_data
import sqlalchemy
engine = sqlalchemy.create_engine("mysql+pymysql://root:root@localhost/")
quary = "Select * from employees"
print(read_data(quary= quary,con=engine).to_string(index=False))