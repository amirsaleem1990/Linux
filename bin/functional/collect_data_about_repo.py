#!/home/amir/.venv_base/bin/python3

import json
import os
test_files_master = open("/media/DATA/SWE/Dockerization/REPOS/tests.json", 'r').read().splitlines()
test_files_master = json.loads("\n".join([i.split("//")[0] for i in test_files_master]))
pre_defined_commands = json.load(open("/media/DATA/SWE/Dockerization/REPOS/pre_defined_commands.json", 'r'))
repo = os.popen("git remote get-url origin").read().strip()
repo_name = repo.replace('https://github.com/', '')
if repo_name.endswith(".git"):
    repo_name = repo_name.replace(".git", "").split("/")[-1]

test_files = test_files_master.get(repo_name)
print("Test files :", test_files)
print("Predifindes:", pre_defined_commands.get(repo_name))
print()
print("Dockerfile:")
dockerfile = open("Dockerfile", 'r').read().splitlines()
lines = []
pips = []
for line in dockerfile:
    if ('alias test' in line) or (not line) or ('COPY' in line) or ('WORKDIR' in line) or ('FROM ' in line):
        continue
    if '||' in line:
        line = line.split("||")[0]
        lines.append(line)
    elif 'RUN pip install' in line:
        if line.strip().endswith("."):
            lines.append(line)
        else:
            pips.append(line.replace("RUN pip install ", "").replace("--upgrade", ""))
    elif line.startswith("pytest -rA"):
        lines.append(f"# {line}")
    else:
        lines.append(line)

print(f"""
FROM python:3.11
WORKDIR /app
COPY . .
{'RUN apt-get update' if not 'RUN apt-get update' in '\n'.join(dockerfile) else ''}"""
)
print(f"pip install --upgrade {'pip' if not ' pip ' in ' '.join(pips) else ''} {'pytest' if not ' pytest' in ' '.join(pips) else ''}", end=" " if pips else "\n")
if pips:
    print("".join(pips))
dockerfile = "\n".join(lines)
print(dockerfile)
print(f'pytest -rA {test_files}')
print()
