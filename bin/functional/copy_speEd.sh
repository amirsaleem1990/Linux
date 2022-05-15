#!/usr/bin/bash
if [[ -z $1 ]]; then
	sleep_secs=10
else
	sleep_secs=$1
fi
size=$(du -s -BM 2>/dev/null | cut -d'M' -f1)
while :; do
	current_size=$(du -s -BM 2>/dev/null | cut -d'M' -f1)
	echo -e "$(date +%T)\t$current_size MB\t$(echo $current_size-$size|bc -l) MB\t$(find . 2>/dev/null| wc -l)"
	size=$current_size
	sleep $sleep_secs
done