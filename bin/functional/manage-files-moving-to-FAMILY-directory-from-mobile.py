#!/home/amir/.venv_base/bin/python3
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter

def get_user_input(prompt_text):
    return prompt(prompt_text, completer=PathCompleter())


# source_dir = "/media/amir/Data_2/320GB/mobile/Ayesha/DCIM/Camera/"
# source_dir = "/home/amir/"
# dest_parent_dir = "/home/amir/Amir/Problem solving/LeetCode/"
import sys
if not sys.argv[1]:
	source_dir = get_user_input("Enter absolute path for source dir: ")
else:
	source_dir = sys.argv[1]
if not sys.argv[2]:
	dest_parent_dir = get_user_input("Enter absolute path for parent destination dir: ")
else:
	dest_parent_dir = sys.argv[2]

# source_dir = "/home/amir/Data_2/320GB/MultiMedia/PICS/Camera/________FAMILY/_________________MY FAMILY/_____TOOO_MOVEEEEEEEEEEEEEEE/"
# dest_parent_dir="/home/amir/Data_2/320GB/MultiMedia/PICS/Camera/________FAMILY/_________________MY FAMILY/"


# source_dir = "."
# dest_parent_dir="."




if not source_dir.endswith("/"):
	source_dir += "/"
if not dest_parent_dir.endswith("/"):
	dest_parent_dir += "/"
pickle_file = "/tmp/__labels__.pkl"

import os
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import NullLocator
import pickle
import shutil

user_inp = input("\n1- Label pictures\n2- Move to desired location")
if not user_inp in ["1", "2"]:
	raise Exception("Wrong input\nAborting.......\n")

if user_inp == "1":
	dirs = list(map(str.strip, os.popen(f"find '{dest_parent_dir}' -maxdepth 1 -type d")))
	dirs = [i.replace(dest_parent_dir, "") for i in dirs]
	dirs = sorted(dirs)
	dirs_dict = dict(zip(range(len(dirs)), dirs))

	labels = {}

	# Get the list of picture files in the directory
	picture_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
	picture_files = [i for i in picture_files if i.lower().endswith(".jpg") or i.lower().endswith(".jpeg") or i.lower().endswith(".png")]
	picture_files = sorted(picture_files)

	# Create a figure and axes for plotting
	fig, ax = plt.subplots(figsize=(8, 6))

	# Adjust the figure position for the right half of the screen
	# fig.canvas.manager.window.move(1000, 0)  # Move the window to the desired position on the screen

	valid_labels = list(map(str, range(len(dirs)))) + ["", "r"]

	for picture_file in picture_files:
		print()
		picture_path = os.path.join(source_dir, picture_file)
		
		# Open the picture using PIL
		try:
			image = Image.open(picture_path)
		except:
			continue
		# Display the image in the right half of the screen
		ax.imshow(image)
		ax.axis('off')  # Turn off the axes
		ax.xaxis.set_major_locator(NullLocator())
		ax.yaxis.set_major_locator(NullLocator())
		
		# Add a rectangle patch to indicate the right half of the screen
		rect = patches.Rectangle((0.5, 0), 0.5, 1, linewidth=1, edgecolor='black', facecolor='none')
		ax.add_patch(rect)
		
		ax.set_title(picture_file)

		# Update the figure display
		plt.draw()
		plt.pause(0.1)

		for k,v in dirs_dict.items():
			print("{:<2}".format(k),"-->", v)
		
		label = input("Enter a label for the picture: ")

		if label == "":
			continue

		elif label == "r":
			os.remove(source_dir + picture_file)
			print(f"The file '{source_dir}{picture_file}' have been removed..")
			continue
		
		while not label  in valid_labels:
			print("Invalid label")
			label = input("Enter a label for the picture: ")

		if label == "":
			continue

		# Add the label to the dictionary
		labels[picture_file] = (label, dirs[int(label)])
		print(f"Label: {label} | Dir: {dirs[int(label)]} | File: {picture_file}")
		pickle.dump(labels, open(pickle_file, 'wb'))
		
		# Clear the figure
		ax.cla()
		
	# Print the dictionary of picture labels
	print(labels)


if user_inp in ["1", "2"]:
	to_delete = []
	to_delete_differet_sizes = []
	dic = pickle.load(open(pickle_file, 'rb'))
	for file_name,v in dic.items():
		destination_dir = dest_parent_dir + v[1] + "/"
		destination_full_name = destination_dir + file_name
		source_file_with_full_path = source_dir + file_name
		if not os.path.exists(source_file_with_full_path):
			continue
		if os.path.exists(destination_full_name):
			source_size = os.path.getsize(source_file_with_full_path)
			destination_size = os.path.getsize(destination_full_name)
			if abs( source_size / destination_size ) > 0.98:
				to_delete.append([file_name, v[1], source_size, destination_size])
			else:
				print(
					"The file 'file_name' have different sizes in the source and destination\n"
					"Source Size     :", source_size, "\n"
					"Destination Size:", destination_size, "\n"
					"abs(source/dest):", round(abs(source_size/destination_size),3), "\n"
				)
				os.system(f"gopen '{destination_full_name}' '{source_file_with_full_path}'")
				inp = input("Do you need to remove the source file? [yes|no]: ")
				if inp == "yes":
					to_delete_differet_sizes.append(source_file_with_full_path)
			print(f"File already exists.. '{destination_full_name}', Here: {source_size}, There: {destination_size} | abs(Here/There): {abs(source_size / destination_size)}")
			continue
		source_file_with_full_path = source_dir + file_name
		shutil.move(source_file_with_full_path, destination_dir)

	if to_delete:
		print(
			"\n"
			"Source     : " + source_dir + "\n"
			"Dest Parent: " + dest_parent_dir + "\n"
			"\n"
		)
		import pandas as pd
		df = pd.DataFrame(to_delete, columns=['file_name', 'dir', 'source_size', 'destination_size']).assign(diff=lambda x: round(abs(x.source_size/x.destination_size),2)).sort_values("diff")
		print(df.to_string())

		inp = input("\nDo you want to remove the above? [yes|no]: ")
		if inp == "yes":
			for i in to_delete:
				os.remove(f"{source_dir}/{i[0]}")

	if to_delete_differet_sizes:
		for i in to_delete_differet_sizes:
			os.remove(i)