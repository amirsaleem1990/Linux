#!/home/amir/.venv_base/bin/python3

import os
from sqlalchemy import create_engine
import pandas as pd

url = input("Enter db url, eg: postgresql://USER:PASS@IP:PORT/DB_NAME ")
tb_name = input("Enter your table name ")
engine = create_engine(url)
df = pd.read_sql(f'SELECT * FROM "{tb_name}";', engine.connect())
output_file_name = f"/tmp/{tb_name}.pkl"
while os.path.exists(output_file_name):
	output_file_name = f"The file {output_file_name} is already exists, please provide another path/name. " 
df.to_pickle(output_file_name)
