#! /bin/bash
# https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252

# Exercise_12 - Write a shell script that consists of a function that displays the number of files in the present working directory. Name this function “file_count” and call it in your script. If you use variable in your function, remember to make it a local variable.

function file_count(){
	files_count=$(ls | wc)
	echo "Count of files in Working Directory: $files_count"
	exit 0
}
file_count