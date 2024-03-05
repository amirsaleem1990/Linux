#!/usr/bin/python3

import nbformat
import pandas as pd
import os
import json
import warnings                  

warnings.filterwarnings("ignore")


# notebook_path = 'dataset-353-LLM/dataset-353.ipynb'
notebook_path = [file_name for file_name in os.listdir() if file_name.endswith(".ipynb")]
if len(notebook_path) > 1:
    print(*notebook_path, end="\n")
    print()
    notebook_path = input("There are multiple notebook, please Enter the name:")
elif not notebook_path:
    print("No notebook found in the directory\nExiting.....")
    import sys
    sys.exit(1)

notebook_path = notebook_path[0]
with open(notebook_path, 'r', encoding='utf-8') as nb_file:
    notebook_json = nbformat.read(nb_file, as_version=4)

R = [
	'"rating": rating,',
	'"codeA": codeA,',
	'"codeB": codeB,',
	'"reasoningA": reasoningA,',
	'"reasoningB": reasoningB,',
	'"dev_code": correct_code,'
]

lst = [] 
for index, cell in enumerate(notebook_json['cells']):
    cell_type = cell['cell_type']

    if cell_type != 'code':
        continue

    source_code = cell['source']
    if not 'dev_feedback' in source_code:
        continue
     
    source_code_cleaned = "=".join(source_code.strip().split("=")[1:]).strip()
    source_code_cleaned = "\n".join([line for line in source_code_cleaned.splitlines() if not line.strip() in R])

    number = source_code.strip().split()[0]
    if '"""' in source_code_cleaned:
        source_code_cleaned = source_code_cleaned.replace('"""\n', '"').replace('\n"""', '"')
    if '"question": NULL,' in source_code_cleaned:
        source_code_cleaned = source_code_cleaned.replace('"question": NULL,', '"question": null,')

    dev_feedback = json.loads(source_code_cleaned)['dev_feedback']
    lst.append([number, bool(dev_feedback)])


x = pd.DataFrame(lst, columns=['number', 'is_devfeedback_exist']).groupby("is_devfeedback_exist").apply(lambda g: g.number).unstack().T
xx = x[True].dropna()
total_interactions = xx.str.strip('q').str[:-1].astype(int).max()
total_iterations = xx.shape[0]
print(f"\n\n{total_interactions} interactions are done")
print(f"{total_iterations} iterations are done")
print(f"Iteraions per interaction ratio: {round(total_iterations / total_interactions, 2)}")
print()