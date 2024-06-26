#! /bin/bash

# https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252

# Exercise_11 - Write a script that executes the command “cat /etc/shadow”. If the command return a 0 exit status, report “command succeeded” and exit with a 0 exit status. If the command returns a non-zero exit status, report “Command failed” and exit with a 1 exit status.

retrn=$(cat /etc/shadow) # assinged to variable, so even if command is succeeded, there is no return on screen

if [[ $? == 0 ]]
	then
		echo "command succeeded"
		exit 0
else
	echo "command failed"
	exit 1
fi