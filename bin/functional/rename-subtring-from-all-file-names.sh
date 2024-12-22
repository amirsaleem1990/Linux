#/usr/bin/bash

IFS=$'\n'
RED="\033[0;31m"
NORMAL="\033[0m"


if [[ $1 == "" ]]; then
	echo -e "\nEnter substring needs to be replaced"
	read to_be_replaced
	echo -e "\nEnter substring needs to be replaced WITH"
	read to_be_replaced_with

fi

test -e /tmp/original_file_names_2
if [[ $? -eq 0 ]]; then
	/amir_bin/DEL /tmp/original_file_names_2
fi

test -e /tmp/file_names_2
if [[ $? -eq 0 ]]; then
	/amir_bin/DEL /tmp/file_names_2
fi

IFS=$'\n'

for file_name in $(ls -a); do
	original_file_name=$file_name
	file_name=$(echo "$file_name" | sed "s/$to_be_replaced/$to_be_replaced_with/g")
	if [[ "$original_file_name" != "$file_name" ]]; then
		echo -e "\n$original_file_name"
		echo -e "${RED}$file_name${NORMAL}"

		echo "$original_file_name" >> /tmp/original_file_names_2
		echo "$file_name" >> /tmp/file_names_2
	fi
done

test -e /tmp/original_file_names_2
if [[ $? -eq 1 ]]; then
	echo -e "\nNo file found\nAborting ....\n\n"
	exit
fi

echo -e "\n\nAre you need to proceed? [yes|no] "
read ans
if [[ $ans == "yes" ]]; then
	echo '
original_file_names = open("/tmp/original_file_names_2", "r").read().splitlines()
file_names = open("/tmp/file_names_2", "r").read().splitlines()
import os
errors = []
for original_file_name, file_name in zip(original_file_names, file_names):
	try:
		os.rename(original_file_name, file_name)
	except:
		errors.append([original_file_name, file_name])
if errors:
	print("\n"*3)
	print("Some files are not renamed, Here they are:")
	print(*errors, sep="\n")
' | /home/amir/.venv_base/bin/python3
fi
