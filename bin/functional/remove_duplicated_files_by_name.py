#!/home/amir/.venv_base/bin/python3
input("Make </tmp/all_files.txt> by using find . -type f > /tmp/all_files.txt, then press any key ")
import pandas as pd
import os
from IPython.display import display

MUST_BE_EXCLUDED_SUB_STRINGS = input("substring/s to EXCLUDE, (if multiple saperate them by pipe, eg('abc|def|ghi')): ")
MUST_BE_INCLUDED_SUB_STRINGS = input("substring/s to INCLUDE, (if multiple saperate them by pipe, eg('abc|def|ghi')): ")
user_option = input("Select you option\n1- All files\n2- Same size only\n3- Different size only\n")
assert user_option in ["1", "2", "3"], "\nWrong option\nAborting.......\n"

f = open("/tmp/all_files.txt", 'r').read().splitlines()
f2 = [i.split("/")[-1] for i in f]
f3 = ["/".join(i.split("/")[:-1])+"/" for i in f]
df = pd.DataFrame({"full" : f, "file_name" : f2, "path" : f3})



df = df[df.full.apply(os.path.exists)]
df = df[df.file_name.duplicated(keep=False)] # Keep only duplicated files by name

if MUST_BE_INCLUDED_SUB_STRINGS:
    df = df[
        df.file_name.isin(
            df
            .groupby("file_name")
            .apply(
                lambda x:x.full.str.contains(MUST_BE_INCLUDED_SUB_STRINGS).any()
            )
            .where(lambda x:x==True)
            .dropna()
            .index
            .to_list()
            )
        ]
    print(df.shape)
if MUST_BE_EXCLUDED_SUB_STRINGS:
    df = df[
        df.file_name.isin(
            df
            .groupby("file_name")
            .apply(
                lambda x:x.full.str.contains(MUST_BE_EXCLUDED_SUB_STRINGS).any()
            )
            .where(lambda x:x==False)
            .dropna()
            .index
            .to_list()
            )
        ]
    print(df.shape)



print(df.shape)
df['size_bytes'] = df.full.apply(os.path.getsize)
print()
print(df.head().to_markdown(index=False))
print()

to_remove = []
def func(user_inp, d):
    global removed_size, removed_qty
    assert user_inp.isnumeric(), "\nWrong input\nAborting........\n"
    user_inp = int(user_inp)
    if not user_inp in d.index.to_list():
        raise Exception(f"This ({user_inp}) index not found")
    to_remove.append("".join(d.loc[user_inp, ["path", "file_name"]].to_list()))
    removed_size += d.loc[user_inp, "size_bytes"]
    removed_qty += 1


removed_size = 0
removed_qty = 0
total_qty = df.file_name.nunique()


for fn in df.file_name.unique():
    try:
        print(f"\n\n{round(removed_size/1024/1024)} MB, Size of files selected to remove")
        print(f"{removed_qty}, Qty of files selected to removed")
        print(f"{total_qty} Total duplicated files qty.")
        d = df[df.file_name.eq(fn)].sort_values("size_bytes").drop("full", axis=1).reset_index(drop=True)
        # 2- Same size only
        # 3- Different size only
        if user_option == "2":
            if d.size.nunique() > 1:
                continue
        elif user_option == "3":
            if d.size.nunique() == 1:
                continue
        display(d)
        user_input = input(
            "Choose file/s to delete using index, if multiple saperate them by comman (eg: 0,2)\n"
            "Press any key if you don't want to remove any file\n"
        ).strip()
        if user_input == "":
            continue
        if "," in user_input:
            for u_i in user_input.split(","):
                u_i = u_i.strip()
                func(u_i, d)
        else:
            func(user_input, d)
    except:
        break

if to_remove:
    print("\n\n")
    for index, value in list(enumerate(to_remove)):
        print(f"{index}- {value}")
    print("\n")

    user_inp = input("Above listed files going to be removed, Do you need to exclude some of them from removing list? [yes|no]: ")
    assert user_inp in ["yes", "no"], "\nWrong option\nAborting.......\n"
    if user_inp == "yes":
        indexes = input("Please specify index numbers, saperate them by comma (eg: 4,9)\n")
        if "," in indexes:
            indexes = list(map(int, indexes.split(",")))
        else:
            indexes = int(indexes)

        to_remove = [value for index, value in list(enumerate(to_remove)) if not index in indexes]

    print("\n")
    print(*to_remove, sep="\n")
    user_inp = input("\nWe are going to remove above listed files, Are you need to proceed? [yes|no]\n")
    assert user_inp in ["yes", "no"], "\nWrong input\nAborting .........\n"
    if user_inp == "yes":
        for file in to_remove:
            os.remove(file)
else:
    print("\nNo file to be removed\nExiting....\n")