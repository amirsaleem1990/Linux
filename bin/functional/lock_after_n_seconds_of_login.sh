#!/usr/bin/bash

#/home/amir/.config/autostart/lock-screen-after-n-seconds-of-login.desktop

file_name=/home/amir/github/Amir-personal/lock-screen-after-n-seconds-of-login.txt
echo true > "$file_name"
sleep 10s

while true; do
    is_computer_screen_locked=$(/amir_bin/is_computer_screen_locked.py)    
    if [[ "$is_computer_screen_locked" == "true" ]] ; then 
        sleep 2
        echo true > "$file_name"
    else
        x=$(cat "$file_name")        
        if [[ "$x" == "true" ]] ; then 
            /usr/bin/xdg-screensaver lock
        fi
    fi
    sleep 5
done