#!/home/amir/.venv_base/bin/python3

# compare_function_1.py

import hashlib
import pandas as pd
import os
from IPython.display import display

import sys
file_name = sys.argv[1]
assert bool(file_name), "No/empty argument"
assert os.path.exists(file_name), "File not found"

from amir_analysis_functions import cksum_python

# file_name = os.environ["f"]

f = open(file_name, "r").read().splitlines()
df = pd.DataFrame({"full" : f})
df["file"] = df.full.str.split("/").str[-1]
df['chksum'] = df.full.apply(cksum_python)
df['size_byte'] = df.full.apply(os.path.getsize)
df.to_csv(file_name + ".csv", index=False)
print(f"\nSaved data as {file_name}.csv")