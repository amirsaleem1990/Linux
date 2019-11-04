#! /bin/bash
FILE = /home/amir/save_script.sh
if [-e $FILE]
	then
		echo "$FILE exist"
fi

if [-x $FILE]
	then
		echo "You have permition to execute $FILE"
	else
		echo "You do Not have permissions to execute $FILE"
fi
