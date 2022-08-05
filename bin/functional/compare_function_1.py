# compare_function_1.py

import hashlib
import pandas as pd
import os
from IPython.display import display

import sys
file_name = sys.argv[1]
assert bool(file_name), "No/empty argument"
assert os.path.exists(file_name), "File not found"

def cksum(file_name):
	command = f"cksum {file_name} 2>/dev/null"
	x = list(os.popen(command))
	if not x:
		return None
	return x[0]

# file_name = os.environ["f"]

f = open(file_name, "r").read().splitlines()
df = pd.DataFrame({"full" : f})
df["file"] = df.full.str.split("/").str[-1]
mask = ~df.full.str.contains("'")
df.loc[mask, "full"] = "'" + df.full[mask] + "'"

df2 = pd.DataFrame(df.full.apply(cksum).dropna().str.split(" ", 2).to_list(), columns=["chksum", "size_byte", "file_name"]).drop("file_name", axis=1)
df = pd.concat([df, df2], axis=1)

df.to_csv(file_name + ".csv", index=False)

print(f"\nSaved data as {file_name}.csv")