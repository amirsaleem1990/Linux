#! /bin/bash
# https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252
# Exercise_15 - Write the script that renames files based on the file extension. Next,It should ask the user what prefix to prepend to the file name(s). By default, the prefix should be the current date in YYYY-MM-DD format. If the user simply press enter,the current date will be used. Otherwise,whatever the user entered will be used as the prefix. Next,it should display the original file name and new name of the file. Finally,it should rename the file.


read -p "Enter Directory name (default is Current directory): " directory
cd $directory

echo "You have these extensions in this directory"
for f in *.*; do printf "%s\n" "${f##*.}"; done | sort -u

read -p "Enter file extension (eg: png) : " extension

read -p "Enter prefix (default is current date) : " prefix 
if [[ prefix == "" ]]
	prefix=$(date +%F)
fi


files=$(ls -1 *.$extension)

if [[ $? != 0 ]]
then
	echo -e "\nSorry, No file with .$extension extension"
	exit 0
else
	for file in $files; do
		new_name=$file-$prefix
		echo "Renaming $file to $new_name"
		mv $file $new_name
	done
fi