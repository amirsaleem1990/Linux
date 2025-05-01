#!/home/amir/.yt_dlp/bin/python3

import string
import multiprocessing.dummy
import subprocess
import os
import traceback
import sys
import yt_dlp
import click

def download(url):
	if url[0] == "#":
		return
	if not is_best:
		print("\nDownloading the video in default resolution, for best resolution you can add the option --is_best\n")
	
	ydl_opts = {
		'outtmpl': '%(title)s-%(id)s.%(ext)s',
		'merge_output_format': 'mp4'
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


def pool_func():
	try:
		downloaded = open("downloaded.txt", "r").read().splitlines()
		urls_to_download = [i for i in urls_to_download if not i in downloaded]
	except:
		pass        
	p = multiprocessing.dummy.Pool()
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


def main_func():
	p = pool_func()
	try:
		p.map(download, urls_to_download)
	except KeyboardInterrupt:
		Exit()


def get_incompleted_videos_urls(urls_file_name):
	# # u = list(map(str.strip, list(os.popen("ls | grep .mp4.part$ | sed 's/.mp4.part//g' | rev | cut -d- -f1 | rev"))))
	# part_files = [i.lower().split(".")[0] for i in os.listdir() if i.endswith("part")]
	# urls = open(urls_file_name, 'r').read().splitlines()
	# r = []
	# for pf in part_files:
	#     for url in urls:
	#         if pf.lower() in url:
	#             r.append(url)
	part_files = [i.lower().split(".")[0].split("-")[0].strip() for i in os.listdir() if i.endswith(".part")]
	urls = open(urls_file_name, 'r').read().splitlines()
	urls_copy = []
	for url in urls:
		urls_copy.append("".join([c for c in url.split("/", urls[0].count("/"))[-1] if c in string.ascii_letters + string.digits]))

	part_files_copy = []
	for pf in part_files:
		part_files_copy.append("".join([c for c in pf if c in string.ascii_letters + string.digits]))

	partial_downloaded_urls = []
	for pf in part_files_copy:
		for e_url, url in enumerate(urls_copy):
			if (pf.lower() in url) and (not url in partial_downloaded_urls) and (abs(len(pf)/len(url))<0.06):
				partial_downloaded_urls.append(urls[e_url])
	partial_downloaded_urls = list(set(partial_downloaded_urls))
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


urls_file_name = ""

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


error_file = ".downloading_errors.txt"
if os.path.exists(error_file):
	os.remove(error_file)


before=int(list(os.popen("du -s -BM | cut -dM -f1"))[0].strip())


is_best = False
ans = input("Do you need to download BEST quality videos? [yes | no (default)]: ").strip().lower()
if  ans == "yes":
	is_best = True

urls_to_download = get_urls_to_download(exclude)


x = get_incompleted_videos_urls(urls_file_name)
if x:
	urls_to_download = x

keyword = input("Do you want a specific keyword to be considered for downloading? [Press Enter for no keyword] ").lower()
if keyword:
	urls_to_download = [i for i in urls_to_download if keyword in i.lower()]

main_func()

n=0
while True:
	part_files = [i for i in os.listdir() if i.endswith(".part")]
	if not part_files:
		Exit()
	# urls_to_download = [i for i in set(open(urls_file_name, "r").read().splitlines()) if i.strip() and (not i.startswith("#"))]
	# part_files_str = ' '.join(part_files)
	# part_files = [i for i in urls_to_download if i.split("/")[-1].replace("watch?v=", '') in part_files_str]
	# if not part_files:
	#   Exit()  
	# urls_to_download = part_files
	# if exclude:
		# urls_to_download = exclude_func()

	x = get_incompleted_videos_urls(urls_file_name)
	if x:
		urls_to_download = x
	else:
		urls_to_download = get_urls_to_download(exclude)

	if n > 5:
		urls_to_download = get_urls_to_download(exclude)

	print("\n\n------------------------------------------------------------------\nAnother attempt\n")
	main_func()
	n += 1
	if n > 20:
		break
