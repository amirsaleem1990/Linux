#! /bin/bash
# https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252

# Exercise_13 - Modify the script from the previous exercise. Make the “file_count” function accept a directory as an argument. Next, have the function display the name of the directory followed by a colon. Finally display the number of files to the screen on the next line. Call the function three times. First on the “/etc” directory, next on the “/var” directory and finally on the “/usr/bin” directory.


function file_count(){
	dirctory=$1
	echo $dirctory
	# files_count=$(ls $dirctory | wc -l)
	# echo files_count
	# echo "Count of files/folders in Working Directory: $files_count"
	# exit 0
}
file_count