#!/home/amir/.venv_base/bin/python3

from datetime import datetime
import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(requests.get("https://stackoverflow.com/users/8875846/amir-saleem").text, "lxml")
s = f"your StackOverFlow reputation is: {soup.find('div', {'class' : 'fs-body3 fc-dark'}).text}"
s_number = s.split()[-1]
current_time = str(datetime.now())
last = open("/home/amir/github/Amir-personal/StackOverFlow_reputaion_record.txt", "r").read().splitlines()[-1].split(",")[1]
last_number = last.split()[-1]
if s_number == last_number:
	print("\nNo increase in reputation, which is:", s_number, "\n")
	import sys
	sys.exit(0)
print("Now:  ", s)
print("Last: ", last)
open("/home/amir/github/Amir-personal/StackOverFlow_reputaion_record.txt", "a").write(current_time+","+s+"\n")
