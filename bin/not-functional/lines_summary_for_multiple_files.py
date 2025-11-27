#!/home/amir/.venv_base/bin/python3

import sys
if len(sys.argv) < 3:
	print("You must pass two or more .txt files names...\nAborting....")
	exit()

files_names = sys.argv[1:]
d = {}
print("Total lines: ")
for e, fn in enumerate(files_names):
	d[e] = open(fn, 'r').read().splitlines()
	print(f"{fn}: {len(d[e])}")
print()
for e1, fn1 in enumerate(files_names):
	for e2, fn2 in enumerate(files_names):
		if e2 >= e1:
			continue
		print(f"\n......... {fn1} - {fn2} ...........\n")
		first_file = d[e1]
		second_file = d[e2]
		print(f"{len(set(first_file)&set(second_file))} lines are common in both {fn1} and {fn2}")
		print(f"{len(set(first_file)-set(second_file))} lines are only in {fn1}")
		print(f"{len(set(second_file)-set(first_file))} lines are only in {fn2}")
