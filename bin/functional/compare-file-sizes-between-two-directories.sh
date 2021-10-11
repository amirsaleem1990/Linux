#!/bin/bash
rm -f _m__
rm -f _diffrent_size_count__
rm -f _file_not_found_count__



echo -e "
#######################################################################################
# This script itereate over all files HERE and if the same named file found THERE,    #
# there is a comparison between the two.                                              #
#######################################################################################
"

while [ $# -gt 0 ]; do
  case "$1" in
    --there)
      from="$2"
      ;;
    -h|--help)
      echo -e "
  Usage:

  --there ............. path/to/be/compared
  --help  ............. help page
  "
      exit
      ;;
    *)
      echo -e "
    ***************************
    * Error: Invalid argument.*
    ***************************
      "
      exit 1
  esac
  shift
  shift
done

if [[ -z $from ]]; then
	echo -e "\n'there' perameter not passed\nAborting.....\n\n"
	exit
fi

function x(){ 
	IFS=$'\n'
	du -s $1 | sed 's/\t/,/g' | cut -d, -f1 ; 
	}

# from=/media/450GB/320GB/MultiMedia/audio/call\ recordings

# from=$1
# if [[ $from = "" ]]; then
# 	echo -en "Enter $from full/relative path\n(eg:/media/450GB/320GB/MultiMedia/audio/call\ recordings)\n\t"
# 	read -e from
# fi



m=0
diffrent_size_count=0
file_not_found_count=0
total_files_count=`ls|wc -l`
IFS=$'\n'
for i in `ls`; do 
	here=`x $i`
	test -e  $from/$i
	if [[ $? != 0 ]]; then
		echo "FILE NOT FOUND:   $i"
		let "m++"
		echo $m > _m__ # me is loop k end me nice pring k lye < | column -t -s,> laga raha hun, ji ki wajah sy $m ki value wo loop k bahir 0 kar deta h, is ko overcome karny k lye ye kya h

		let "file_not_found_count++"
		echo $file_not_found_count > _file_not_found_count__ # me is loop k end me nice pring k lye < | column -t -s,> laga raha hun, ji ki wajah sy $file_not_found_count ki value wo loop k bahir 0 kar deta h, is ko overcome karny k lye ye kya h

		continue
	fi
	there=`x $from/$i`
	if [[ $here != $there ]] ; then 
		let "m++"
		echo $m > _m__ # me is loop k end me nice pring k lye < | column -t -s,> laga raha hun, ji ki wajah sy $m ki value wo loop k bahir 0 kar deta h, is ko overcome karny k lye ye kya h

		let "diffrent_size_count++"
		echo $diffrent_size_count > _diffrent_size_count__ # me is loop k end me nice pring k lye < | column -t -s,> laga raha hun, ji ki wajah sy $diffrent_size_count ki value wo loop k bahir 0 kar deta h, is ko overcome karny k lye ye kya h

		echo "DIFFRENT SIZE :   $i, Here:$here, There:$there, Size similarity %: `echo "scale=5; $there/$here" | bc`"
	fi
done | column -t -s,
m=`cat _m__ 2>/dev/null`
_diffrent_size_count__=`cat _diffrent_size_count__ 2>/dev/null`
_file_not_found_count__=`cat _file_not_found_count__ 2>/dev/null`

if [[ $m == "" ]]; then
	m=0
fi

if [[ $_diffrent_size_count__ == "" ]]; then
	_diffrent_size_count__=0
fi


if [[ $_file_not_found_count__ == "" ]]; then
	_file_not_found_count__=0
fi

if [[ $m == 0 ]]; then
	echo -e "\nAll files HERE exists in <$from> and the Sizes are same, so you can delete files HERE\n\n"
fi

echo -e "\n********* COUNT *********"
echo "Total files (Here): $total_files_count"
echo "DIFFRENT files    : $_diffrent_size_count__"
echo "File not found    : $_file_not_found_count__"

rm -f _m__
rm -f _diffrent_size_count__
rm -f _file_not_found_count__