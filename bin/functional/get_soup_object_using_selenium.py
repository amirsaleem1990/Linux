#!/usr/bin/ipython3
import sys
url_passed = False
try:
	url = sys.argv[1]
	if url.startswith("http"):
		url_passed = True
except:
	pass

def get_soup_object_using_selenium(url, visual=False):
	from selenium import webdriver
	from bs4 import BeautifulSoup
	import re
	# url = input("Enter your url: ")
	# visusl = True if input("Visual or not? [y|n]") in ['y', 'Y'] else False

	if visual:
		browser = webdriver.Firefox(executable_path = "/home/amir/github/Daily_facebook/geckodriver")
	else:
		from selenium.webdriver.firefox.options import Options
		options = Options()
		options.add_argument("--headless")
		browser = webdriver.Firefox(executable_path = "/home/amir/github/Daily_facebook/geckodriver", options=options)
	print(">>> browser.get(url)")
	browser.get(url)
	print('>>> s = BeautifulSoup(browser.page_source, "lxml")')
	s = BeautifulSoup(browser.page_source, "lxml")
	browser.close()
	extrected_urls =  [i['href'] for i in s.find_all('a', href=re.compile(''))] +\
	[i['src'] for i in s.find_all('source', href=re.compile(''))]
	print("\nA tuple is returned, 1st vlues is urls, 2nd value is BeautifulSoup object\n")
	return (set(extrected_urls), s)



def get_all_links(url, pattern=""):
	from bs4 import BeautifulSoup
	import requests
	import re
	extrected_urls = []
	s = BeautifulSoup(requests.get(url).text, 'lxml')
	x2= s.find_all('a', href=re.compile(pattern))
	extrected_urls += [i['href'] for i in x2]

	x2= s.find_all('source', href=re.compile(pattern))
	extrected_urls += [i['src'] for i in x2]

	extrected_urls = list(set(extrected_urls))
	if url_passed:
		print(*extrected_urls, sep="\n")
	return extrected_urls


if url_passed:
	get_all_links(url)


def get_all_links_from_html_file(file_name):
	from bs4 import BeautifulSoup

	s = BeautifulSoup(open(file_name, 'r').read(), 'lxml')

	return [i['href'] for i in s.find_all('a', href=re.compile(''))] + \
	[i['src'] for i in s.find_all('source', href=re.compile(''))]