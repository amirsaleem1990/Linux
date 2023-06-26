#!/usr/bin/python3

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




def connect_to_mysql_db(user, passw, host, database=None, port=3306):
	import sqlalchemy
	if database is None:
		conn = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{passw}@{host}?charset=utf8')
	else:
		conn = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{passw}@{host}/{database}?charset=utf8')
	conn = conn.connect()
	return conn



def fuzzy_matching(val_1: str, val_2: str):
	from fuzzywuzzy import fuzz
	return fuzz.ratio(val_1, val_2)




def time_comparison(time_1, time_2):
	time_1_original = time_1
	time_2_original = time_2
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
		print(f"Time-1 ({time_1_original}) is {round(times_faster, 3)} times faster than time-2 ({time_1_original})")
	else:
		print(f"Time-2 ({time_2_original}) is {round(times_faster, 3)} times faster than time-1 ({time_2_original})")