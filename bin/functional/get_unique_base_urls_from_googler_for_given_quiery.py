#!/home/amir/.venv_base/bin/python3
import requests
import os
import sys
import pandas as pd
import random

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


f = open("/home/amir/_urlS__", 'r').read().splitlines()
os.remove("/home/amir/_urlS__")
f = [i.strip('"') for i in f]

# F = []
# for i in f:
# 	try:
# 		if requests.get(i).ok:
# 			F.append(i)
# 	except:
# 		pass
# f = F.copy()
# del F

df = pd.DataFrame({'orignal': f})
df['removed_http(s)'] = df.orignal.str.split("//").str[1]
df['base_url'] = df['removed_http(s)'].str.split("/").str[0]
df['base_url_with_http(s)'] = df.orignal.str.split("//").str[0] + "//" + df.base_url

name = "/home/amir/urls_" + str(random.randint(1,9999999999999)) + ".csv"
df.to_csv(name)
print("\n\ndf saved as <" + name + ">\n\n")
print(*list(set(df['base_url_with_http(s)'].to_list())), sep="\n")
