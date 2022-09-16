#!/usr/bin/bash
for i in $(cat  /home/amir/github/Amir-personal/urls_to_open_right_after_login.txt); do 
    firefox $i
done
