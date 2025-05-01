import os
import pandas as pd
# os.system("find . /media/amir/13c2e3c7-b1c6-4b54-a575-730cf9ae508c/Camera/ -type f > /tmp/all_files_names")
files = open("/tmp/all_files_names", 'r').read().splitlines()
lst=[]
errors = []
for i in files:
	try:
		ind = len(i) - i[::-1].index("/")
		actual_file_name = i[ind:]
		path = i[:ind]
		bytes_ = int(list(os.popen(f"""du -sb "{i}" """))[0].split("\t")[0])
		lst.append([actual_file_name, path, bytes_])
	except:
		errors.append(i)
df = pd.DataFrame(lst, columns=['file', 'path', 'bytes'])
df = df[df.file.isin(df.file.value_counts().loc[lambda x: x>1].index.to_list())].sort_values("file").reset_index(drop=True)
for file_name, s_df in df.groupby("file"):
	if s_df.bytes.nunique() == 1:
		continue
	break