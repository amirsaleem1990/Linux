#! /bin/bash
# https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252

# Exercise_6 - write a shell script that prompts the user for a name of a file or directory and reports if it is a regular file, a directory, or another type of file. Also perform an ls command against the file or directory with the long listing option.


read -p "Enter file/directory name: " name # get user input, and save it in <name>
echo "" # new line

b=$(ls -l | grep -w $name)

first_char=${b:0:1} # get first character of long listing for our file/folder

if [[ $first_char  == "-" ]]
	then
		echo "<$name> is regular file"
elif [[ $first_char == "d" ]]
	then
		echo "<$name> is regular directory"

else
	echo "<$name> is another type of file"
fi

echo ls -l $name