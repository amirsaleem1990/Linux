#!/home/amir/.yt_dlp/bin/python3

import datetime
import yt_dlp
import click
import time

retry_number = 0

def download_with_ytdlp(url, is_best=False, playlist=False):
	global retry_number
	if not is_best:
		print("\nDownloading the video in default resolution, for best resolution you can add the option --is_best\n")
	
	ydl_opts = {
		'outtmpl': '%(title)s-%(id)s.%(ext)s',
		'merge_output_format': 'mp4'
	}

	if not playlist:
		ydl_opts['noplaylist'] = True
	if is_best:
		ydl_opts['format'] = 'bestvideo+bestaudio/best'
	try:
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
		print("Download completed successfully!")
	except Exception as e:
		retry_number += 1
		print(f"An error occurred: {e}")
		print(f"Retry #: {retry_number}")
		download_with_ytdlp(url, is_best=is_best, playlist=playlist)

@click.command()
@click.option('--url', required=True, type=str, help='Url of the video (required)')
@click.option('--is_best', is_flag=True, help='Download the best available resolution')
@click.option('--playlist', is_flag=True, help='Download the whole playlist')

def main(url, is_best, playlist):
	download_with_ytdlp(url, is_best=is_best, playlist=playlist)

if __name__ == "__main__":
	main()