#! /bin/bash
# Exercise_4 - Write a shell script to check to see if the file </home/amir/save_script.sh>  exists. If it does exist, display </home/amir/save_script.sh exist>. 
# Next, check to see if you can write to the file. If you can, display <You have permissions to execute /home/amir/save_script.sh> .If you cannot, display <You do NOT have permissions to execute /home/amir/save_script.sh> 

FILE="/home/amir/save_script.sh"
if [ -e "$FILE" ] # space must after and before <[> and <]>, so this is wrong <if [-e "$FILE"]>
	then
		echo "$FILE exist"
fi

if [ -x "$FILE" ]
	then
		echo "You have permition to execute $FILE"
	else
		echo "You do Not have permissions to execute $FILE"
fi
