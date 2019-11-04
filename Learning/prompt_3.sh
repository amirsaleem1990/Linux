#! /bin/bash

# https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252
# Exercise_8 - Modify the previous script to accept an unlimited number of files and directories as arguments.

files=$@
for file in $files
	do 
		b=$(ls -l | grep -w $file)

		first_char=${b:0:1} # get first character of long listing for our file/folder
		if [[ $first_char == "" ]]
			then 
				echo "Sorry, file/folder not exist"

		else
			if [[ $first_char  == "-" ]]
				then
					echo "<$file> is regular file"
			elif [[ $first_char == "d" ]]
				then
					echo "<$file> is regular directory"

			else
				echo "<$file> is another type of file"
			fi
		fi
			
		echo $(ls -l | grep -w $file)