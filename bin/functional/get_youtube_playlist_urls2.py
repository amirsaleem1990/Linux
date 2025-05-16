#!/home/amir/.venv_youtube/bin/python3

import yt_dlp

def get_playlist_videos(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            playlist_info = ydl.extract_info(playlist_url, download=False)
            if 'entries' in playlist_info:
                print(f"Playlist: {playlist_info.get('title', 'Untitled Playlist')}")
                print(f"Total videos: {len(playlist_info['entries'])}\n")
                
                for idx, video in enumerate(playlist_info['entries'], start=1):
                    video_url = f"https://youtube.com/watch?v={video['id']}"
                    print(f"{idx}. {video['title']}")
                    print(f"   URL: {video_url}\n")
            else:
                print("No videos found in this playlist.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        playlist_url = sys.argv[1]
    else:
        playlist_url = input("Enter YouTube playlist URL: ")
    get_playlist_videos(playlist_url)