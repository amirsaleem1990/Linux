#!/usr/bin/bash


# Function to display help message
display_help() {
	echo -e "
Usage: $0 --path_1 PATH1 --path_2 PATH2 [OPTIONS]\n
This script requires two paths to be specified and performs some operations with them.\n
Mandatory arguments:\n
  --path_1 PATH1    First path to process\n
  --path_2 PATH2    Second path to process\n
Optional arguments:\n
  --help           Display this help message and exit\n
Example:\n
  $0 --path_1 /home/user/dir1 --path_2 /var/log\n
"
    exit 0
}

path_1=""
path_2=""

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --path_1) 
            path_1="$2"
            shift 
            ;;
        --path_2) 
            path_2="$2"
            shift 
            ;;
        --help) 
            display_help
            ;;
        *) 
            echo "Unknown parameter passed: $1"
            display_help
            exit 1
            ;;
    esac
    shift
done

# Check if mandatory arguments are provided
if [[ -z "$path_1" ]] || [[ -z "$path_2" ]]; then
    echo "Error: Both --path_1 and --path_2 are required arguments"
    display_help
    exit 1
fi

echo "Path 1: $path_1"
echo "Path 2: $path_2"

# Example operation: check if paths exist
if [[ ! -e "$path_1" ]]; then
    echo "$path_1 does not exist"
    exit 1
fi

if [[ ! -e "$path_2" ]]; then
    echo "$path_2 does not exist"
    exit 1
fi

>/tmp/kjk_files.txt
>/tmp/kjk_same_size_path1.txt
>/tmp/kjk_same_size_path2.txt
>/tmp/kjk_duplicated_files.txt

ls "$path_1" "$path_2" > /tmp/kjk_files.txt
cat /tmp/kjk_files.txt | sort | uniq -c | sed 's/^\ \{1,\}//g' | grep -v ^1\  | cut -d' ' -f2-50 > /tmp/kjk_duplicated_files.txt
echo -e "\nThere are $(cat /tmp/kjk_duplicated_files.txt | wc -l) duplicated files\n"

while IFS= read -r line; do
	echo -e "\n>>>>>>>> $line"
	size_path_1=$(du -sh $path_1/"$line" | cut -d$'\t' -f1)
	size_path_2=$(du -sh $path_2/"$line" | cut -d$'\t' -f1)
	if [[ $size_path_1 == $size_path_2 ]]; then
		COLOR=$GREEN
		echo "$path_1/$line" >> /tmp/kjk_same_size_path1.txt
		echo "$path_2/$line" >> /tmp/kjk_same_size_path2.txt
	else
		COLOR=$RED
	fi
	echo -e "${COLOR}
$(du -sh $path_1/"$line")
$(du -sh $path_2/"$line")
${NORMAL}"
done < '/tmp/kjk_duplicated_files.txt'


echo -e "-----------------------------------------------\n\nSame Files' size:"
echo -e "\n${GREEN}Path_1 $path_1${NORMAL}"
cat /tmp/kjk_same_size_path1.txt

echo -e "\n${GREEN}Path_2 $path_2${NORMAL}"
cat /tmp/kjk_same_size_path2.txt
echo -------------------------------------------