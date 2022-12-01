# #!/usr/bin/python3

# import os
# import sys
# from get_soup_object_using_selenium import get_soup_object_using_selenium

# try:
# 	channel_url = sys.argv[1]
# 	if not 'youtube' in channel_url:
# 		channel_url = input("Enter channel url: ")
# except:
# 	channel_url = input("Enter channel url: ")
# x = get_soup_object_using_selenium(channel_url)
# urls = ['https://www.youtube.com'+i for i in x[0] if i.startswith("/watch?v=")]

# file_name = "mp4_links.txt"
# while os.path.exists(file_name):
# 	file_name = input(f"\nThe {file_name} is already exists, please enter another name: ")
# open(file_name, 'w').write("\n".join(urls))
# print(f"Saved {len(urls)} urls in {file_name}")


