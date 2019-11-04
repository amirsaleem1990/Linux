#! /bin/bash
# https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252

# Exercise_7 - Modify the previous script to that it accepts the file or directory name as an argument instead of prompting the user to enter it.


b=$(ls -l | grep -w $1)

first_char=${b:0:1} # get first character of long listing for our file/folder
if [[ $first_char == "" ]]
	then 
		echo "Sorry, file/folder not exist"
fi
# if [[ $first_char  == "-" ]]
# 	then
# 		echo "<$1> is regular file"
# elif [[ $first_char == "d" ]]
# 	then
# 		echo "<$1> is regular directory"

# else
# 	echo "<$1> is another type of file"
# fi

# echo ""
# echo $(ls -l | grep -w $1)