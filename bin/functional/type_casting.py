#!/home/amir/.venv_base/bin/python3

# print("We noticed that this method changes the data, for details open /home/amir/github/short-codes/Type_casting_changes_the_data.ipynb")
# import sys
# sys.exit()





print("""
Usage:
	import sys
	sys.path += ['/amir_bin/']
	import type_casting 
	type_casting.Type_casting(id(df)) # call it only, this function not return anything, but your <df> is now type casted.
""")
import pandas as pd
import matplotlib.pyplot as plt
import ctypes
def Type_casting(df_id):
	from termcolor import colored
	def type_casting(type_, down_cast):

		before = df.memory_usage(deep=True).sum()

		if type_ == "O":
			for obj_col in (df.select_dtypes(type_).nunique() / len(df)).where(lambda x:x < .5).dropna().index:
				modified_col = df[obj_col].astype(down_cast)
				if hash(tuple(modified_col)) == original_hash[original_hash.Column.eq(obj_col)].hash_.iloc[0]:
					df[obj_col] = df[obj_col].astype(down_cast)
				else:
					print(colored(f"\nFaild to down cast the '{obj_col}' variable", "red"))
		else:
			for col_ in df.dtypes[df.dtypes == type_].index.to_list():
				modified_col = pd.to_numeric(df[col_], downcast = down_cast)
				if hash(tuple(modified_col)) == original_hash[original_hash.Column.eq(col_)].hash_.iloc[0]:
					# df[col_] = df[col_].astype(down_cast)
					df[col_] = pd.to_numeric(df[col_], downcast = down_cast)
				else:
					print(colored(f"\nFaild to down cast the '{col_}' variable", "red"))		
		after = df.memory_usage(deep=True).sum()
		
		# print("Reduced after <{:>9}> {} down casting : {:>5} %".format(down_cast, '', round((1-after/before)*100, 2)))

	def hash_(dataframe: pd.DataFrame):
		return (
				dataframe
				.apply(lambda x: hash(tuple(x)))
				.rename("hash_")
				.rename_axis("Column")
				.reset_index()
			)

	df = ctypes.cast(df_id, ctypes.py_object).value
	original_hash = hash_(df)

	# b = df.memory_usage(deep=True).sum()
	# b_ = df.memory_usage(deep=True)

	type_casting(int, 'integer')
	type_casting(float, 'float')
	type_casting("O", 'category')

	# a = df.memory_usage(deep=True).sum()
	# a_ = df.memory_usage(deep=True)


	# print(f"\n\nTotal Reduction: {round((1-a/b)*100, 2)} %\n")
	# print(f"Before : {round(b    / 1024 ** 2, 2) } MB")
	# print(f"After  : {round(a    / 1024 ** 2, 2) } MB")
	# print(f"Reduced: {round((b-a)/ 1024 ** 2, 2) } MB")
	# ((a_ / b_).sort_values().reset_index(drop=True) // .1 * 10).plot(kind='hist',
	# 																 grid=True,
	# 																 figsize=(14,7));
	# plt.xlabel("Reduction % ", size=14) #, color='red');
	# plt.ylabel("Frequency"   , size=14) #, color='red');
	# plt.title ("Reduction % plot", size=16, color='red')
	# plt.show()

	plt.show()
