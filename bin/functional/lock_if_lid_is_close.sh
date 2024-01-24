#!/usr/bin/bash
file_name=$(ls /proc/acpi/button/lid/*/state)
# file_name=$(ls /proc/acpi/button/lid/LID0/state)
# test -e "$file_name"
# if [[ $? -ne 0 ]]; then
#     file_name=/proc/acpi/button/lid/LID/state
#     test -e "$file_name"
#     if [[ $? -ne 0 ]]; then
#         echo -e "\nNeither of '/proc/acpi/button/lid/LID/state' or '/proc/acpi/button/lid/LID0/state' exist."
#         return 1
#     fi
# fi

while true; do
    if [ $(cat "$file_name" | awk '{print $2}') == "closed" ]; then
        # gnome-screensaver-command --lock
        xdg-screensaver lock
    fi
    sleep 1s
done