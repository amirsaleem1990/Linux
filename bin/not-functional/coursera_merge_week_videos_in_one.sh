#!/usr/bin/bash
main_path=$(pwd)
for week in $(ls -d */); do 
	cd $week 
	echo 1 | /amir_bin/merge_join_mp4_videos
	cd "$main_path"
done
