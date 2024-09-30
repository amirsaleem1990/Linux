#/usr/bin/bash

#/home/amir/.config/autostart/lock-screen-after-n-seconds-of-login.desktop


file_name=/home/amir/github/Amir-personal/lock-screen-after-n-seconds-of-login.txt
echo true > "$file_name"

while true; do
    computer_screen_locked=$(is_computer_screen_locked)
    if [ $x == true ] ; then 
        echo true > "$file_name"
    else:
        x=$(cat "$file_name")
        if [ $x == true ] ; then 
            /usr/bin/xdg-screensaver lock
        fi
    fi
    sleep 10s
done
