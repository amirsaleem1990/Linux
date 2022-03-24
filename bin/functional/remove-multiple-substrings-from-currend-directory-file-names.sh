#/usr/bin/bash

IFS=$'\n'
ans=$1
RED="\033[0;31m"
NORMAL="\033[0m"


if [[ $1 == "" ]]; then
	echo -e "\nEnter substring to remove, if many saperate them by | "
	read ans
fi

test -e /home/amir/.original_file_names
if [[ $? -eq 0 ]]; then
	/amir_bin/DEL /home/amir/.original_file_names
fi

test -e /home/amir/.file_names
if [[ $? -eq 0 ]]; then
	/amir_bin/DEL /home/amir/.file_names
fi

if [[ $(echo "$ans" | grep -o \| | wc -l) -gt 0 ]]; then
	IFS=$'\n'
	for file_name in $(ls); do
		original_file_name=$file_name
		IFS=$'|'
		for to_be_removed in $(echo "$ans"); do
			file_name=$(echo "$file_name" | sed "s/$to_be_removed//g")
		done
		if [[ "$original_file_name" != "$file_name" ]]; then

			echo -e "\n$original_file_name"
			echo -e "${RED}$file_name${NORMAL}"

			echo "$original_file_name" >> /home/amir/.original_file_names
			echo "$file_name" >> /home/amir/.file_names
		fi
	done
else
	IFS=$'\n'
	to_be_removed=$ans
	for file_name in $(ls); do
		original_file_name=$file_name
		file_name=$(echo "$file_name" | sed "s/$to_be_removed//g")
		if [[ "$original_file_name" != "$file_name" ]]; then

			echo -e "\n$original_file_name"
			echo -e "${RED}$file_name${NORMAL}"

			echo "$original_file_name" >> /home/amir/.original_file_names
			echo "$file_name" >> /home/amir/.file_names
		fi
	done
fi

test -e /home/amir/.original_file_names
if [[ $? -eq 1 ]]; then
	echo -e "\nNo file found\nAborting ....\n\n"
	exit
fi

echo -e "\n\nAre you need to proceed? [yes|no] "
read ans
if [[ $ans == "yes" ]]; then
	echo '
original_file_names = open("/home/amir/.original_file_names", "r").read().splitlines()
file_names = open("/home/amir/.file_names", "r").read().splitlines()
import os
for original_file_name, file_name in zip(original_file_names, file_names):
	os.rename(original_file_name, file_name)
' | python3
fi
