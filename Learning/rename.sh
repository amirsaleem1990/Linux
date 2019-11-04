#! /bin/bash

# https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252

# Exercise_14 - Write the shell script that renames all files in the current directory that end in “.jpg” to begin with today’s date in the following format: YYYY-MM-DD. For example, if a picture of my cat was in the current directory and today was October 31,2016 it would change name from “mycat.jpg” to “2016–10–31-mycat.jpg”.

JPG=$(ls -1 *.jpg)
if [[ JPG == "" ]]
	then
		echo "Sorry, There is no .jpg file"
		exit 0
else
	current_date=$(date '+%y-%m-%d')
	for jpg in $JPG
		do
			new_name="$current_date-$JPG"
			# mv $jpg $new_name
			echo $new_name
		done
fi