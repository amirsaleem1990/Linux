#!/usr/bin/bash

# Function to display usage
usage() {
	echo "Usage: $0 --absolute_path_of_file <absolute_path_of_file> --drive_path <drive_path>"
	exit 1
}

# Parse options using `getopt`
OPTIONS=$(getopt -o "" --long absolute_path_of_file:,drive_path: -- "$@")
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
		--drive_path)
			drive_path="$2"
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
if [ -z "$absolute_path_of_file" ] || [ -z "$drive_path" ]; then
	echo "Error: Missing required arguments."
	usage
fi

file_name=$(basename "$absolute_path_of_file")

echo 
copied=false
rclone copy "$absolute_path_of_file" "$drive_path"
if [[ $? -eq 0 ]]; then 
	copied=true
fi
try_number=1
max_tries=5
while [[ "$copied" == "false" ]]; do
	if [[ $try_number -gt $max_tries ]]; then
		echo "Failed to UPLOAD the file in $max_tries retries."
		exit 1
	fi
	echo -e "> Retry ($try_number) to get UPLOAD the <$file_name> ...\n"
	rclone copy "$absolute_path_of_file" "$drive_path"
	if [[ $? -eq 0 ]]; then 
		copied=true
	fi
	let "try_number+=1"
done


try_number=1
max_tries=5
url=$(rclone link "$drive_path/$file_name")
while [[ -z "$url" ]]; do
	if [[ $try_number -gt $max_tries ]]; then
		echo "Failed to get the url link in $max_tries retries."
		break
	fi
	echo "> Retry ($try_number) to get a link for $file_name ..."
	url=$(rclone link "$drive_path/$file_name")
	let "try_number+=1"
done
url="$url&usp=drive_copy"
echo 
echo "$url"
