#! /bin/bash
# https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252
# Exercise_15 - Write the script that renames files based on the file extension. Next,It should ask the user what prefix to prepend to the file name(s). By default, the prefix should be the current date in YYYY-MM-DD format. If the user simply press enter,the current date will be used. Otherwise,whatever the user entered will be used as the prefix. Next,it should display the original file name and new name of the file. Finally,it should rename the file.


read -p "Enter file extension (eg: png): " extension
read -p "Enter Directory name: " directory
cd $directory
files=$(ls -1 *.$extension)
