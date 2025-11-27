#!/home/amir/.venv_base/bin/python3

import sys
import os
import pandas as pd
file_name = sys.argv[1]
df = pd.read_csv(file_name)
df.columns = df.columns.str.strip()
x = df.select_dtypes("O").nunique().sort_values().rename("Nunique").reset_index().assign(Nunique_Ratio = lambda x: x.Nunique/len(df)*100).set_index("index")
print()
print(x.to_markdown())
print()
threshold = input("Select the upper threshold (inclusive), eg: 10 will remove all variables that have 10 or more unique values: ")
if threshold:
	threshold = float(threshold)
	cols_to_keep = input("Do you want any column(s) to keep?, if yes then list them separated by a comma: ")
	if cols_to_keep:
		cols_to_keep = [i.strip() for i in cols_to_keep.strip().split(",")]
	else: 
		cols_to_keep = []
	cols_to_remove = x.drop(cols_to_keep).loc[lambda x: x.Nunique >= threshold].index.to_list()
	if cols_to_remove:
		print("\nCols to remove: ")
		print(*cols_to_remove, sep='\n') 
		if input("Do you agree? [yes|no] ") == 'yes':
			print(df.shape[1])
			df = df.drop(columns=cols_to_remove)
			print(df.shape[1])
			print()



print("\n\nNaNs ratio in each column: ")
x = df.isna().mean().mul(100).sort_values()
if x.sum():
	print()
	print(x.to_markdown())
	print()
	threshold_ = input("Select the upper threshold (inclusive), eg: 50 will remove all variables that have 50% or more missing values: ")
	cols_to_remove_ = []
	if threshold_:
		threshold_ = float(threshold_)
		cols_to_keep_ = input("Do you want any column(s) to keep?, if yes then list them separated by a comma: ")
		if cols_to_keep_:
			cols_to_keep_ = [i.strip() for i in cols_to_keep_.strip().split(",")]
		else: 
			cols_to_keep_ = []
		cols_to_remove_ = x.drop(cols_to_keep_).loc[lambda x: x >= threshold_].index.to_list()
	if cols_to_remove_:
		print("\nCols to remove: ")
		print(*cols_to_remove_, sep='\n') 
		if input("Do you agree? [yes|no] ") == 'yes':
			print(df.shape[1])
			df = df.drop(columns=cols_to_remove_)
			print(df.shape[1])
			print()

print(df.shape)
df = df.drop(columns=df.nunique().loc[lambda x: x==1].index.to_list()).drop_duplicates()
print(df.shape)
print()

print(df.shape[0])
df = df.dropna()
print(df.shape[0])
print()






df.to_csv("/tmp/aljalkjads.csv", index=False)

print("\n"*20)
os.system("du -sh /tmp/aljalkjads.csv")
print("\n"*20)
