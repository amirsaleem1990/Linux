#!/usr/bin/bash
while true; do
    if [ $(cat /proc/acpi/button/lid/LID0/state | awk '{print $2}') == "closed" ]; then
        # gnome-screensaver-command --lock
        xdg-screensaver lock
    fi
    sleep 0.3s
done