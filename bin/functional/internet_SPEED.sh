#!/usr/bin/bash
total=0
n=0
start=$(date +%s)
size_before=$(du -sk | cut -d$'\t' -f1)
secs_to_sleep=$1
if [[ -z $secs_to_sleep ]]; then
	secs_to_sleep=0
fi
func() {
var_=$1
# echo -e "var:\t$var_"
lenght=${#var_}
# echo -e "lenght:\t$lenght"
provided_lenght=$2
if [[ $lenght == $provided_lenght ]]; then
echo $var_
else
add_zeros=$(echo $provided_lenght-$lenght-1|bc -l)
# echo -e "add_zeros:\t$add_zeros"
# echo $(echo -n  "print($add_zeros*'_')" | python3)$var_
for i in $(seq $add_zeros) ; do 
	echo -n ' '
done
echo $var_
echo
fi
}

echo 'Speed|Total|Avg|Time|Downloaded' >  '/home/amir/.speed_hist.csv'

plot() {
	echo '
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/home/amir/.speed_hist.csv", sep="|", index_col=None)
# df.columns = "Speed|Total|Avg|Time|Downloaded".split("|")
series = df.Speed.str.strip("Speed:").str.strip().str.strip("K").astype(float)
series.plot()
plt.axhline(series.mean(), color="red");
plt.axhline(series.quantile(0.25), color="green");
plt.axhline(series.quantile(0.75), color="green");
plt.show()
	' | python3
}
x=-1
main () {
	let "n++"
	current=$(ifstat -i wlp3s0 1s 1 | awk 'NR==3 {print $1}')
	current_=$(func $current 8)K

	total=$(echo $current + $total|bc)
	total_=$(echo "scale=2; $total/1024"|bc -l)
	total_=$(func $total_ 7)M

	avg=$(echo "scale=3; $total/$n"|bc -l)
	avg_=$(func $avg 10)K

	now_=$(date +%s)
	diff_=$(echo $now_-$start|bc)
	time_=$(eval "echo $(date -ud "@$diff_" +'$((%s/3600/24)):%H:%M:%S')")

	size_after=$(du -sk | cut -d$'\t' -f1)
	downloaded_size_mb=$(echo "scale=1; ($size_after-$size_before)/1024"|bc -l)
	downloaded_size_gb=$(echo "scale=3; $downloaded_size_mb/1024"|bc -l)

	downloaded_size_mb_=$(func $downloaded_size_mb 6)
	downloaded_size_gb_=$(func $downloaded_size_gb 6)
	let "x++"
	if [[ $(( $x % 20 )) == 0 ]]; then
		x=0
		echo -e "--Speed--|--Total--|----Avg-----|----Time----|----Downloaded----" | grep --color=auto '\|Speed\|Total\|Avg\|Time\|Downloaded\|-\||'
	fi
	echo -e "$current_ | $total_ | $avg_ | $time_ | $downloaded_size_mb_ M, $downloaded_size_gb_ G" | tee -a /home/amir/.speed_hist.csv
}

control_c() {
	plot
	exit
}

trap control_c SIGINT

while true ; do 
   main
   sleep $secs_to_sleep
done

