#!/home/amir/.venv_base/bin/python3

import json
import os
import clipboard

test_files_master = open("/media/DATA/SWE/Dockerization/REPOS/tests.json", 'r').read().splitlines()
test_files_master = json.loads("\n".join([i.split("//")[0] for i in test_files_master]))
repo = os.popen("git remote get-url origin").read().strip()
repo_name = repo.replace('https://github.com/', '')
repo_url = repo_name
if repo_name.endswith(".git"):
	repo_url = repo_name.replace(".git", "")
	repo_name = repo_name.replace(".git", "").split("/")[-1]

to_copy = f"""I am trying to dockerize {repo_url}, and test `pytest -rA {test_files_master.get(repo_name, "____________________________________")}'. However I am getting the above error. 

Visit the repo, explore it, and let me know how to solve this error
Note: Don't give any advise before exploring the current repo, so first go and visit it.
"""

clipboard.copy(to_copy)
print(to_copy)