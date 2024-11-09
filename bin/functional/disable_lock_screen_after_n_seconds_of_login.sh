#!/usr/bin/bash
x=$(cat /home/amir/github/Amir-personal/lock-screen-after-n-seconds-of-login.txt)
if [[ "$x" == "true" ]]; then
	echo false > /home/amir/github/Amir-personal/lock-screen-after-n-seconds-of-login.txt
	notify-send -u critical -t 5000 "Important Alert" "____________DDDDDDDD____________"
fi