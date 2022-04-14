#!/usr/bin/bash
if [[ -z $1 ]]; then
	:
else
	cd "$1"
fi
size=$(du -s -BM | cut -d'M' -f1)
while :; do
	current_size=$(du -s -BM | cut -d'M' -f1)
	echo -e "$(date +%T)\t$current_size MB\t$(echo $current_size-$size|bc -l) MB\t$(find . | wc -l)"
	size=$current_size
	sleep 10
done