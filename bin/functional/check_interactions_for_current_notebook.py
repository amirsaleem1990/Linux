#!/usr/bin/python3
import matplotlib.pyplot as plt
import nbformat  # Module for handling Jupyter notebooks
import pandas as pd  # Data manipulation library
import os  # Operating System module for file operations
import json  # JSON encoding and decoding module
import warnings  # Warning control module

warnings.filterwarnings("ignore")  # Ignore warnings during execution

# Get all notebook files in the current directory with the ".ipynb" extension
notebook_path = [file_name for file_name in os.listdir() if file_name.endswith(".ipynb")]

# Check if there are multiple notebooks in the directory
if len(notebook_path) > 1:
    print(*notebook_path, end="\n")
    print()
    # Allow the user to select a notebook if there are multiple
    notebook_path = input("There are multiple notebooks. Please enter the name: ")
elif not notebook_path:
    print("No notebooks found in the directory.\nExiting.....")
    import sys
    sys.exit(1)

# Get the first notebook path (assuming there's at least one)
notebook_path = notebook_path[0]

# Open the notebook file and read it as a Jupyter notebook format
with open(notebook_path, 'r', encoding='utf-8') as nb_file:
    notebook_json = nbformat.read(nb_file, as_version=4)

# List of strings to be removed from source code
R = [
    '"rating": rating,',
    '"codeA": codeA,',
    '"codeB": codeB,',
    '"reasoningA": reasoningA,',
    '"reasoningB": reasoningB,',
    '"dev_code": correct_code,'
]

lst = []  # List to store extracted information

# Iterate through the cells in the Jupyter notebook
for index, cell in enumerate(notebook_json['cells']):
    cell_type = cell['cell_type']

    # Skip non-code cells
    if cell_type != 'code':
        continue

    source_code = cell['source']

    # Check if the source code contains 'dev_feedback'
    if not 'dev_feedback' in source_code:
        continue
     
    # Extract relevant information from the source code
    source_code_cleaned = "=".join(source_code.strip().split("=")[1:]).strip()
    source_code_cleaned = "\n".join([line for line in source_code_cleaned.splitlines() if not line.strip() in R])

    number = source_code.strip().split()[0]

    # Handle special cases in the source code formatting
    if '"""' in source_code_cleaned:
        source_code_cleaned = source_code_cleaned.replace('"""\n', '"').replace('\n"""', '"')
    if '"question": NULL,' in source_code_cleaned:
        source_code_cleaned = source_code_cleaned.replace('"question": NULL,', '"question": null,')

    # Load dev_feedback from the cleaned source code
    dev_feedback = json.loads(source_code_cleaned)['dev_feedback']
    lst.append([number, bool(dev_feedback)])

# Create a DataFrame from the extracted information
df  = pd.DataFrame(lst, columns=['number', 'is_devfeedback_exist'])
# df.number.str.strip("q").str[:-1].astype(int).value_counts().sort_index().plot(kind='bar', title="Iterations Count for Interactions");
# plt.ylabel("Iterations count")
# plt.xticks(rotation=0)
# plt.grid(True)
# plt.show()


# df.number.str.strip("q").str[:-1].astype(int).value_counts().sort_index().cumsum().plot(kind='bar', title="Accumulated sum of interactions over iterations' count")
# plt.xticks(rotation=0)
# plt.grid(True)
# plt.ylabel("Accumulated sum of iterations count.")
# plt.show()

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

df.number.str.strip("q").str[:-1].astype(int).value_counts().sort_index().plot(kind='bar', ax=axs[0], title="Iterations Count for Interactions")
axs[0].set_ylabel("Iterations count")
axs[0].set_xlabel("Iterations")
axs[0].grid(True)

df.number.str.strip("q").str[:-1].astype(int).value_counts().sort_index().cumsum().plot(kind='bar', ax=axs[1], title="Accumulated sum of interactions over iterations' count")
axs[1].set_ylabel("Accumulated sum of iterations count.")
axs[1].set_xlabel("Iterations")
axs[1].grid(True)

plt.tight_layout()
plt.show()


x = df.groupby("is_devfeedback_exist").apply(lambda g: g.number).unstack().T
if df.is_devfeedback_exist.all():
    xx = x.copy()
else:
    xx = x[True].dropna()
# Calculate and print statistics based on the extracted information
total_interactions = xx.str.strip('q').str[:-1].astype(int).max()
total_interactions = xx.str.strip('q').str[:-1].nunique()
total_iterations = xx.shape[0]
print(f"\n\n{total_interactions} interactions are done")
print(f"{total_iterations} iterations are done")
print(f"Iterations per interaction ratio: {round(total_iterations / total_interactions, 2)}")
print()




