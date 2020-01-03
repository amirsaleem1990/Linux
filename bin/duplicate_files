import os
os.system('find . -type f -name "*" > files-with-complete-path.txt')
with open("files-with-complete-path.txt", "r") as file:
    a = file.read().splitlines()


with open("files-with-complete-path.txt", "w") as file:
	file.write("\n".join([i for i in a if not "thumbnails" in i]))

with open("files-with-complete-path.txt", "r") as file:
    a = file.read().splitlines()
a = [i.strip().replace("_", "").replace("-", "").replace(" ", "") for i in a]
files = []
for i in a:
	if i.startswith("./"):       
	    i = i[2:]                   
	files.append(i[i.rfind("/")+1:])
print(len(a) == len(files))

import pandas as pd
print(pd.Series(files).nunique())

df = pd.DataFrame([files, a]).T
df.columns = ["File", "Path"]
# freq = df.File.value_counts()
# freq[freq > 1]
duplicated = df[df.File.duplicated()].sort_values("File")
duplicated.to_csv("files_names.csv")


print("2 file Ganerated:\nfiles-with-complete-path.txt\nfiles_names.csv\n\n")