#!/usr/bin/bash
cwd=$(pwd)
IFS=$'\n'
cd "$cwd"
there="$1"
if [[ -z "$1" ]]; then
	read -p "Enter second path: " there
fi
for i in $(ls -d */); do 
	cd "$i"
	echo -e "\n>>>>>>>> $i"
	remove_files_and_folders_that_are_here_and_there_FROM_HERE.sh "$there/$i"
	cd "$cwd"
done