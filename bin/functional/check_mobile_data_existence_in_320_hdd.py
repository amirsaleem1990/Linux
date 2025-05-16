#!/home/amir/.venv_base/bin/python3

import os
import shutil
import pandas as pd

def make_data_frame(file_path):
	x = open(file_path, 'r').read().splitlines()
	df =  pd.DataFrame([(i[:i.index("  ")], i[i.index("  ")+2:]) for i in x], columns=['hash', 'full_file_path'])
	df['file'] = df.full_file_path.str.split("/").str[-1]
	df.full_file_path = file_path.split("/hashes_sha256sum_")[0] + "/" + df.full_file_path.str.lstrip("./")
	return df


input("""
Open your termianl
Go to /media/70GB/Mobile/
We assume that your mobile data is there
Now execute the following:
	IFS=$'\\n'; find . -type f -print0 | parallel -0 sha256sum > hashes_sha256sum_media_70GB_Mobile.csv
Wait for completion of the above Linux command 
Press any key to proceed ...
""")

new = make_data_frame("/media/70GB/Mobile/hashes_sha256sum_media_70GB_Mobile.csv")
_320 = make_data_frame("/media/amir/Data_2/320GB/hashes_sha256sum_Data_2_320GB.csv")

base_exists_folder_name="_already_exist_"
exists_folder_name="_already_exist"
e=1
while os.path.exists(exists_folder_name):
    e += 1
    exists_folder_name = f"{base_exists_folder_name}_{e}"
os.mkdir(exists_folder_name)

merged = new.merge(_320, on=['hash', 'file'], how='inner', suffixes=("_new", "_320")).reset_index(drop=True)
for index, row in merged.iterrows():
	try:
	    shutil.move(row.full_file_path_new, exists_folder_name)
	except:
		print(f"Failed to move <{row.full_file_path_new}> to <{exists_folder_name}>")
print(f"\n{len(merged)} existing files moved to {exists_folder_name}, they exist already, feel free to remove them...\n")

