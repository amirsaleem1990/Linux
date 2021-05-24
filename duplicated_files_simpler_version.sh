#!/usr/bin/bash
IFS=$'\n'
for i in `find . -type f | sed 's/^\.\///g' | rev | cut -d/ -f1 | rev | sort | uniq -c |sort -n | sed 's/^\ \{1,\}//g' | grep -v ^1 | cut -d' ' -f2`; do
	qty=`find . -name $i | wc -l`
	echo -e "<<<<<<<<<<<<< $i >>>>>>>>>>>>>"
	echo "Qty.: $qty"
	IFS=$'\n'
	unique_sizes=`du -sh $(find . -name $i)| sort -n | sed 's/\t/,/g' | cut -d, -f1 | sort -u | wc -l`
	if [[ $unique_sizes -eq 1 ]]; then
		echo "Note: All files ARE same size"     | grep --color=auto "\|ARE\|Note"
	else
		echo "Note: NOT All files are same size" | grep --color=auto "\|NOT\|Note"
	fi
	for q in `find . -name $i`; do
		echo "`du -sh $q | sort -n`"
	done
done