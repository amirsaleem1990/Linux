#!/usr/bin/bash
x=$(xdotool getmouselocation --shell | grep ^X= | cut -d= -f2)
y=$(xdotool getmouselocation --shell | grep ^Y= | cut -d= -f2)
xdotool mousemove 920 1050 click 1
# xdotool key Control_L+d
xdotool key 0xffe3+Control_L
sleep 0.5s
xdotool mousemove $x $y click 1
# if [[ -z $1 ]]; then
# 	# xdotool mousemove $x $y
# else
# fi
