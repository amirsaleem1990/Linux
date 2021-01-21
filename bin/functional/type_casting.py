print("""
Usage:
	improt sys
	sys.path += ['/amir_bin/']
	type_casting.Type_casting(id(df)) # call it only, this function not return anything, but your <df> is now types casted.
""")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ctypes
def Type_casting(df_id):
	def type_casting(type_, down_cast):
		df = ctypes.cast(df_id, ctypes.py_object).value

		before = df.memory_usage(deep=True).sum()

		if type_ == "O":
				for obj_col in (df.select_dtypes(type_).nunique() / len(df)).where(lambda x:x < .5).dropna().index:
					df[obj_col] = df[obj_col].astype(down_cast)
		
		else:
			for col_ in df.dtypes[df.dtypes == type_].index:
				df[col_] = pd.to_numeric(df[col_], downcast = down_cast)

		after = df.memory_usage(deep=True).sum()
		
		print("Reduced after <{:>9}> {} down casting : {:>5} %".format(down_cast, '', round((1-after/before)*100, 2)))

	df = ctypes.cast(df_id, ctypes.py_object).value
	b = df.memory_usage(deep=True).sum()
	b_ = df.memory_usage(deep=True)

	type_casting(int, 'integer')
	type_casting(float, 'float')
	type_casting("O", 'category')

	a = df.memory_usage(deep=True).sum()
	a_ = df.memory_usage(deep=True)
	print(f"\n\nTotal Reduction: {round((1-a/b)*100, 2)} %\n\n")

	((a_ / b_).sort_values().reset_index(drop=True) // .1 * 10).plot(kind='hist',
																	 grid=True,
																	 figsize=(14,7));
	plt.xlabel("Reduction % ", size=14) #, color='red');
	plt.ylabel("Frequency"   , size=14) #, color='red');
	plt.title ("Reduction % plot", size=16, color='red');

	plt.show()
