#!/usr/bin/bash

absolute_path_of_file="$1"
drive_path="$2"

echo "$absolute_path_of_file" "$drive_path"

if [[ -z "$absolute_path_of_file" ]] || [[ -z "$drive_path" ]]; then
	echo -e "\nPlease try again, and provide both absolute_path_of_file and drive_path\n"
	exit
fi

do_it(){
	echo 
	copied=false
	rclone copy "$1" "$2"
	if [[ $? -eq 0 ]]; then 
		copied=true
	fi
	try_number=1
	max_tries=5
	while [[ "$copied" == "false" ]]; do
	    if [[ $try_number -gt $max_tries ]]; then
	        echo "Failed to UPLOAD the file in $max_tries retries."
	        return 1
	    fi
	    echo "> Retry ($try_number) to get UPLOAD the <$file_name> ..."
		rclone copy "$1" "$2"
		if [[ $? -eq 0 ]]; then 
			copied=true
		fi
	    let "try_number+=1"
	done

	file_name=$(basename "$absolute_path_of_file")

	url=$(rclone link "$2/$file_name")

	try_number=1
	max_tries=5

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
	echo "$url"
}

do_it "$absolute_path_of_file" "$drive_path"