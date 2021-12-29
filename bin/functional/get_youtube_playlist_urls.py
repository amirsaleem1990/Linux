#!/usr/bin/python3

from get_soup_object_using_selenium import get_soup_object_using_selenium
import os
import sys

try:
	play_list_url = sys.argv[1]
	if not 'youtube' in play_list_url and (not 'playlis' in play_list_url):
		play_list_url = input("Enter playlist url: ")
except:
	play_list_url = input("Enter playlist url: ")


x = get_soup_object_using_selenium(play_list_url)
urls = ['https://www.youtube.com' + i.split("&list=")[0] for i in x[0] if str(i).startswith("/watch?v=")] 

file_name = "mp4_links.txt"
while os.path.exists(file_name):
	file_name = input(f"\nThe {file_name} is already exists, please enter another name: ")
open(file_name, 'w').write('\n'.join(urls))

print(f"Saved {len(urls)} Urls in {file_name}")