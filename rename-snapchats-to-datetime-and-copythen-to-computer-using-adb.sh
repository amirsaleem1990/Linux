# DO `adb shell` 


# THEN 

# in adb sheel do:

mkdir /sdcard/DCIM/Snapchat/Snap
cd /sdcard/DCIM/Snapchat
for i in *; do 
	extention_=$(echo "$i"  | cut -d. -f2)
	datetime_=$(stat -c %y "$i" | cut -d. -f1 | sed 's/\ \{1,\}/_/g' | sed 's/\:\{1,\}/-/g' | sed 's/-\{1,\}//g')
	datetime_="Snap/SnapChat_$datetime_.$extention_"
	cp -v "$i" "$datetime_"
done




# adb pull /sdcard/DCIM .
# First move DCIM/Snapchat/Snap to DCIM/, then Remove files in DCIM/Snapchart after making sure that every file there IS IN  DCIM/Snap 
