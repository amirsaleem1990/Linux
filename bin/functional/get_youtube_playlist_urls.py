#!/home/amir/.venv_base/bin/python3

print("\nDEPRETIATED\nUse /amir_bin/get_youtube_playlist_urls2.py instead\n")

# from get_soup_object_using_selenium import get_soup_object_using_selenium
# import os
# import sys

# try:
# 	play_list_url = sys.argv[1]
# 	if not 'youtube' in play_list_url and (not 'playlis' in play_list_url):
# 		play_list_url = input("Enter playlist url: ")
# except:
# 	if os.path.exists("LINK"):
# 		play_list_url = open("LINK", 'r').read().strip()
# 		can_we_user_LINK_url = input("We're going to use url in LINK, Do you want to proceed? [yes|no] ") == 'yes'
# 		if not can_we_user_LINK_url:
# 			play_list_url = input("Enter playlist url: ")
# 	else:	
# 		play_list_url = input("Enter playlist url: ")


# # x = get_soup_object_using_selenium(play_list_url)

# # urls = ['https://www.youtube.com' + i.split("&list=")[0] for i in x[0] if str(i).startswith("/watch?v=")] 

# # file_name = "/home/amir/.mp4_links.txt"
# # while os.path.exists(file_name):
# # 	file_name = input(f"\nThe {file_name} is already exists, please enter another name: ")
# # open(file_name, 'w').write('\n'.join(urls))

# # print(f"Saved {len(urls)} Urls in {file_name}")

# x = get_soup_object_using_selenium(play_list_url)
# # "https://www.youtube.com/playlist?list=PLWv9VM947MKi_7yJ0_FCfzTBXpQU-Qd3K"
# urls = ['https://www.youtube.com/' + i.split("&list=")[0] for i in x[0] if i.startswith("/watch?v=")]
# FILE_NAME = "/home/amir/.mp4_links.txt"

# while os.path.exists(FILE_NAME):
# 	FILE_NAME = input(f"\nThe {FILE_NAME} is already exists, please enter another name: ")
# open(FILE_NAME, 'w').write('\n'.join(urls))
# print(f"Saved {len(urls)} Urls in {FILE_NAME}")