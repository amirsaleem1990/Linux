#!/usr/bin/bash
second_path=$1
if [[ -z $1 ]]; then
	read -p "You should provide the socond path, (eg: ~/Downloads/HTML) " second_path
fi
IFS=$'\n'; find . -maxdepth 1 -type f  | cut -d/ -f2-10 > /tmp/t1
IFS=$'\n'; find $second_path -maxdepth 1 -type f  | rev | cut -d/ -f1| rev > /tmp/t2
cat /tmp/t{1,2} > /tmp/t3 
IFS=$'\n'
for i in $(cat /tmp/t3); do
	test -e "$i"
	here=$?
	test -e $second_path/"$i"
	there=$?
	if [[ $here -eq 0 ]]; then
		if [[ $there -eq 0 ]]; then
			echo "IN BOTH >>> $i"
		else
			echo "IN HERE ONLY >>> du -sh $i"
		fi
	else
		echo "IN THERE ONLY >>> du -sh $second_path/$i"
	fi 
done | sort -h | grep --color "\|HERE\|THERE\|BOTH" 