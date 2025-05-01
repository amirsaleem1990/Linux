
import yt_dlp
import sys


def download_with_ytdlp(url):
    output_path="/downloads"
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        retry_number += 1
        print(f"An error occurred: {e}")
        print(f"Retry #: {retry_number}")
        download_with_ytdlp(url)

if __name__ == "__main__":
    retry_number = 0
    if len(sys.argv) < 2:
        print("\nPlease specify the download link\nAborting...")
        sys.exit(1)
    
    download_with_ytdlp(sys.argv[1])