#!/usr/bin/bash

# Function to display usage
usage() {
	echo "Usage: $0 --absolute_path_of_file <absolute_path_of_file> --target_directory <target_directory> --task_number <task_number> --batch <batch>"
	exit 1
}

# Parse options using `getopt`
OPTIONS=$(getopt -o "" --long absolute_path_of_file:,target_directory:,task_number:,batch: -- "$@")
if [ $? -ne 0 ]; then
	usage
fi

# Reorganize the arguments
eval set -- "$OPTIONS"

# Extract options
while true; do
	case "$1" in
		--absolute_path_of_file)
			absolute_path_of_file="$2"
			shift 2
			;;
		--target_directory)
			target_directory="$2"
			shift 2
			;;
		--task_number)
			task_number="$2"
			shift 2
			;;
		--batch)
			batch="$2"
			shift 2
			;;
		--)
			shift
			break
			;;
		*)
			usage
			;;
	esac
done

# Check if all options are provided
if [ -z "$absolute_path_of_file" ] || [ -z "$target_directory" ] || [ -z "$task_number" ] || [ -z "$batch" ]; then
	echo "Error: Missing required arguments."
	usage
fi

# # Script logic
# echo "File path: $absolute_path_of_file"
# echo "Target directory: $target_directory"
# echo "Task number: $task_number"
# echo "Batch: $batch"
# echo "Google Drive base path: $gdrive_base_path"

validate_input() {
	if [[ -z $1 ]]; then
		echo -e "\nInput not provided for $2\nExiting....\n"
		exit 1
	fi
}

validate_file() {
	if [[ ! -e $1 ]]; then
		echo -e "\nFile not found: $1\nExiting....\n"
		exit 1
	fi
}

make_a_gdrive_path() {
	directory_name=$1
	validate_input "$directory_name" "directory_name"
	echo "$gdrive_base_path $batch/$directory_name"
}

gdrive_base_path='am_data:[Turing]:Multimodality Delivery/Batch'
validate_file "$absolute_path_of_file"
drive_path=$(make_a_gdrive_path "$target_directory")
echo -e "> Copying <$absolute_path_of_file> to <$target_directory> ..."
echo -e "\nLast Modified before:\n\nDD:HH:MM:SS"
last_modified_before.sh "$absolute_path_of_file"

push_to_g_drive_script.sh --absolute_path_of_file "$absolute_path_of_file" --drive_path "$drive_path"

# output=$(push_to_g_drive_script.sh --absolute_path_of_file "$absolute_path_of_file" --drive_path "$drive_path")
# if [[ $? -ne 0 ]]; then
# 	echo -e "The file <$absolute_path_of_file> <$drive_path> is failed to be UPLOADED, upload it manually and press any key "
# 	read 
# fi
# link=$(echo "$output" | grep 'http')
# echo -e "$link\n"
# echo -e "\n$target_directory:\t$link" >> /tmp/urls_$task_number.txt