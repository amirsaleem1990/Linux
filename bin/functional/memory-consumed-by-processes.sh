#!/usr/bin/bash
IFS=$'\n'
for serv in $(ps aux | awk '{print $11}' | tail -n +2 | sort | uniq | grep  -v '\[' | grep -v \( | rev | cut -d/ -f1 | rev | sort | uniq); do 
	# x=$(pmap $(pgrep "$serv") 2>/dev/null) 
	# if [[ $? -ne 0 ]]; then
	# 	continue
	# fi
	# x=$(echo "$x" | grep total | awk '{sum += $2} END {print sum/1024}' 2>/dev/null)
	x=$(ps aux | grep "$serv" | awk '{print $6/1024}' | paste -sd+ | bc)
	echo "$serv : $x"
done > /tmp/ram_consumption



cat /tmp/ram_consumption | sort -k2 -t\: -n | column -t -s\: