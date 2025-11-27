#!/home/amir/.venv_base/bin/python3
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import json
import os
import amir_analysis_functions
import zipfile

def function(file, file_name):
	print(f"\n\nAnalyzing {file_name} ...")
	if not file:
		print("Empty file")
		return pd.DataFrame(columns=['line_num', 'file', 'function', 'params', 'result']).set_index("line_num")
	lst = []
	for line_num, line in enumerate(file):
		if not (('FAILED' in line) or ('PASSED' in line)):
			continue
		if (".py" in line) and ("::" in line):
			if line.count("::") > 1:
				line = line[::-1].replace("::", '-------', 1)[::-1]
			if line.startswith("PASSED ") or line.startswith("FAILED "):
				result = line.split()[0].strip()					
				file_name = line.split()[1].strip().split("::")[0].strip()
				func_name = (line.split("::")[1].strip().split("PASSED")[0].strip() if ' PASSED ' in line else line.split("::")[1].strip().split("FAILED")[0].strip() if ' FAILED ' in line else line.split("::")[1].strip().split("SKIPPED")[0].strip())
				params = ""
				if ('[' in func_name) and (']' in func_name) and (not x.strip().endswith("]")):
					params = "[" + func_name.split("[")[1].strip().split("]")[0].strip() + "]"
					func_name = func_name.split("[")[0].strip()
			else:
				x = line.split("::")
				file_name = x[0].strip()
				with_func_name = x[1].strip()
				x = (with_func_name.split("PASSED") if ' PASSED ' in with_func_name else with_func_name.split(" FAILED ") if " FAILED" in with_func_name else with_func_name.split(" SKIPPED "))[0]
				params = ""
				if ('[' in x) and (']' in x) and (not x.strip().endswith("]")):
					params = "[" + with_func_name.split("[")[1].strip().split("]")[0].strip() + "]"
					func_name = with_func_name.split("[")[0].strip()
					result = with_func_name.split("]")[1].strip().split()[0]
				else:
					try:
						func_name = with_func_name.split()[0].strip()
						result = with_func_name.split()[1].strip()
					except:
						breakpoint()
			# if line_num in (7902, 8090):
				# print(line)
				# print(file_name)
				# print(func_name)
				# print(result)
				# print("------------------")
			lst.append((line_num, file_name, func_name, params, result))

	df = pd.DataFrame(lst, columns=['line_num', 'file', 'function', 'params', 'result']).set_index("line_num")
	df = df.drop_duplicates()
	df.function = df.function.str.replace("-------", "::")
	if df.empty:
		return df

	duplicates = df.groupby(['file', 'function', 'params']).apply(len).gt(1).loc[lambda x: x].index.to_list()
	if duplicates:
		print("Duplicates found:")
		for file, func, param in duplicates:
			_str = f"{file}-{func}-{param}"
			_ser = df[['file', 'function', 'params']].astype(str).apply("-".join, axis=1)
			indecies = _ser.eq(_str).loc[lambda x: x].index.to_list()
			print(df[df.file.eq(file) & df.function.eq(func) & df.params.eq(param)].sort_values(["file", "function", "params"]).to_markdown())
			# indecies = (df.file.eq(file) & df.function.eq(func) & df.params.eq(param)).loc[lambda x: x].index.to_list()
			for e, i in enumerate(file) :
				if e in indecies:
					print(f"{e}: {i.strip()}")
			print("--------------")	
	return df



input("\nDownload the GD folder, and then press any key: ")
correct_zip_file = False
path = "/home/amir/Downloads"
while not correct_zip_file:
	zip_files = [i for i in os.listdir(path) if i.endswith(".zip")]
	print(zip_files)
	zip_files_details = [(amir_analysis_functions.seconds_since_last_modification(f"{path}/{zf}"), zf) for zf in zip_files]
	downloaded_before_secs, latest_zip_file = sorted(zip_files_details, key=lambda x: x[0])[0]
	downloaded_before = amir_analysis_functions.seconds_to_hh_mm_ss(downloaded_before_secs)
	print("> Latest zip file:", latest_zip_file)
	print("> Downloaded before:")
	print(downloaded_before)
	print()
	ui = input("\nDo you want to proceed with the above zip file? [yes|no] ")
	if ui == "yes":
		correct_zip_file = True



zip_path = f"/home/amir/Downloads/{latest_zip_file}"
extract_to = "/home/amir/Downloads"

with zipfile.ZipFile(zip_path, 'r') as zf:
    zf.extractall(extract_to)
    top_level = os.path.commonpath(zf.namelist()).split(os.sep)[0]
print("Extracted folder name:", top_level)

os.chdir(f"{path}/{top_level}")

root = [i for i in os.listdir() if i.endswith(".json")]
if len(root) > 1:
	raise Exception("More than one json file found")
root = root[0]
root = json.load(open(root, 'r'))

print("Hints:", root['hints'])
print("Language:", root['language'])

ftp_root = root['fail_to_pass']
ptp_root = root['pass_to_pass']

# if len(set(ftp_root)) == len(ftp_root):
# 	print("No duplicates in fail_to_pass")
# else:
# 	dups = [i for i in set(ftp_root) if ftp_root.count(i) > 1]
# 	print("Duplicates found in fail_to_pass")
# 	print(*dups, sep="\n")

# if len(set(ptp_root)) == len(ptp_root):
# 	print("No duplicates in pass_to_pass")
# else:
# 	dups = [i for i in set(ptp_root) if ptp_root.count(i) > 1]
# 	print("Duplicates found in pass_to_pass")
# 	print(*dups, sep="\n")


for i in os.listdir("logs"):
	if i.endswith("_after.log"):
		logs_after = open("logs/" + i, 'r').readlines()
	elif i.endswith("_before.log"):
		logs_before = open("logs/" + i, 'r').readlines()
	elif i.endswith("_base.log"):
		logs_base = open("logs/" + i, 'r').readlines()

logs_after[-5:]
print("\nlogs_base:")
print(*[i for i in logs_base if ('===' in i) and ('in' in i)], sep="\n")
print("\nlogs_before:")
print(*[i for i in logs_before if ('===' in i) and ('in' in i)], sep="\n")
print("\nlogs_after:")
print(*[i for i in logs_after if ('===' in i) and ('in' in i)], sep="\n")


logs_after_df = function(logs_after, "logs_after")
logs_before_df = function(logs_before, "logs_before")
logs_base_df = function(logs_base, "logs_base")	

print("\n\n")

# At least one failed test in base log is present in P2P
logs_base_failed = logs_base_df[logs_base_df.result.eq("FAILED")]
if not logs_base_failed.empty:
	logs_base_failed_str_series = logs_base_failed.file + "::" + logs_base_failed.function + logs_base_failed.params
	failed_in_base_and_present_in_ptp = logs_base_failed_str_series[logs_base_failed_str_series.isin(ptp_root)].to_list()
	if failed_in_base_and_present_in_ptp:
		print("\n\nFailed in base AND present in P2P:")
		print(*failed_in_base_and_present_in_ptp, sep="\n")
		print()
else:
	print(f"✅ Passed the rule: (At least one failed test in base log is present in P2P)\n\tlogs_base_failed: {logs_base_failed.shape[1]}")


# At least one failed test in after log is present in F2P / P2P
failed_in_after_and_present_in_ptp = pd.DataFrame([])
failed_in_after_and_present_in_ftp = pd.DataFrame([])

logs_after_failed = logs_after_df[logs_after_df.result.eq("FAILED")]
if not logs_after_failed.empty:
	logs_after_failed_str_series = logs_after_failed.file + "::" + logs_after_failed.function + logs_after_failed.params
	failed_in_after_and_present_in_ptp = logs_after_failed_str_series[logs_after_failed_str_series.isin(ptp_root)].to_list()
	if failed_in_after_and_present_in_ptp:
		print("\n\n❌ Failed in after AND present in P2P:")
		print(*failed_in_after_and_present_in_ptp, sep="\n")
		print()
	failed_in_after_and_present_in_ftp = logs_after_failed_str_series[logs_after_failed_str_series.isin(ftp_root)].to_list()
	if failed_in_after_and_present_in_ftp:
		print("\n\n❌ Failed in after AND present in F2P:")
		print(*failed_in_after_and_present_in_ftp, sep="\n")
		print()
else:
	print(f"✅ Passed the rule: (At least one failed test in after log is present in F2P / P2P)\n\tlogs_after_failed: {logs_after_failed.shape[1]}\n\tfailed_in_after_and_present_in_ptp: {failed_in_after_and_present_in_ptp.shape[1]}\n\tfailed_in_after_and_present_in_ftp: {failed_in_after_and_present_in_ftp.shape[1]}")

# At least one F2P test is present and successful in before log
before_passed = logs_before_df[logs_before_df.result.eq("PASSED")]
before_passed_str_series = before_passed.file + "::" + before_passed.function + before_passed.params
f2p_in_before_passed = before_passed_str_series[before_passed_str_series.isin(ftp_root)].to_list()
if f2p_in_before_passed:
	print("❌ Failed the rule: (At least one F2P test is present and successful in before log)")
	print(*f2p_in_before_passed, sep="\n")
	print()
else:
	print(f"✅ Passed the rule: (At least one F2P test is present and successful in before log)\n\tbefore_passed: {before_passed.shape[0]}")

ptp_root
logs_base_str_series = logs_base_df.file + "::" + logs_base_df.function + logs_base_df.params


# Empty FAIL_TO_PASS
if ftp_root:
	print(f"✅ Passed the rule: (Empty FAIL_TO_PASS)\n\tftp_root: {len(ftp_root)}")
else:
	print(f"❌ Failed the rule: (Empty FAIL_TO_PASS)\n\tftp_root: {len(ftp_root)}")


# PR has more than 15 test files
test_files_count = sum([('test' in fn) and fn.endswith(".py") for fn in root['files_changed']])
if test_files_count>15:
	print(f"❌ Failed the rule: (PR has more than 15 test files)\n\ttest_files_count: {test_files_count}")
else:
	print(f"✅ Passed the rule: (PR has more than 15 test files)\n\ttest_files_count: {test_files_count}")

# PR has more than 50 updated files
total_files_count = sum([fn.endswith(".py") for fn in root['files_changed']])
if total_files_count >50:
	print(f"❌ Failed the rule: (PR has more than 50 updated files)\n\ttotal_files_count: {total_files_count}")
else:
	print(f"✅ Passed the rule: (PR has more than 50 updated files)\n\ttotal_files_count: {total_files_count}")



# Empty log file (except _post_agent_patch.log)
for i in os.listdir("logs"):
	if i.endswith(".log") and (not i.endswith("_post_agent_patch.log")):
		f = open(f"logs/{i}", 'r').read()
		if os.path.getsize("logs/" + i) == 0:
			print(f"❌ Failed the rule: (Empty log file: logs/{i})")
		elif (not '= PASSES =' in f):
			print(f"❌ Failed the rule: (Empty log file: logs/{i}) | doesn't have <= 'PASSES' => in it.")
		elif i.endswith("_before.log") and (not '= FAILURES =' in f):
			print(f"❌ Failed the rule: (Empty log file: logs/{i}) | doesn't have <= 'FAILURES' => in it.")
		else:
			print(f"✅ Passed the rule: (Empty log file: logs/{i})")