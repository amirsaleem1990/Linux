#!/home/amir/.venv_base/bin/python3

import shutil
from amir_analysis_functions import convert_units
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv("/tmp/here_there.txt", delimiter=",", header=None)
df.columns=["file", "here_kb", "there_kb"]
df[["here_kb", "there_kb"]] = df[["here_kb", "there_kb"]].fillna(0).astype(int)
df = df[~df.file.isin([".", "..", ".:"])]
mask = df.here_kb.gt(0) & df.there_kb.gt(0)
df["where_"] = df.apply(lambda row: "in_both" if row.here_kb>0 and row.there_kb > 0 else "here_only" if row.here_kb>0 else "there_only", axis=1)
x = df.groupby("where_").apply(lambda g: (g["here_kb"].sum(), g["there_kb"].sum(), g.shape[0]))
x = pd.DataFrame(x.to_list(), index=x.index, columns=["here_kb", "there_kb", "lenght"])
x[["here_kb", "there_kb"]] = x[["here_kb", "there_kb"]].applymap(lambda val: convert_units(from_unit="kb", value=val))
x = x.rename_axis(None)
print(x.to_string())
kb="kb"
in_both = df[df.where_.eq("in_both") & df.here_kb.eq(df.there_kb)]
print(f"\nThere are {len(in_both)} files/folders ({convert_units(from_unit=kb, value=in_both.here_kb.sum())}) that have the same size.\n")

if not in_both.empty:
    import os
    there_dir = open("/tmp/there_dir", "r").read().strip()
    here_dir = open("/tmp/here_dir", "r").read().strip()

    if not there_dir.endswith("/"):
        there_dir += "/"
    if not here_dir.endswith("/"):
        here_dir += "/"

    print(in_both.set_index("file").here_kb.sort_values().apply(lambda v: convert_units(from_unit="kb", value=v, rounded_to=2)).to_string())
    print(f"\n\nNow you can remove all common files/folders with same size from one of the following directories:\n\t1-{here_dir}\n\t2-{there_dir}\n")
    user_selected_num = int(input())-1
    lst = [here_dir, there_dir]
    if input(f"Do you want to remove files/folders that have same size in both directories FROM ({lst[user_selected_num]})? [yes|no] ") == "yes":
        if input("Are you sure? [yes|no] ") == "yes":
            for i in in_both.file:
                if os.path.exists(lst[user_selected_num]+i):
                    if os.path.isdir(i):
                        shutil.rmtree(i)
                    else:
                        os.remove(lst[user_selected_num]+i)
                    print(f"The file {lst[user_selected_num]+i} removed.")