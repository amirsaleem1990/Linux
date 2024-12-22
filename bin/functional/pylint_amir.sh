#!/usr/bin/bash

pylint --msg-template='{msg_id}:{line:3d}:{column}:{msg}' "$1" | grep --color=auto "^[A-Za-z-]" | head -n -2 | sort -k1,4 -s > /tmp/xx
cat /tmp/xx | cut -d: -f1 | sort -u | sort > /tmp/unique_codes
cat /tmp/xx | cut -d: -f1 | sort | uniq -c > /tmp/distribution

cat /tmp/xx

/home/amir/.venv_base/bin/python3 <<< '
import pandas as pd
import json
def func(line):
    count, code = line.strip().split()
    return code, count
unique_codes = open("/tmp/unique_codes", "r").read().splitlines()
distribution = open("/tmp/distribution", "r").read().splitlines()
pylint_codes = json.load(open("/home/amir/github/Linux/pylint_codes.txt"))
selected_pylint_codes = {k: v for k,v in pylint_codes.items() if k in unique_codes}
distribution = dict(map(func, distribution))
selected_distribution = {k: int(v) for k,v in distribution.items() if k in unique_codes}
print(
    pd.DataFrame.from_dict(
        selected_distribution, 
        orient="index", 
        columns=["Count"]
    )
	.rename_axis("Code")
	.merge(
        pd.DataFrame.from_dict(
            selected_pylint_codes, 
            orient="index", 
            columns=["Error"]
        ).rename_axis("Code"), 
        left_index=True, 
        right_index=True
    )
    .reset_index()
    .sort_values(
        by="Code"
    )
    .to_string()
)
'