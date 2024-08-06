#!/bin/bash
qty=$(find . -empty | wc -l)
starting_qty=$qty

echo -e "$starting_qty empty files/folders"

n=0
while true; do
	if [[ $n > 10 ]]; then
		break
	fi
	let "n++"
	IFS=$'\n'
	empty_files_and_folders_count=$(find . -empty | wc -l)

	if [[ $empty_files_and_folders_count -eq 0 ]]; then
		exit
	elif [[ $empty_files_and_folders_count -eq 1 ]]; then
		if [[ $(find . -empty) == "." ]] ; then
			exit
		fi
	fi
	echo -e "\n\nEmpty Files/Folders list ......\n"
	IFS=$'\n'
	/amir_bin/dt $(find . -empty)
	echo -e "\nWe are going to remove above empty files/folders, do you agree? [yes|no]"
	read response
	if [[ $response == "yes" ]]; then
		/amir_bin/DEL -rf $(find . -empty)
	fi
	empty_files_and_folders_count=$(find . -empty | wc -l)
	echo -e "\n>>>>>>>>>>>>> $empty_files_and_folders_count empty files/folders still exist"
done

