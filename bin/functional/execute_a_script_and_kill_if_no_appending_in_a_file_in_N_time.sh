#!/usr/bin/bash

while [ $# -gt 0 ]; do
	case "$1" in
		--sleep_time)
			sleep_time="$2"
			shift 2
			;;
		--executable_file_full_path)
			executable_file_full_path="$2"
			shift 2
			;;
		--file_to_append_full_path)
			file_to_append_full_path="$2"
			shift 2
			;;
		--stop_file_full_path)
			stop_file_full_path="$2"
			shift 2
			;;
		-h|--help)
			echo -e "
Usage:

--sleep_time ........................ sleep time (eg: 30s, 1m, etc).
--executable_file_full_path  ........ full path of the script you want to execute
--file_to_append_full_path .......... full path of the file the main script append the results to
--stop_file_full_path ............... this sceipt will be exited when <stop_file_full_path> will be found. So ${RED}$executable_file_full_path${NORMAL} will have to write this empty file when it needs to be stopped.
-h, --help  ............. help page
"
			exit 0
			;;
		*)
			echo "unknown option: $1"
			exit 1
			;;
		esac
done

echo 
if [ ! -f "$executable_file_full_path" ]; then
    echo -e "The file <$executable_file_full_path> ${RED}DOESN'T EXIST${NORMAL}\nAborting ...\n"
    exit 1
fi

if [ ! -x "$executable_file_full_path" ]; then
    echo -e "The file <$executable_file_full_path> is ${RED}NOT executable${NORMAL}\nAborting ...\n"
    exit 1
fi

if [ ! -f "$file_to_append_full_path" ]; then
	touch "$file_to_append_full_path"
else
	echo -e "\nThe append file <$file_to_append_full_path> exists, do anything you want with it, and then press Enter .. "
	read 
	if [ ! -f "$file_to_append_full_path" ]; then
		touch "$file_to_append_full_path"
	fi
fi



pid_file=$(echo "/tmp/$(tr -dc 'a-zA-Z' </dev/urandom | head -c 12)")

# stop_file="$pid_file_____STOP"
# while [ -f $stop_file ]; do
# 	pid_file=$(echo "/tmp/$(tr -dc 'a-zA-Z' </dev/urandom | head -c 12)")
# 	stop_file="$pid_file_____STOP"
# done

while [ -f "$stop_file_full_path" ]; do
	echo -e "The stop file $stop_file_full_path is already exist, which isn't supposed to\nKindly remove it and then press Enter ..."
	read
done


echo -e "\n\n\npid file: $pid_file\n\n\n"

iteration_num=0
while [ ! -f "$stop_file_full_path" ]; do
	let "iteration_num++"
	echo -e "\n\n\n>>> $(date +%T) -- Iteration# $iteration_num\n\n"
    "$executable_file_full_path" &
    echo $! > $pid_file
    before=$(wc -l < $file_to_append_full_path)
    while true; do
        sleep "$sleep_time"
        now=$(wc -l < $file_to_append_full_path)
        if [ "$now" -eq "$before" ]; then
            kill -9 "$(cat $pid_file)" 2>/dev/null
            break
        else
            before=$now
        fi
    done
done
