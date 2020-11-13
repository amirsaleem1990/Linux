#!/bin/bash
echo -e "
####################################
# This script itereate over all files HERE and if the same named found THERE(which you specify soon)
####################################
"
function x(){ 
	du -sh $1 | sed 's/\t/,/g' | cut -d, -f1 ; 
	}

#from=/media/450GB/320GB/MultiMedia/audio/call\ recordings
echo -en "Enter $from full/relative path\n(eg:/media/450GB/320GB/MultiMedia/audio/call\ recordings)\n\t"
read from

for i in `ls`; do 
	here=`x $i`
	test -e  $from/$i
	if [[ $? != 0 ]]; then
		echo "FILE NOT FOUND:   $i"
		continue
	fi
	there=`x $from/$i`
	if [[ $here != $there ]] ; then 
		echo "DIFFRENT SIZE:   $i, Here:$here, There:$there"
	fi
done