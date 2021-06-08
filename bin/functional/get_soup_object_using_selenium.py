#!/usr/bin/ipython3
def get_soup_object_using_selenium(url, visual=False, urls=True):
	from selenium import webdriver
	from bs4 import BeautifulSoup
	
	# url = input("Enter your url: ")
	# visusl = True if input("Visual or not? [y|n]") in ['y', 'Y'] else False

	if visual:
		browser = webdriver.Firefox(executable_path = "/home/amir/github/Daily_facebook/geckodriver")
	else:
		from selenium.webdriver.firefox.options import Options
		options = Options()
		options.add_argument("--headless")
		browser = webdriver.Firefox(executable_path = "/home/amir/github/Daily_facebook/geckodriver", options=options)

	browser.get(url)
	s = BeautifulSoup(browser.page_source, "lxml")
	extrected_urls = []
	if urls:
		for i in s.select("a"):
			try:
				l = i['href']
				extrected_urls.append(l)
			except:
				pass
		for i in s.select("source"):
			try:
				l = i['src']
				extrected_urls.append(l)
			except:
				pass
		print("\nA tuple is returned, 1st vlues is urls, 2nd value is BeautifulSoup object\n")
	return (set(extrected_urls), s)



def get_all_links(url, pattern=""):
	from bs4 import BeautifulSoup
	import requests
	import re
	
	s = BeautifulSoup(requests.get(url).text, 'lxml')
	x2= s.find_all('a', href=re.compile(pattern))
	x2 = [i['href'] for i in x2]
	se = []
	for i in x2:
		if not i in se:
			se.append(i)
	return se
