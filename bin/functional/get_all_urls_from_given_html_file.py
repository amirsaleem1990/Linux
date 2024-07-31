#!/usr/bin/python3
import sys
from bs4 import BeautifulSoup
import re

if len(sys.argv) != 2:
	raise Exception("No HTML file path provided .....\nExiting ....\n")

html_file_name = sys.argv[1]

def get_all_links(soup_object, pattern=""):
	extrected_urls = []
	x2= soup_object.find_all('a', href=re.compile(pattern))
	extrected_urls += [i['href'] for i in x2]

	x2= soup_object.find_all('source', href=re.compile(pattern))
	extrected_urls += [i['src'] for i in x2]

	extrected_urls = list(set(extrected_urls))

	return extrected_urls

soup_object = BeautifulSoup(open(html_file_name, 'r').read(), 'lxml')
all_links = get_all_links(soup_object)
print("\n")
print(*sorted(all_links), sep="\n")
print("\n")