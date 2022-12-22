#!/home/amir/github/virtual_envs/fake_data/bin/python3
from faker import Faker
import numpy as np
import pandas as pd
import os
import sys

class my_fake_ganerator:
	def __init__(self, n_rows, int_=False, float_=False, detetime_=False, string_=False, other_=False, lang = 'en_US', seed=4321, adjust=35):
		print("""
Example:
	self = my_fake_ganerator(
		n_rows=10, 
		int_=True, 
		float_=True,
		string_=True,
		other_=True,
		detetime_=True
		).main()
	df = self.df
			""")
		# if not any([int_,float_,detetime_,string_,other_]):
			# raise Exception("\nYon can pass atleast on of the arguments from [int_,float_,detetime_,string_,other_]\n")
		self.n_rows = n_rows
		self.seed = seed
		self.lang = lang
		self.int_ = int_
		self.float_ = float_
		self.detetime_ = detetime_
		self.string_ = string_
		self.other_ = other_

		Faker.seed(self.seed)
		self.fake = Faker(self.lang)
		self.adjust = adjust

		self.data = {}

		self.int_list = [
			"random_digit",
			"random_digit_not_null",
			"random_digit_not_null_or_empty",
			"random_int",
			"random_number",
			"year",
		]

		self.float_list = [
			"latitude",
			"longitude",
			"pricetag"
		]

		self.datetime_list = [
			"future_date",
			"future_datetime",
			"time",
			"time_object",
			"date",
			"date_between_dates",
			"date_time",
			"date_time_between_dates",
			"past_datetime"
		]


		self.string_list = [
			"random_element",
			"random_letter",
			"timezone",
			"word",
			"address",
			"ascii_free_email",
			"century",
			"city",
			"color_name",
			"company",
			"country",
			"day_of_week",
			"first_name_female",
			"first_name_male",
			"month_name",
			"password",
			"prefix_female",
			"prefix_male"
		]


		self.other_list = [
			"random_elements",
			"random_letters",
			"rgb_color",
			"words",
			"color",
			"coordinate",
			"hex_color",
			"latlng",
			"phone_number"
		]

	def do(self, lst, key_name):
		for i in lst:
			com = f"self.fake.{i}()"
			self.data[key_name] = self.data.get(key_name, []) + [{i : [eval(com) for _ in range(self.n_rows)]}]

	def write_to_disk(self):
		orig_name = "/home/amir/fake_data"
		name = orig_name
		n = 1
		while os.path.exists(name + ".csv"):
			name = f"{orig_name}_{n}"
			n += 1
		self.df.to_csv(name+".csv", index=False)
		print(f"\n\nYou fake data saved as {name+'.csv'}\n")


	def main(self):
		if self.int_:
			self.do(self.int_list, "int_")
		if self.float_:
			self.do(self.float_list, "float_")
		if self.other_:
			self.do(self.other_list, "other_")
		if self.detetime_:
			self.do(self.datetime_list, "datetime_")
		if self.string_:
			self.do(self.string_list, "string_")

		lst = []
		for k,v in self.data.items():
			lst.append(pd.DataFrame([(x,y) for i in v for x,y in i.items()]).assign(type=k))
		df = pd.concat(lst)
		df.columns = ["method", "values", "type"]
		self.df = pd.concat([df.drop("values", axis=1), pd.DataFrame(df['values'].tolist(), df.index)],axis=1).set_index("method").drop("type", axis=1).T#.reset_index(drop=True)
		self.df.columns.name = None
		self.write_to_disk()


if __name__ == "__main__":
	if len(sys.argv) == 1:
		n_rows = 10
		print("\n\bSince you haven't passed the number for n_rows perameter, we are going to use the default '10'.\n\n")
	else:
		n_rows = sys.argv[1]
		try:
			n_rows = int(n_rows)
		except:
			raise Execption("Wrong input. The input should be integer value")

	self = my_fake_ganerator(
		n_rows=n_rows, 
		int_=True, 
		float_=True,
		string_=True,
		other_=True,
		detetime_=True
		)
	self.main()