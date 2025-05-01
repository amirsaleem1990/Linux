
#!/home/amir/.venv_base/bin/python3

def join_summary(s1, s2):
	s1 = set(s1)
	s2 = set(s2)
	print("In first       : ", len(s1))
	print("In second      : ", len(s2))
	print("Intersection   : ", len(s1 & s2))
	print("Only in first  : ", len(s1 - s2))
	print("Only in second : ", len(s2 - s1))


def remove_identical_columns(df) -> list:
	import pandas as pd
	"""
	Retuns a list of columns that are not identical
	"""
	print("Retuns a list of columns that are not identical")
	# x = df.astype(str).apply(lambda col: hash(tuple(col))).rename("hash").rename_axis("col").reset_index()
	hash_dict = {}
	for col_name in df.columns.to_list():
		hash_dict[col_name] = hash(tuple(df[col_name].astype(str)))
	x = pd.Series(hash_dict).rename("hash").rename_axis("col").reset_index()
	duplicated_hashs = x.hash.value_counts().where(lambda x: x>=2).dropna().index.to_list()

	for i in duplicated_hashs:
		print(f"\n>>>>>>>>>>>>>>>>> '{i}'")
		cols  = sorted(x[x.hash.eq(i)].col.to_list())
		print(len(cols))
		print(cols)


	non_duplicate_columns = x.drop_duplicates(subset="hash", keep="first").col.to_list()
	non_duplicate_columns += x[~x.hash.isin(duplicated_hashs)].col.to_list()
	non_duplicate_columns = list(set(non_duplicate_columns))

	print("\nAll columns count    :", df.shape[1])
	print("Non-identical columns:", len(non_duplicate_columns))
	return non_duplicate_columns

def standardize(df):
	print("\nReturning tuple of two values: 1- df, 2- min_max_std_dict\n")
	potential_bool_cols = df.select_dtypes("number").nunique().eq(2).where(lambda x: x==True).dropna().index.to_list()
	bool_with_type_number =  df[potential_bool_cols].apply(lambda x: sorted(set(x)) == [0,1]).where(lambda x: x==True).dropna().index.to_list()
	int_cols = df.select_dtypes("number").apply(lambda x: (x.eq(x//1).all())).where(lambda x: x==True).dropna().index.to_list()
	cols_to_standardize = list(set(int_cols) - set(bool_with_type_number))
	min_max_std_dict = df[cols_to_standardize].agg([min,max,"std"]).to_dict()
	df[cols_to_standardize] = (df[cols_to_standardize] - df[cols_to_standardize].mean()) / df[cols_to_standardize].std()
	print("\nReturning tuple of two values: 1- df, 2- min_max_std_dict\n")
	return df, min_max_std_dict




def get_model_to_be_built(decision_tree__binary_classification, logistic_regression__binary_classification, random_forest__binary_classification, SVM__binary_classification, SVM_Linear__binary_classification, LDA__binary_classification, KNN__binary_classification,decision_tree__multiclass_classification, random_forest__multiclass_classification, SVM__multiclass_classification, SVM_Linear__multiclass_classification, LDA__multiclass_classification, KNN__multiclass_classification,decision_tree__regression, random_forest__regression, linear_regression__regression, KNN__regression, ridge__regression, lasso__regression, SVM__regression):

	models_to_be_built = []

	# Binary Classification
	if decision_tree__binary_classification:
		models_to_be_built.append("'Decision Tree'")
	if logistic_regression__binary_classification:
		models_to_be_built.append("'Logistic Regression'")
	if random_forest__binary_classification:
		models_to_be_built.append("'Random Forest'")
	if SVM__binary_classification:
		models_to_be_built.append("'Support Vector Machine'")
	if SVM_Linear__binary_classification:
		models_to_be_built.append("'Support Vector Machine (Linear)'")
	if LDA__binary_classification:
		models_to_be_built.append("'Linear Discriminant Analysis'")
	if KNN__binary_classification:
		models_to_be_built.append("'K-Nearest Neighbors")

	# Multiclass Classification
	if decision_tree__multiclass_classification:
		models_to_be_built.append('Decision Tree')
	if random_forest__multiclass_classification:
		models_to_be_built.append('Random Forest')
	if SVM__multiclass_classification:
		models_to_be_built.append('Support Vector Machine')
	if SVM_Linear__multiclass_classification:
		models_to_be_built.append('Support Vector Machine (Linear)')
	if LDA__multiclass_classification:
		models_to_be_built.append('Linear Discriminant Analysis')
	if KNN__multiclass_classification:
		models_to_be_built.append('K-Nearest Neighbors')

	# Regression
	if decision_tree__regression:
		models_to_be_built.append('Decision Tree')
	if random_forest__regression:
		models_to_be_built.append('Random Forest')
	if linear_regression__regression:
		models_to_be_built.append('Linear Regression')
	if KNN__regression:
		models_to_be_built.append('K-Nearest Neighbors')
	if ridge__regression:
		models_to_be_built.append('Ridge Regression')
	if lasso__regression:
		models_to_be_built.append('Lasso Regression')
	if SVM__regression:
		models_to_be_built.append('Support Vector Machine')

	names_maping = {
		"K-Nearest Neighbors" : "k Nearest Neighbor",
		"Ridge Regression" : "Ridge Regresssion",
		"Lasso Regression" : "Lasso Regresssion"
	}
	models_to_be_built = [i if not i in names_maping else names_maping[i] for i in models_to_be_built]
	return models_to_be_built




def train_all_models(
		df, target_variable_name, n_iter=30, random_forest_n_iter=20, svm_n_iter=2, cv=2, normalization=False,
		decision_tree__binary_classification=False, logistic_regression__binary_classification=False, random_forest__binary_classification=False, SVM__binary_classification=False, SVM_Linear__binary_classification=False, LDA__binary_classification=False, KNN__binary_classification=False,
		decision_tree__multiclass_classification=False, random_forest__multiclass_classification=False, SVM__multiclass_classification=False, SVM_Linear__multiclass_classification=False, LDA__multiclass_classification=False, KNN__multiclass_classification=False,
		decision_tree__regression=False, random_forest__regression=False, linear_regression__regression=False, KNN__regression=False, ridge__regression=False, lasso__regression=False, SVM__regression=False
	):


	models_to_be_built = get_model_to_be_built(decision_tree__binary_classification, logistic_regression__binary_classification, random_forest__binary_classification, SVM__binary_classification, SVM_Linear__binary_classification, LDA__binary_classification, KNN__binary_classification,decision_tree__multiclass_classification, random_forest__multiclass_classification, SVM__multiclass_classification, SVM_Linear__multiclass_classification, LDA__multiclass_classification, KNN__multiclass_classification,decision_tree__regression, random_forest__regression, linear_regression__regression, KNN__regression, ridge__regression, lasso__regression, SVM__regression)

	# def choose_models(models_list):
	#     print("\nnChoolse Models by index,\n"
	#           "for multiple choose use comma for saperation\n"
	#           "for range use double dot saperation (both sides are inclusive):\n")
	#     print(f"0-\tAll")
	#     for e,i in enumerate(models_list, start=1):
	#         print(f"{e}-\t{i}")
	#     indexes = input().replace(" ", "").split(",")
	#     if '..' in ''.join(indexes):
	#         new_indexes = []
	#         for index in indexes:
	#             if '..' in index:
	#                 x = index.split("..")
	#                 for i in range(int(x[0]), int(x[-1])+1):
	#                     new_indexes.append(str(i))
	#             else:
	#                 new_indexes.append(index)
	#         indexes = new_indexes

	#     # Here I subtract `int(i)-1` because we started numbers in `enumerate` from `1`
	#     indexes = [int(i)-1 for i in indexes]

	#     # [-1] when user choose `0` for `All`
	#     if indexes == [-1]:
	#         models_to_be_built = models_list
	#     else:
	#         models_to_be_built = [models_list[i] for i in indexes] 
	#     # models_to_be_built_new = [] 
	#     # for i in models_to_be_built:
	#     #     for k,v in models_names_maping.items():
	#     #         if v == i:
	#     #             models_to_be_built_new.append(k)
	#     # return models_to_be_built_new
	#     names_maping = {
	#         "K-Nearest Neighbors" : "k Nearest Neighbor",
	#         "Ridge Regression" : "Ridge Regresssion",
	#         "Lasso Regression" : "Lasso Regresssion"
	#     }
	#     models_to_be_built = [i if not i in names_maping else names_maping[i] for i in models_to_be_built]
	#     return models_to_be_built

	import sys
	sys.path.append("/home/amir/github/LFD_projects_6/36-EDA_tool/auto_eda_modeling_app/modeling_progress/")
	import train_all_models 
	import utils
	import pandas as pd
	import pickle
	import os

	pickle.dump(target_variable_name, open("target_variable_name.pkl", 'wb'))

	target_type = str(df[target_variable_name].dtype)
		
	if target_type == "object":
		if df[target_variable_name].nunique() == 2:
			modeling_problem = "binary_classfication"
		else:
			modeling_problem = "multi_class_classfification"
	elif target_type == "bool":
		modeling_problem = "binary_classfication"
		df[target_variable_name] = df[target_variable_name].astype(int)
	elif sorted(df[target_variable_name].unique()) == [0, 1]:
		modeling_problem = "binary_classfication"
	elif target_type.startswith("int") or target_type.startswith("float"):
		modeling_problem = "regression"
	else:
		raise Exception("Error in type of target variable, it should be in ('object', 'regression')")

	models_names_maping = utils.models_names_maping

	# if modeling_problem == "binary_classfication":
	#     binary_classification_models = utils.binary_classification_models
	#     models_to_be_built = choose_models(models_list=binary_classification_models)

	# elif modeling_problem == "multi_class_classfification":
	#     multiclass_classification = utils.multiclass_classification
	#     models_to_be_built = choose_models(models_list=multiclass_classification)

	# elif modeling_problem == "regression":
	#     regression_models = utils.regression_models
	#     models_to_be_built = choose_models(models_list=regression_models)
	print("\nYou have selected the following models to be built: ")
	print(*models_to_be_built, sep="\n")
	pickle.dump(models_to_be_built, open("models_to_be_built.pkl", 'wb'))


	# inp = input(
	#     "Do you want to exlude some predictors? (Please choose a number)\n"
	#     "1- Yes\n"
	#     "2- No\n"
	# )
	# if inp == "1":
	#     print("\nChoolse columns to exclude by index,\n"
	#           "for multiple choose use comma for saperation\n"
	#           "for range use double dot saperation (both sides are inclusive):\n")
	#     for e, i in enumerate(sorted(df.columns.drop(target_variable_name).to_list())):
	#         print(f"{e}-\t{i}")
	#     print("\nChoolse columns to exclude by index,\n"
	#           "For no exclude press Enter\n"
	#           "For multiple choose use comma for saperation\n"
	#           "For range use double dot saperation (both sides are inclusive):\n")
	#     indexes = input().replace(" ", "").split(",")

	#     # If use doesn't want to exclude any column
	#     if len(indexes) == 1 and (not indexes[0]):
	#         vars_to_be_used_in_modeling = df.columns.to_list()
	#     else:
	#         if '..' in ''.join(indexes):
	#             new_indexes = []
	#             for index in indexes:
	#                 if '..' in index:
	#                     x = index.split("..")
	#                     for i in range(int(x[0]), int(x[-1])+1):
	#                         new_indexes.append(str(i))
	#                 else:
	#                     new_indexes.append(index)
	#             indexes = new_indexes
	#         indexes = list(map(int, indexes))

	#         vars_to_be_used_in_modeling = [i for e, i in enumerate(df.columns.drop(target_variable_name).to_list()) if not e in indexes] 
	#         vars_to_be_used_in_modeling += [target_variable_name]
	#         pickle.dump(vars_to_be_used_in_modeling, open("vars_to_be_used_in_modeling.pkl", 'wb'))

	#         df = df[vars_to_be_used_in_modeling]

	# default_perams = {
	#     "n_iter":30,
	#     "random_forest_n_iter":20,
	#     "svm_n_iter":2,
	#     "cv":2,
	#     "normalization":False    
	# }
	# print("\nPerameters: ")
	# for k,v in default_perams.items():
	#     p = input(f"'Default '{k}'='{v}', Press a new value if you want to assign a new value, of press Enter to proceed with the defult: ")
	#     if p == '':
	#         continue
	#     elif isinstance(v, bool):
	#         default_perams[k] = bool(p)
	#     if isinstance(v, int):
	#         default_perams[k] = int(p)

	obj = train_all_models.TrainDifferentMlModes(
		dataframe=df, 
		target_variable_name_=target_variable_name, 
		models_to_be_built = models_to_be_built,
		hyperparameters_json_path="/home/amir/github/LFD_projects_6/36-EDA_tool/auto_eda_modeling_app/hyperparameters.json",   
		n_iter=n_iter,
		random_forest_n_iter=random_forest_n_iter,
		svm_n_iter=svm_n_iter,
		cv=cv,
		normalization=normalization    
		)
	obj.main()
	best_models_summary = obj.get_best_models_summary()
	best_models_summary.to_pickle("best_models_summary.pkl")
	modeling_problem = ' '.join(list(map(str.capitalize, modeling_problem.split('_'))))
	
	best_models_summary = (
		best_models_summary.drop(
			["predictions", "best_model_object", "optimal_hyperparameters", "modeling_problem"], 
			axis=1
		)
		.rename(
			columns={
				"model_name" : "Model", 
				"start_time" : "Start Time", 
				"end_time" : "End Time", 
				"time_consumed" : "Time Consumed",
				"baseline_error" : "Baseline Error",
				"error_decreased_percentage" : "% of Error decreased (0-100)",
			}
		)
	)
	actual_vs_prediction_plots = False
	confusion_metrix_plots = False

	if "rmse" in best_models_summary.columns.to_list():
		best_models_summary = best_models_summary.rename(columns={
			"rmse" : "RMSE"
		}).sort_values("RMSE")
		cols = ['Baseline Error', 'RMSE']
		best_models_summary[cols] = best_models_summary[cols].applymap(lambda x: format(x, ","))
		actual_vs_prediction_plots=True

	elif "error" in best_models_summary.columns.to_list():
		best_models_summary = best_models_summary.rename(columns={
			"error" : "Error",
			"f1_score" : "F1 score"
		}).sort_values("Error")
		confusion_metrix_plots=True

	best_models_summary.index = range(1, len(best_models_summary)+1)
	
	best_models_summary['Model'] = best_models_summary['Model'].replace(models_names_maping)
	pickle.dump(best_models_summary, open("best_models_summary_updated.pkl", 'wb'))


def confusion_metrix_plot(actual, predicted, title="", normalize=None):
	import matplotlib.pyplot as plt
	import numpy
	from sklearn import metrics
	confusion_matrix = metrics.confusion_matrix(actual,predicted, normalize=normalize)
	cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])
	cm_display.plot()
	plt.title(title)
	plt.show() 



def convert_units(from_unit, value, rounded_to=3):
	"""
	>>> convert_units('gb', value=0.00009999)
	'99.99 KB'
	>>> convert_units('by', value=999900)
	'999.9 KB'
	>>> convert_units('gb', value=0.099)
	'99.0 MB'
	"""
	units = {
		'by': 1, # bytes
		'kb': 1000,
		'mb': 1000_000,
		'gb': 1000_000_000,
	}
	if not from_unit.lower() in units:
		return "Invalid unit"
	total_bytes = value * units[from_unit.lower()]
	if total_bytes < 1000:
		return f"{total_bytes} B"
	elif total_bytes < 1000_000:
		return f"{round(total_bytes/1000, rounded_to)} KB"
	elif total_bytes < 1000_000_000:
		return f"{round(total_bytes/1000_000, rounded_to)} MB"
	else:
		return f"{round(total_bytes/1000_000_000, rounded_to)} GB"



def get_data_from_localhost_mysql_db(query, database='Practice', port=3306, host="localhost"):
	from dotenv import load_dotenv
	import pandas as pd
	import sqlalchemy
	import os

	env_file_path = list(os.popen("ls /home/a*/g*b/A*l/.env"))[0].strip()
	load_dotenv(dotenv_path=env_file_path)
	
	user=os.environ.get("localhost_mysql_user")
	passw=os.environ.get("localhost_mysql_password")


	conn = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{passw}@{host}:{port}/{database}?charset=utf8').connect()

	df = pd.DataFrame(
			conn.execute(sqlalchemy.text(query))
		)
	conn.close()
	return df


def connect_to_mysql_db(user=None, passw=None, host="localhost", database='Practice', port=3306):
	print("\nThis function returns a tuple: `conn` and `connect`\n")
	import sqlalchemy

	if user is None or passw is None:
		import os
		from dotenv import load_dotenv
		env_file_path = list(os.popen("ls /home/a*/g*b/A*l/.env"))[0].strip()
		load_dotenv(dotenv_path=env_file_path)
	
		user=os.environ.get("localhost_mysql_user")
		passw=os.environ.get("localhost_mysql_password")

	conn = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{passw}@{host}:{port}/{database}?charset=utf8')
	connect = conn.connect()
	return conn, connect



def fuzzy_matching(val_1: str, val_2: str):
	from fuzzywuzzy import fuzz
	return fuzz.ratio(val_1, val_2)




def time_comparison(time_1, time_2):
	time_1_original = time_1
	time_2_original = time_2
	if isinstance(time_1, float) and isinstance(time_2, float):
		if time_1_original*1000000>1:
			time_1_original=f"{round(time_1_original*1000000, 2)} µs"
		else:
			time_1_original=f"{round(time_1_original*1000000000)} ns"

		if time_2_original*1000000>1:
			time_2_original=f"{round(time_2_original*1000000, 2)} µs"
		else:
			time_2_original=f"{round(time_2_original*1000000000)} ns"

		# to nano seconds
		time_1 = time_1*1000000000
		time_2 = time_2*1000000000
	else:	
		def to_microseconds(time):
			if not time.endswith("µs"):
				return float(time.split()[0]) * 1000
			return float(time.split()[0])
		time_1 = to_microseconds(time_1)
		time_2 = to_microseconds(time_2)


	if time_1 > time_2:
		times_faster = time_1 / time_2
	else:
		times_faster = time_2 / time_1

	if time_1 == int(time_1):
		time_1 = int(time_1)
	if time_2 == int(time_2):
		time_2 = int(time_2)

	if time_1 > time_2:
		print(f"Time-2 ({time_2_original}) is {round(times_faster, 3)} times faster than time-1 ({time_1_original})")
	else:
		print(f"Time-1 ({time_1_original}) is {round(times_faster, 3)} times faster than time-2 ({time_2_original})")





def connect_to_my_db():
	import sqlite3
	conn = sqlite3.connect('/home/amir/github/Amir-personal/db.db')
	return conn




def all_possible_combinations(inputArray, order_matters=True, min_length=1, max_length=None):
	import itertools
	n = len(inputArray)
	lst = []

	if max_length is None:
		max_length = n
	
	if order_matters:
		for length in range(min_length, max_length + 1):
			for indices in itertools.permutations(range(n), length):
				inner_list = [inputArray[i] for i in indices]
				lst.append(inner_list)
	else:
		for length in range(min_length, max_length + 1):
			for r in range(length, min(max_length, n) + 1):
				for combination in itertools.combinations(inputArray, r):
					lst.append(list(combination))

	return lst






def is_computer_locked():
	import subprocess
	screensaver_active = subprocess.run(["gnome-screensaver-command", "-q"], capture_output=True, text=True).stdout
	if "is active" in screensaver_active:
		# print("Computer is locked (screensaver is active).")
		# exit(0)
		return True

	# Check if the X11 screen lock is active
	x11_screen_lock_active = subprocess.run(["xset", "-q"], capture_output=True, text=True).stdout
	if "Monitor is On" not in x11_screen_lock_active:
		# print("Computer is locked (X11 screen lock is active).")
		# exit(0)
		return True

	# print("Computer is not locked.")
	# exit(1)
	return False




def get_insert_query_from_df(df, dest_table: str):
	import re
	import clipboard

	insert = """
	INSERT INTO `{dest_table}` (
		""".format(dest_table=dest_table)

	columns_string = str(list(df.columns))[1:-1]
	columns_string = re.sub(r' ', '\n        ', columns_string)
	columns_string = re.sub(r'\'', '', columns_string)

	values_string = ''

	for row in df.itertuples(index=False,name=None):
		values_string += re.sub(r'nan', 'null', str(row))
		values_string += ',\n'
	result = insert + columns_string + ')\n     VALUES\n' + values_string[:-2] + ';'
	
	open("/tmp/INSERT_query.sql", 'w').write(result)
	
	clipboard.copy(result)
	
	print("\nThe INSERT query copied to the clipboard, and saved as '/tmp/INSERT_query.sql', you can paste it anywhere you want.\n")


def convert_time_to_appropiate_units(time, round_to=2):
	"""
	>>> convert_time_to_appropiate_units("23:22:01")
	'23.37 h'
	>>> convert_time_to_appropiate_units("00:00:01")
	'1 s'
	>>> convert_time_to_appropiate_units("23:59:59")
	'24 h'
	>>> convert_time_to_appropiate_units("00:00:00")
	'0 s'
	"""
	day=False
	if time.count(":") == 3:
		day = True
		d = int(time.split(":")[0])
		time = time[time.index(":")+1:]
	h,m,s = list(map(int, time.split(":")))
	assert 0 <= h < 24, f"Wrong time (hour) ({time})"
	assert 0 <= m < 60, f"Wrong time (minute) ({time})"
	assert 0 <= s < 60, f"Wrong time (second) ({time})"

	total_seconds = h*60*60 + m*60 + s
	total_minutes = h*60 + m + s/60
	total_hours = h + m/60 + s/60/60
	if day:
		total_hours += 24*d
		total_minutes += 24*d*60
		total_seconds += 24*d*60*60
	if total_seconds < 60:
		return f"{total_seconds} s"
	if total_minutes < 60:
		x = round(total_minutes, round_to)
		if x == int(x):
			x = int(x)
		return f"{x} m"
	if total_hours < 24:
		x = round(total_hours, round_to)
		if x == int(x):
			x = int(x)
		return f"{x} h"
	x = round(d, round_to)
	if x == int(x):
		x = int(x)
	return f"{x} d"

def convert_time_to_seconds(time, round_to=2):
	"""
	>>> convert_time_to_seconds("23:22:01")
	84121
	>>> convert_time_to_seconds("00:00:01")
	1
	>>> convert_time_to_seconds("23:59:59")
	86399
	>>> convert_time_to_seconds("00:00:00")
	0
	"""
	d=0
	if time.count(":") == 3:
		d = int(time.split(":")[0])
		time = time[time.index(":")+1:]
	h,m,s = list(map(int, time.split(":")))
	# assert 0 <= h < 24, f"Wrong time (hour) ({time})"
	# assert 0 <= m < 60, f"Wrong time (minute) ({time})"
	# assert 0 <= s < 60, f"Wrong time (second) ({time})"

	return  d*24*60*60 + h*60*60 + m*60 + s



def usd_to_pkr_rate():
	import requests
	import json
	def exchangeratesapi():
		x = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=3711e8823fb8576e76fc7943d1791d88&symbols=USD,PKR&format=1").text
		xx = json.loads(x)['rates']
		usd_to_pkr_rate_today = xx['PKR']/xx['USD']
		return usd_to_pkr_rate_today

	def currencyapi():
		import currencyapicom
		client = currencyapicom.Client('cur_live_GAmZiaaag2YIC5k53gD2vpBwnlgr3iasviYa0C5r')
		result = client.latest('USD',currencies=['PKR'])
		# result = 
		# {'meta': {'last_updated_at': '2023-07-23T23:59:59Z'},
		# 'data': {'PKR': {'code': 'PKR', 'value': 286.5697274993}}}
		return result['data']['PKR']['value']

	try:
		return exchangeratesapi()
	except:
		return currencyapi()
	


def open_url_in_selenium(url):
	from selenium import webdriver
	browser = webdriver.Firefox(executable_path = "geckodriver")
	browser.get(url)
	print('\n\n*******************\n>>> s = bs4.BeautifulSoup(browser.page_source, "lxml")\n\n>>>browser.close()\n*******************\n\n')
	# browser.close()
	return browser

def is_add_running(browser, substring='ytp-ad-skip-button-icon'):
	import bs4
	# return "Skip Ads" in bs4.BeautifulSoup(browser.page_source, "lxml").text
	return substring in str(bs4.BeautifulSoup(browser.page_source, "lxml"))


def get_current_mouse_position():
	import os
	print(*list(map(lambda x: x.replace(":", ": "), list(os.popen("xdotool getmouselocation"))[0].strip().split()[:2])), sep="\n")

def click_mouse(x,y):
	import os
	command = f"xdotool mousemove {x} {y} click 1"
	os.system(command)

def run_youtube(url="https://www.youtube.com/"):
	# from amir_analysis_functions import open_url_in_selenium, is_add_running
	import time
	import os
	browser = open_url_in_selenium(url)
	while True:
		time.sleep(1)
		if is_add_running(browser):
			print("True")
			click_mouse(x=1831, y=948)
		else:
			print("False")


def view_data_frame(df):
	from pandastable import Table
	from tkinter import Tk, Frame

	def set_mousewheel(widget, command):
		"""Activate / deactivate mousewheel scrolling when 
		cursor is over / not over the widget respectively."""
		widget.bind("<Enter>", lambda _: widget.bind_all('<MouseWheel>', command))
		widget.bind("<Leave>", lambda _: widget.unbind_all('<MouseWheel>'))

	root = Tk()
	root.geometry("1920x1600")
	frame  = Frame(root)
	set_mousewheel(frame, lambda e: frame.config(text=e.delta))
	frame.pack(anchor="center", fill="both", expand=True, side="left")
	table = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)
	table.show()
	root.mainloop()




def Type_casting(df_id):
	import pandas as pd
	import matplotlib.pyplot as plt
	import ctypes
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

	b = df.memory_usage(deep=True).sum()
	b_ = df.memory_usage(deep=True)

	type_casting(int, 'integer')
	type_casting(float, 'float')
	type_casting("O", 'category')

	a = df.memory_usage(deep=True).sum()
	a_ = df.memory_usage(deep=True)


	print(f"\n\nTotal Reduction: {round((1-a/b)*100, 2)} %\n")
	print(f"Before : {round(b    / 1024 ** 2, 2) } MB")
	print(f"After  : {round(a    / 1024 ** 2, 2) } MB")
	print(f"Reduced: {round((b-a)/ 1024 ** 2, 2) } MB")
	((a_ / b_).sort_values().reset_index(drop=True) // .1 * 10).plot(kind='hist',
																	 grid=True,
																	 figsize=(14,7));
	plt.xlabel("Reduction % ", size=14) #, color='red');
	plt.ylabel("Frequency"   , size=14) #, color='red');
	plt.title ("Reduction % plot", size=16, color='red')
	plt.show()



def seconds_to_hh_mm_ss(seconds):
	hours, remainder = divmod(seconds, 3600)
	minutes, seconds = divmod(remainder, 60)
	return f'{hours:02d}:{minutes:02d}:{seconds:02d}'



def plot_for_different_types(df, string=['bar'], numeric=['hist', 'box'], date=[]):

	numeric_cols = df.select_dtypes("number").columns.to_list()
	obj_cols = df.select_dtypes("O").columns.to_list()
	date_cols = df.select_dtypes("datetime").columns.to_list()
	
	def _box_plot(series, _ax):
		nonlocal e_int_cols
		if not 'box' in numeric:
			return
		sns.boxplot(x=series, ax=_ax, color='lightcoral')
		_ax.set_title('Box Plot')
		# _ax.set_xlabel('X-axis label')
		_ax.set_ylabel('Box Plot Values')
		e_int_cols += 1
	
	def _hist_plot(series, _ax):
		nonlocal e_int_cols
		if not 'hist' in numeric:
			return
		_ax.hist(df[col_name], bins=20, color='skyblue', edgecolor='black')
		_ax.set_title('Histogram')
		# _ax.set_xlabel('X-axis label')
		_ax.set_ylabel('Frequency')
		e_int_cols += 1
	
	e_int_cols = 0
	e_obj_cols = 0
	e_date_cols = 0
	
	if len(numeric) == 1:
		numeric.append(None)
	if len(string) == 1:
		string.append(None)
	
	for col_name in df.columns.to_list():
		if col_name in numeric_cols:
			if not len(numeric):
				continue
			fig, axes = plt.subplots(1, len(numeric), figsize=(12, 5))
			plt.suptitle(f'Distribution of {col_name}')
			_box_plot(df[col_name], _ax=axes[e_int_cols])
			_hist_plot(df[col_name], _ax=axes[e_int_cols])
	
			plt.tight_layout(rect=[0, 0, 1, 0.95])
			plt.show()
			e_int_cols = 0




def fetch_data_from_google_sheet(json_path, worksheet_id, scope):
	# import json
	# from google.oauth2 import service_account
	import pandas as pd
	import gspread
	from oauth2client.service_account import ServiceAccountCredentials

	# Add your service account credentials file
	creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)

	# Authorize the client
	client = gspread.authorize(creds)

	# # Open the Google Sheet by its title
	# spreadsheet = client.open("Sheet1")

	# Open the Google Sheet by its ID
	spreadsheet = client.open_by_key(worksheet_id)

	# Select the first sheet
	sheet = spreadsheet.sheet1

	# Get all values from the first sheet
	data = sheet.get_all_records()

	df = pd.DataFrame(data)

	return df


def fetch_last_break_was_before_value_from_time_logging_sheet(json_path, scope, worksheet_id):
	import gspread
	from oauth2client.service_account import ServiceAccountCredentials
	creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
	client = gspread.authorize(creds)
	spreadsheet = client.open_by_key(worksheet_id)
	sheet = spreadsheet.sheet1  # Use sheet1 or .worksheet('Sheet Name') for specific sheet
	cell_value = sheet.acell('J2').value
	return cell_value




def turing_google_comparative_analysis_work_for_current_week():
	import pandas as pd
	x = pd.to_datetime(
			pd.read_clipboard(header=None)[0]
		)
	x = (
		x
		.to_frame("Date")
		.assign(
			Day=x.dt.day_name()
		)
		.value_counts()
		.reset_index(
			name="Count"
		)
		.sort_values(
			by="Date"
		)
		.reset_index(
			drop=True
		)
	)
	print(x.to_markdown(index=False))
	print("\n"*5)
	x = (
		x
		.loc[
			x
			.Day.eq("Monday")
			.loc[lambda x: x==True]
			.index.max():
		]
	)

	x['Count_cumsum'] = x.Count.cumsum()
	x['Count_cummean'] = x.Count_cumsum/(x.reset_index(drop=True).index+1)

	print(x.to_markdown(index=False))
	


def number_to_column_name_in_excel_sheet(num):
	"""
	>>> number_to_column(1))
	A
	>>> number_to_column(26))
	Z
	>>> number_to_column(27))
	AA
	>>> number_to_column(52))
	AZ
	>>> number_to_column(53))
	BA
	"""
	column_name = ''
	while num > 0:
		num -= 1
		column_name = chr(num % 26 + 65) + column_name
		num //= 26
	return column_name

def generate_dataframe_code(df, variable_name="df"):
	all_values = [f"{variable_name} = pd.DataFrame({{"]
	df.columns = df.columns.astype(str)
	types = df.dtypes.astype(str)
	x = df.astype(str).to_dict(orient="list")
	for col_name, col_values in x.items():
		values = "\t'" + col_name + "': ["
		if types[col_name].startswith("int") or types[col_name].startswith("float"):
			values += ",".join(col_values) + "],"
		else:
			values += "'" + "', '".join(col_values) + "'],"
		
		all_values.append(values)
	all_values.append("})")
	print("\n".join(all_values))


def get_x_and_y_lims(ax):
	if "<module 'matplotlib.pyplot' from " in ax.__str__():
		ax = ax.gca() # 'ax' in 'ax.gc()' is actually 'plt'
	xlim = ax.get_xlim()
	ylim = ax.get_ylim()
	x_from = float(xlim[0])
	x_to = float(xlim[1])
	y_from = float(ylim[0])
	y_to = float(ylim[1])
	return [x_from, x_to, y_from, y_to]




def convert_jupyter_notebook_to_python_script(notebook_path):
	"""
	This function accepts a path of a jupyter notebook, and return a string representation of that notebook. 
	"""
	import nbformat
	from nbconvert import PythonExporter

	with open(notebook_path, "r", encoding="utf-8") as f:
		notebook = nbformat.read(f, as_version=4)
	exporter = PythonExporter()
	script, _ = exporter.from_notebook_node(notebook)
	return script


def cksum_python(file_path):
	import hashlib

	def calculate_checksum(file_path, algorithm="sha256"):
		hash_func = hashlib.new(algorithm)
		with open(file_path, "rb") as f:
			while chunk := f.read(4096):  # Read in chunks for efficiency
				hash_func.update(chunk)
		return hash_func.hexdigest()
	checksum = calculate_checksum(file_path, "sha256")  # You can also use 'md5', 'sha1', etc.
	return checksum



def time_since_last_update_of_a_file(file_path):
	import os
	import time
	modified_time = os.path.getmtime(file_path)
	current_time = time.time()
	time_diff = int(current_time - modified_time)
	days = time_diff // 86400
	hours = (time_diff % 86400) // 3600
	minutes = (time_diff % 3600) // 60
	seconds = time_diff % 60
	return f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}"


def get_image_hash(image_path, HASH_SIZE=6):
	from PIL import Image
	import imagehash
	with Image.open(image_path) as img:
		# img_hash = str(imagehash.average_hash(img))
		img_hash = str(imagehash.phash(img, hash_size=HASH_SIZE))
	return img_hash

def get_hashes_of_all_images_recursively_in_this_directory(directory):
	import os
	from PIL import Image
	import imagehash
	from collections import defaultdict
	import pickle
	import shutil

	hash_file_name = "/home/amir/.duplicates.pkl"
	error_file_name = "/home/amir/.duplicates_ERROR_files.pkl"
	pickle.dump([], open(hash_file_name, 'wb'))
	pickle.dump([], open(error_file_name, 'wb'))

	hashes = defaultdict(list)
	e=0
	error_files = []
	total_files_count = int(list(os.popen(f'find "{directory}" -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" | wc -l'))[0])
	en = 0
	for root, _, files in os.walk(directory):
		for file in files:
			en += 1
			perc = int(en / total_files_count * 100)
			if perc % 3 == 0:
				print(f">>> {perc}% scanning is completed ...")
			if file.lower().endswith(('.jpg', '.jpeg', '.png')):
				try:
					path = os.path.join(root, file)
					hashes[ get_image_hash(path) ].append(path)
					pickle.dump(hashes, open(hash_file_name, 'wb'))
				except Exception as error:
					error_files.append(file)
					pickle.dump(error_files, open(error_file_name, 'wb'))
					print(f"Error processing {file}: {error}")
				if e%50 == 0:
					print(f">Image# {e} with {len(hashes)} records saved in {hash_file_name}", sep=" | ")
				e += 1
	to_remove = []
	hashes = pickle.load(open("/home/amir/.duplicates.pkl", 'rb'))
	for hash_, files in hashes.items():
		if len(files) == 1:
			continue
		if not any(['___TO_MOVEEEEEEEEEEEEEEEEEEEEEE' in i for i in files]):
			continue

		files = [file for file in files if os.path.exists(file)]

		if len(files) < 2:
			continue

		command = ""
		mx = max([len(file) for file in files])
		for file in files:
			ff = file + (mx-len(file))*' '
			print(ff, os.path.getsize(file))
			command += f"eog -f '{file}'; "
		os.system(command)
		user_inp = input("File to remove: ")
		if not user_inp:
			continue
		f_to_remove = files[int(user_inp)]
		to_remove.append(f_to_remove)
		pickle.dump(to_remove, open("/home/amir/.duplicates_TO_REMOVE_3.pkl", 'wb'))
		print(f"Removing {f_to_remove}.. ")
		shutil.move(f_to_remove, '/home/amir/.local/share/Trash/files/')