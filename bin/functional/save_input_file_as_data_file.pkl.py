#!/home/amir/.venv_base/bin/python3
import sys
import pandas as pd


def to_pickle(extention, file_name):
	try: 
		reading_methods[extention](file_name).to_pickle('/tmp/data_file.pkl')
	except: 
		try:
			reading_methods[extention](file_name, encoding='ISO-8859-1').to_pickle('/tmp/data_file.pkl')
		except:
			raise Exception("Failing to save $file_name to /tmp/data_file.pkl")

if len(sys.argv) == 1:
	raise Exception("\nFile name not not provided...\n")

file_name=sys.argv[1]

reading_methods = {
	"csv": pd.read_csv,
	"pkl": pd.read_pickle,
	"xlsx": pd.read_excel
}

success=False
if '.' in file_name:
	extention = file_name.split(".")[-1]
	if extention in reading_methods:
		to_pickle(extention, file_name)
		success = True


if not success:
	for extention in reading_methods:
		try:
			to_pickle(extention, file_name)
			break
		except:
			pass
