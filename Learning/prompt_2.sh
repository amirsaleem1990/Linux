#! /bin/bash
# https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252

# Exercise_7 - Modify the previous script to that it accepts the file or directory name as an argument instead of prompting the user to enter it.


b=$(ls -l | grep -w $@)

first_char=${b:0:1} # get first character of long listing for our file/folder

if [[ $first_char  == "-" ]]
	then
		echo "<$@> is regular file"
elif [[ $first_char == "d" ]]
	then
		echo "<$@> is regular directory"

else
	echo "<$@> is another type of file"
fi

echo ""
ls -l $@