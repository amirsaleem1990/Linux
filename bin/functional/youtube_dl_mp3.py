#!/home/amir/.yt_dlp/bin/python3

import yt_dlp
import os

def download_youtube_mp3(url, output_path='./'):
    """
    Download high quality MP3 audio from a YouTube video.
    
    Args:
        url (str): YouTube video URL
        output_path (str): Directory to save the MP3 file (default: current directory)
    """
    
    # Set options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Select the best quality audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',  # Highest quality MP3
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Output template
        'quiet': False,  # Show progress
        'no_warnings': False,  # Show warnings if any
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nDownload completed successfully!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    else: 
        video_url = input("Enter YouTube video URL: ")
    download_youtube_mp3(video_url)