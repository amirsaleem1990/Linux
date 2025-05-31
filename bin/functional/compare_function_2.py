#!/home/amir/.venv_base/bin/python3

# compare_function_2.py

from pandas import read_csv
import os
from termcolor import colored

here = read_csv("/tmp/here_files.csv")
there = read_csv("/tmp/there_files.csv")
merged = here.merge(there, on=["chksum", "size_byte"], how="inner", suffixes=("_here", "_there"))[["chksum", "size_byte", "file_here", "file_there", "full_here", "full_there"]]
merged.to_csv("/tmp/merged.csv", index=False)
user_input = input(f"""{len(merged)} files are identical in both directories ({int(merged.size_byte.sum()/1024/1024)} MB), which one you need to REMOVE?\n\t1-{os.environ["here"]}\n\t2-{os.environ["there"]}\n\t""")
def func_3(files):
	removed_qty = 0
	filed_to_remove_qty = 0
	print(*files, sep="\n")
	print(colored("We are going to REMOVE above mentioned files, DO YOU WANT TO PROCEED? [yes|no]", "red"), end="\t")
	inp = input("")
	if inp == "yes":
		for file_to_remove in files:
			try:
				os.remove(file_to_remove)
				removed_qty += 1
			except:
				print(f"Filed to remove {file_to_remove}")
				filed_to_remove_qty += 1
		print(f"\nRemoved: {removed_qty}\nFiled to remove: {filed_to_remove_qty}\n")

merged.full_here = merged.full_here.str.strip("'")

if user_input == "1":
	files = merged.full_here.sort_values().to_list()
	func_3(files)
elif user_input == "2":
	files = merged.full_there.sort_values().to_list()
	func_3(files)
elif user_input == '':
	merged = merged[merged.chksum.isin(merged.chksum.value_counts().loc[lambda x: x==1].index.to_list())]
	unique_cksums = merged.chksum.unique()
	merged['Group'] = merged.chksum.map(dict(zip(unique_cksums, range(len(unique_cksums)))))
	merged = merged.sort_values(by="Group").reset_index(drop=True)
	merged = merged.filter(regex="^(?!full_).*", axis=1)
	merged['file_name_same_in_here_and_there'] = merged.file_here == merged.file_there
	print(merged)
else:
	raise Exception ("Wrong input\nAborting.........")
