#!/home/amir/.yt_dlp/bin/python3

import string
import multiprocessing.dummy
import subprocess
import os
import traceback
import sys
import yt_dlp
import click
import time

def download(url):
	time.sleep(0.1)
	if url[0] == "#":
		return
	if not is_best:
		print("\nDownloading the video in default resolution, for best resolution you can add the option --is_best\n")
	
	ydl_opts = {
		'outtmpl': '%(title)s-%(id)s.%(ext)s',
		'merge_output_format': 'mp4',
		'quiet': True,               # Suppresses all stdout output
		'no_warnings': True,         # Ignores warnings
		# 'verbose': False,
	}

	if is_best:
		ydl_opts['format'] = 'bestvideo+bestaudio/best'

	try:
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
		open("downloaded.txt", "a").write(url+"\n")
	except:
		e_ = traceback.format_exc()
		print("\n\nERROR --------------------------------------------------")
		print(f"url: {url}")
		print(e_)
		print("---------------------------------------------- Error END\n\n")
		open(error_file, 'a').write(f'---------------------------------\n\n\nUrl:{url}\n{e_}\n\n')


def pool_func(N_PARALLEL_PROCESSES):
	try:
		downloaded = open("downloaded.txt", "r").read().splitlines()
		urls_to_download = [i for i in urls_to_download if not i in downloaded]
	except:
		pass        
	p = multiprocessing.dummy.Pool(processes=N_PARALLEL_PROCESSES)
	return p

def exclude_func(urls_to_download):
	te_be_removed = []
	for key_word in exclude.split("|"):
		for url in urls_to_download:
			if key_word.lower().strip() in url:
				te_be_removed.append(url)
	return [i for i in urls_to_download if not i in te_be_removed]

def Exit():
	print(f"\n\nErrors saved as {error_file}\n\n")
	after=int(list(os.popen("du -s -BM | cut -dM -f1"))[0].strip())
	downloaded_size= after - before
	print (f"\n\n................... Downloaded {downloaded_size} MB ................\n\n")
	sys.exit(1)



def main_func(N_PARALLEL_PROCESSES):
	p = pool_func(N_PARALLEL_PROCESSES)
	try:
		p.map(download, urls_to_download)
	except KeyboardInterrupt:
		Exit()


def get_incompleted_videos_urls(urls_file_name):
	part_files = [i for i in os.listdir() if i.endswith(".part")]
	urls = open(urls_file_name, 'r').read().splitlines()
	ids = [i.split(".mp4")[0].split("-")[-1] for i in part_files]
	partial_downloaded_urls = [url for id_ in ids for url in urls if id_ in url]
	print(f"\n\n\n{len(partial_downloaded_urls)} partial downloades identified\n\n\n")
	return partial_downloaded_urls



def get_urls_to_download(exclude):
	global urls_file_name
	try:
		urls_to_download = [i for i in set(open("mp4_links.txt", "r").read().splitlines()) if i.strip()]
		urls_file_name = "mp4_links.txt"
	except:
		try:
			urls_file_name = sys.argv[1]
		except: 
			import readline
			readline.parse_and_bind("tab: complete")
			urls_file_name = input("file <mp4_links.txt> not found, please Enter your file name: ")
		urls_to_download = [i for i in set(open(urls_file_name, "r").read().splitlines()) if i.strip() and (not i.startswith("#"))]


	if exclude:
		urls_to_download = exclude_func(urls_to_download)
	
	return urls_to_download

def exclude_substrings():
	exclude_file = "/home/amir/github/Amir-personal/.exclude_download_bulk"
	get_input_from_user = False
	if os.path.exists(exclude_file):
		e = open(exclude_file, 'r').read().strip()
		if e:
			# user_inp = input("Do you need to exclude last stuff [yes|no]  (which is:\n" + e + "\n")
			user_inp = input("Do you need to exclude last stuff [yes (default) | no]  \n")
			if user_inp.lower().strip() in ['yes', '']:
				exclude = e
			else:
				get_input_from_user=True
		else:
			get_input_from_user= True
	else:
		get_input_from_user=True
	if get_input_from_user:
		exclude = input("Words to exclude (if multiple separate them by '|')  ")
		if exclude:
			open(exclude_file, 'w').write(exclude)
	return get_input_from_user, exclude




urls_file_name = ""

error_file = ".downloading_errors.txt"
if os.path.exists(error_file):
	os.remove(error_file)


get_input_from_user, exclude = exclude_substrings()

before=int(list(os.popen("du -s -BM | cut -dM -f1"))[0].strip())

is_best = True
ans = input("Do you need to download BEST quality videos? [yes (default) | no]: ").strip().lower()
if  ans == "no":
	is_best = False

keyword = input("Do you want a specific keyword to be considered for downloading? [Press Enter for no keyword] ").lower()
n=0
N_PARALLEL_PROCESSES = 16
while True:
	urls_to_download = get_urls_to_download(exclude)
	partial_completed_urls = get_incompleted_videos_urls(urls_file_name)

	if (not urls_to_download) and (not partial_completed_urls):
		break
	
	if partial_completed_urls:
		if len(urls_to_download) >= N_PARALLEL_PROCESSES:
			urls_to_download = partial_completed_urls
		else:
			partial_completed_urls = partial_completed_urls + urls_to_download[:N_PARALLEL_PROCESSES-len(partial_completed_urls)]

	if keyword:
		urls_to_download = [i for i in urls_to_download if keyword in i.lower()]

	main_func(N_PARALLEL_PROCESSES)

	n += 1
	if n > 20:
		break

	print(f"\n\n------------------------------------------------------------------\nAttempt #{n}\n")