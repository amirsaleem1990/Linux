#!/home/amir/.venv_base/bin/python3

print("""
	=========== Example ===========
	
	import os
	from save_locals_to_disK import save_locals_to_disk
	zz = list(range(200000000))
	save_locals_to_disk({i : (id(eval(i)), type(eval(i))) for i in dir()}, os.getcwd())
""")
def save_locals_to_disk(dict__, base_dir):
	import pandas as pd
	from IPython.display import display
	import sys
	import time
	import pickle
	import os
	import ctypes

	# {i : id(eval(i)) for i in dir()}
	dict__ = {k : v for k,v in dict__.items() if not k in ['In', 'Out', 'exit', 'quit', 'locals_'] and (not '__' in k)  and (not k.startswith("_")) }

	if dict__ == {}:
		print("You dont supply any argument, please type \nsave_locals_to_disk"
			"({i : (id(eval(i)), type(eval(i))) for i in dir()}, os.getcwd())\n")
		return None
	
	locals = {k : v[0] for k, v in dict__.items() if str(v[1]).strip('"<class ').strip(">").strip("'") not in ["method", "function", "module"]}
	# print(locals)	
	data_dict__ = {k : ctypes.cast(v, ctypes.py_object).value for k,v in locals.items()}
	
	f = pd.DataFrame([(k, sys.getsizeof(v)) for k,v in data_dict__.items()], columns=["Object", "bytes"]).sort_values("bytes", ascending=False)
	f = f.assign(MB=f.bytes/1000000, GB=f.bytes/1000000/1000).round(4)
	display(f)
	
	ans = input("Are you need to proceed? [y|n]: ")
	if ans != 'y':
		print("Interepted ............. ")
		return None
    # orignal_dir = os.getcwd()

	name = base_dir + "/" + str(int(time.time()))
	os.mkdir(name)
	os.chdir(name)
	# print(data_dict__)
	for k,v in data_dict__.items():
		try:
			pickle.dump(v, open(k, "wb"))
		except Exception as e:
			print(f">>>>>>>>>>>>>>>>>>>> FAILED {k}")
#     os.chdir(orignal_dir)