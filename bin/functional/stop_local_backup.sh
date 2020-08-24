#!/bin/bash

t=`cat /home/amir/.Local_backup_permision`
if [[ $t == False ]]; then
	echo "Already Stoped before"
	exit 1
else
	echo -en  "Are you need to STOP local backup?\n[y|n]:  "
	read ans
	if [[ $ans != 'y' ]]; then
		exit 1
	fi
	echo False > /home/amir/.Local_backup_permision
	if [[ $? == 0 ]]; then
		echo "Local backup permision set to <FALSE>."
	fi
	echo 

	next_local_backup_time
fi