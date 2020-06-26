#!/bin/bash
echo "date,time,total,used,free,shared,buff/cache,available,swap_total,swap_used,swap_free"
a=`free -h | tail -2`
b=`echo  $a | cut -d" " -f 2-7,9-11 | sed 's/\ /,/g'`
c=`date  +%d-%B-%y`
d=`date  +%H:%M:%S`
ram_and_swap="$c,$d,$b"
echo  $ram_and_swap

echo -e "\n\n\nTotal,Used,Avail,Mounted"
echo "`diskfree  | tail -3 | cut -d " " -f5- | sed 's/\ /,/g' | sed  's/,\{2,\}/,/g'`"