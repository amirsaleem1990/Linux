#! /bin/bash

# https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252

# Exercise_14 - Write the shell script that renames all files in the current directory that end in “.jpg” to begin with today’s date in the following format: YYYY-MM-DD. For example, if a picture of my cat was in the current directory and today was October 31,2016 it would change name from “mycat.jpg” to “2016–10–31-mycat.jpg”.

JPG=$(ls *.jpg)
if [[ JPG == "" ]]
	echo Sorry, There is no .jpg file
	exit 0
else
	for jpg in $JPG
		do
			current_date=$(date '+%y-%m-%d')
			new_name="$current_date-$JPG"
fi