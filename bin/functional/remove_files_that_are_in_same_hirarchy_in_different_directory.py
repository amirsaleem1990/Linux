#!/home/amir/.venv_base/bin/python3
import os
import sys
import pandas as pd

def function(files):
	lst = []
	for file_path in files:
		lst.append([file_path, os.path.getsize(file_path)])
	return lst

def function2(user_inp):
	if user_inp == '1':
		return first_base_path, df.f_file_full.to_list(), f_before_count
	elif user_inp == '2':
		return second_base_path, df.s_file_full.to_list(), s_before_count

if len(sys.argv) > 1:
	first_path = sys.argv[1]
else:
	first_path = input("Enter first  full  path, (eg: /media/amir/1TB_backup/sdb4_Apps_Books_learning/learning/) ")
if len(sys.argv) > 2:
	second_path = sys.argv[2]
else:
	second_path = input("Enter second full path, (eg: /media/amir/Data_1/learning/) ")

# first_base_path =  input("First base path  (eg: /media/amir/1TB_backup/sdb4_Apps_Books_learning/learning/)")
# second_base_path = input("Second base path (eg: /media/amir/Data_1/learning/) ")

first_base_path = first_path
second_base_path = second_path
# first_base_path = "/media/amir/1TB_backup/sdb4_Apps_Books_learning/learning/"
# second_base_path = "/media/amir/Data_1/learning/"

os.system(f"find '{first_path}' -type f > /tmp/f_path.txt")
print(f"The first path have {open('/tmp/f_path.txt', 'r').read().count('\n')} files")
os.system(f"find '{second_path}' -type f > /tmp/s_path.txt")
print(f"The second path have {open('/tmp/s_path.txt', 'r').read().count('\n')} files")

f_file = open("/tmp/f_path.txt", 'r').read().splitlines()
s_file = open("/tmp/s_path.txt", 'r').read().splitlines()

df_f = pd.DataFrame(function(f_file), columns=['f_file_full', 'f_size'])
df_s = pd.DataFrame(function(s_file), columns=['s_file_full', 's_size'])

df_f['f_name_without_base_path'] = df_f.f_file_full.str.replace(first_base_path, "")
df_s['s_name_without_base_path'] = df_s.s_file_full.str.replace(second_base_path, "")

f_before_count = df_f.shape[0]
s_before_count = df_s.shape[0]

df = df_f.merge(df_s, left_on='f_name_without_base_path', right_on='s_name_without_base_path', how='inner')
df = df[df.f_size.eq(df.s_size)]

prompt = f"There are {df.shape[0]} files that are with same name, size, and directory hirachy in <{first_base_path}>, and <{second_base_path}>, which path's files you want to delete?\n1-{first_base_path}\n2-{second_base_path}\n"

input()
user_inp = input(prompt)
while not user_inp in ('1', '2'):
	user_inp = input(prompt)

base_path, file_full_names, before_count = function2(user_inp)

if input(f"Are you sure that you want to remove all matching files from {base_path}? [yes|no] ") == 'yes':
	if input(f"Are you sure? (This operation will remove {df.shape[0]} files (out of existing {before_count} ({round(df.shape[0]/before_count*100, 2)}%)), ({df.f_size.sum()} bytes | {round(df.f_size.sum()/1024)} KB, or {round(df.f_size.sum()/1024/1024)} MB | {round(df.f_size.sum()/1024/1024/1024)} GB) [yes|no]? ") == 'yes':
		print()
		print(*file_full_names, sep="\n")
		print()
		input("\nALL the above files would be removed, please press enter to proceed: ")
		for file_path in file_full_names:
			try:
				os.remove(file_path)
				print(f"{file_path} has been removed ... ")
			except:
				print(f"!!! File {file_path} couldn't be removed !!! ")
