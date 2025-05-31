# !/usr/bin/bash

test -e /tmp/screen_shots_prefix
if [[ $? -eq 0 ]]; then
	read -p "Do you need to reuse the last prefix? [yes|no]: " ans
	if [[ $ans == "yes" ]]; then
		prefix=$(cat /tmp/screen_shots_prefix)
		echo $prefix > /tmp/screen_shots_prefix
	else
		read -p "Enter your prefix: " prefix
	fi
else
	read -p "Enter your prefix: " prefix
	echo $prefix > /tmp/screen_shots_prefix
fi



test -e /tmp/starting_x
if [[ $? -eq 0 ]]; then
	read -p "Do you need to reuse the last positions? [yes|no]: " ans
	if [[ $ans  == "yes" ]]; then
		starting_x=$(cat /tmp/starting_x)
		starting_y=$(cat /tmp/starting_y)
		ending_x=$(cat /tmp/ending_x)
		ending_y=$(cat /tmp/ending_y)
	fi
fi

if [[ -z $starting_x ]]; then
	read -p "Put the mouse cursor on starting x,y position, and then press any key "
	starting_x=$(xdotool getmouselocation --shell | grep X\=| sed 's/X\=//g')
	starting_y=$(xdotool getmouselocation --shell | grep Y\=| sed 's/Y\=//g')


	read -p "Put the mouse cursor on ending x,y position, and then press any key "
	ending_x=$(xdotool getmouselocation --shell | grep X\=| sed 's/X\=//g')
	ending_y=$(xdotool getmouselocation --shell | grep Y\=| sed 's/Y\=//g')
fi

echo $starting_x > /tmp/starting_x
echo $starting_y > /tmp/starting_y
echo $ending_x > /tmp/ending_x
echo $ending_y > /tmp/ending_y




while true; do
	currently_max_number=$(max $(ls *.png 2>/dev/null | cut -d- -f1 | xargs))
	if [[ $? -eq 0 ]] ; then
		next_number=$(echo "$currently_max_number + 1"|bc -l)
	else
		next_number=1
	fi
	read -p "Press any key to take the next screenshot: "
	/usr/bin/rm /tmp/tmp_screen_shot.png 2>/dev/null
	xdotool mousemove $starting_x $starting_y; (/amir_bin/screen_shot_selected_area &); sleep 2s; xdotool mousedown 1; xdotool mousemove $ending_x $ending_y; sleep 2s; xdotool mouseup 1; sleep 1s
	si /tmp/tmp_screen_shot
	feh "/tmp/tmp_screen_shot.png"
	echo -e "\nEnter file name: "
	read file_name
	if [[ $file_name != "" ]]; then
		new_file_name="$prefix"__"$next_number-$file_name".png
		mv /tmp/tmp_screen_shot.png "$new_file_name"
	fi
done
