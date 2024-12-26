#!/bin/bash

SEC=$(( `date +%s` - `stat -c %Y "$1"` ))
# x=`eval "echo $(date -ud "@$SEC" +'$((%s/3600/24)) D,%H H,%M M,%S S')"`
x=`eval "echo $(date -ud "@$SEC" +'$((%s/3600/24)):%H:%M:%S')"`
if [[ $(echo $x | grep '^[0-9]\:' | wc -l) -gt 0 ]]; then
	x=0$x
fi
echo "$x"