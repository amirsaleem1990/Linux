#!/usr/bin/python3
import os
import sys
try:
	_, n, search_query = sys.argv
	n = int(n)
except:
	pass
if len(sys.argv) < 3:
	n=input("Enter n links (default is 10): ")
	if n == "":
		n = 10
	else:
		n = int(n)
	search_query = input("Enter search query: ")
com=f"""googler -n{n} --json  '{search_query}' | grep http | sed 's/    "url": //g' > /home/amir/_urlS__"""
os.system(com)


import pandas as pd
f = open("/home/amir/_urlS__", 'r').read().splitlines()
os.remove("/home/amir/_urlS__")
f = [i.strip('"') for i in f]
df = pd.DataFrame({'orignal': f})
df['removed_http(s)'] = df.orignal.str.split("//").str[1]
df['base_url'] = df['removed_http(s)'].str.split("/").str[0]
df['base_url_with_http(s)'] = df.orignal.str.split("//").str[0] + "//" + df.base_url

import random
name = "/home/amir/urls_" + str(random.randint(1,9999999999999)) + ".csv"
df.to_csv(name)
print("\n\ndf saved as <" + name + ">\n\n")
print(*list(set(df['base_url_with_http(s)'].to_list())), sep="\n")
