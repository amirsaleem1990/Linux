#!/bin/bash
echo -e "
####################################
# This script itereate over all files HERE and if the same named found THERE(which you specify soon)
####################################
"
function x(){ 
	IFS=$'\n'
	du -s $1 | sed 's/\t/,/g' | cut -d, -f1 ; 
	}

#from=/media/450GB/320GB/MultiMedia/audio/call\ recordings
echo -en "Enter $from full/relative path\n(eg:/media/450GB/320GB/MultiMedia/audio/call\ recordings)\n\t"
read from
m=0
IFS=$'\n'
for i in `ls`; do 
	here=`x $i`
	test -e  $from/$i
	if [[ $? != 0 ]]; then
		echo "FILE NOT FOUND:   $i"
		let m++
		continue
	fi
	there=`x $from/$i`
	if [[ $here != $there ]] ; then 
		let m++
		echo "DIFFRENT SIZE:   $i, Here:$here, There:$there"
	fi
done
if [[ $m == 0 ]]; then
	echo -e "\nAll files HERE exists in <$from> and the Sizes are same, so you can delete files HERE\n\n"
fi