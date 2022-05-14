#!/bin/bash
qty=$(find . -empty | wc -l)
starting_qty=$qty

echo -e "$starting_qty empty files/folders"

n=0
while [ $qty -gt 0 ]; do
	if [[ $n > 10 ]]; then
		break
	fi
	let "n++"
	IFS=$'\n'
	/amir_bin/DEL -rf $(find . -empty)
	qty=$(find . -empty | wc -l)
done

echo -e "$qty empty files/folders"
