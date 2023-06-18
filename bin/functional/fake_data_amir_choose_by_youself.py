#!/home/virtual_envs/fake_data/bin/python3

from faker import Faker
import numpy as np
import pandas as pd
import os
import sys
import numpy as np

dict_to_csv = {'INTEGER': {0: 'random_digit',1: 'random_digit_not_null',2: 'random_digit_not_null_or_empty',3: 'random_int',4: 'random_number',5: 'year',6: 'FLOAT',7: 'latitude',8: 'longitude',9: 'pricetag',10: 'DATETIME',11: 'future_date',12: 'future_datetime',13: 'time',14: 'time_object',15: 'date',16: 'date_between_dates',17: 'date_time',18: 'date_time_between_dates',19: 'past_datetime',20: 'STRING',21: 'random_element',22: 'random_letter',23: 'timezone',24: 'word',25: 'address',26: 'ascii_free_email',27: 'century',28: 'city',29: 'color_name',30: 'company',31: 'country',32: 'day_of_week',33: 'first_name_female',34: 'first_name_male',35: 'month_name',36: 'password',37: 'prefix_female',38: 'prefix_male',39: 'OTHER',40: 'random_elements',41: 'random_letters',42: 'rgb_color',43: 'words',44: 'color',45: 'coordinate',46: 'hex_color',47: 'latlng',48: 'phone_number'},'Example': {0: '4',1: '1',2: '1',3: '6394',4: '102971882',5: '1998',6: 'FLOAT',7: '-38.662185',8: '46.356264',9: '$88.29',10: 'DATETIME',11: '2023-01-08',12: '2022-12-28 02:03:21',13: '08:37:56',14: '14:03:51',15: '2000-01-15',16: '2022-12-25',17: '1999-04-12 02:57:51',18: '2022-12-25 21:56:17',19: '2022-12-10 02:24:54',20: 'STRING',21: 'b',22: "['m', 'T', 'V', 'u', 'X', 'P', 'b', 'g', 'H']",23: 'Pacific/Apia',24: 'tax',25: '8467 Michelle Courts Apt. 453 Port Jaime, ND 56477',26: 'donaldgould@yahoo.com',27: 'XVIII',28: 'Choiville',29: 'DarkViolet',30: 'Thomas, Dawson and Castillo',31: 'Swaziland',32: 'Thursday',33: 'Megan',34: 'Bradley',35: 'February',36: '_8LyH6Fg$0',37: 'Mrs.',38: 'Mr.',39: 'OTHER',40: "['c', 'c', 'c']",41: 'X',42: '237,23,228',43: "['employee', 'newspaper', 'effort']",44: '#d455d6',45: '-124.607372',46: '#e0e081',47: "(Decimal('-78.4078195'), Decimal('148.782676'))",48: '(373)265-7667x33386'},'Count': {0: ' ',1: ' ',2: ' ',3: ' ',4: ' ',5: ' ',6: 'FLOAT',7: ' ',8: ' ',9: ' ',10: 'DATETIME',11: ' ',12: ' ',13: ' ',14: ' ',15: ' ',16: ' ',17: ' ',18: ' ',19: ' ',20: 'STRING',21: ' ',22: ' ',23: ' ',24: ' ',25: ' ',26: ' ',27: ' ',28: ' ',29: ' ',30: ' ',31: ' ',32: ' ',33: ' ',34: ' ',35: ' ',36: ' ',37: ' ',38: ' ',39: 'OTHER',40: ' ',41: ' ',42: ' ',43: ' ',44: ' ',45: ' ',46: ' ',47: ' ',48: ' '}}

n_rows = int(input("nrows: "))

df = pd.DataFrame(dict_to_csv)
df.to_csv("/tmp/dict_to_csv.csv", index=False)
os.system("gopen /tmp/dict_to_csv.csv")


input("\n\nFill the file and then press any button here ....... ")
df2 = pd.read_csv("/tmp/dict_to_csv.csv")
if df.eq(df2).all().all():
	print("\nYou didn't fill any number. \nExiting ..........")
	sys.exit()
df2 = df2[df2.Count.ne(" ") & ~df2.Count.isin(["FLOAT", "DATETIME", "STRING", "OTHER"])][['INTEGER', 'Count']]
dict_ = df2.set_index("INTEGER").to_dict()['Count']
# dict_ = {'random_digit': '5', 'random_int': '3', 'random_number': '1', 'date': '3'}


Faker.seed(4321)
fake = Faker('en_US')
data = {}
for k, count in dict_.items():
	for i in range(int(count)):
		com = f"fake.{k}()"
		random_ganerated_vals = [eval(com) for _ in range(n_rows)]
		data[f"{k}-{i}"] = random_ganerated_vals
df = pd.DataFrame(data)

orig_name = "/home/amir/fake_data"
name = orig_name
n = 1
while os.path.exists(name + ".csv"):
	name = f"{orig_name}_{n}"
	n += 1
df.to_csv(name+".csv", index=False)
print(f"\n\nYou fake data saved as {name+'.csv'}\n")