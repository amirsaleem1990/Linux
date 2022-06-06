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

# echo 'Speed|Total|Avg|Time|current_time|Downloaded' >  '/home/amir/.speed_hist.csv'
/usr/bin/rm '/home/amir/.speed_hist.csv' 2>/dev/null

plot() {
	echo '
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/home/amir/.speed_hist.csv", sep="|", index_col=None)
df.columns = ["Speed", "Total", "Avg", "Time", "current_time", "Downloaded"]
df.Speed = df.Speed.str.strip("Speed:").str.strip().str.strip("K").astype(float)
d,h,m,s = [i.zfill(2) for i in df.Time.iloc[-1].strip().split(":")]
df.set_index("current_time").Speed.plot(title=f"DD:HH:MM:SS\n  {d}:{h}:{m}:{s}")
plt.axhline(df.Speed.mean(), color="red");
plt.axhline(df.Speed.quantile(0.25), color="green");
plt.axhline(df.Speed.quantile(0.75), color="green");
plt.show()
' | python3
}

live_plot(){
echo '
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from collections import deque
import os

from matplotlib import style
style.use("fivethirtyeight")

def animate(i):
	if not os.path.exists("/home/amir/.speed_hist.csv"):
		return
	rows_count = len(open("/home/amir/.speed_hist.csv", "r").read().splitlines()) -1
	if  rows_count < 1:
		return
	
	# df = pd.read_csv("/home/amir/.speed_hist.csv", sep="|", index_col=None).iloc[-60:]

	last_n_rows = deque(open("/home/amir/.speed_hist.csv", "r"), 300 if rows_count > 300 else rows_count) # load only last 300 lines
	df = pd.read_csv(StringIO("".join(last_n_rows)), header=None, sep="|")
	df.columns = ["Speed", "Total", "Avg", "Time", "current_time", "Downloaded"]
	df.Speed = df.Speed.str.strip("Speed:").str.strip().str.strip("K").astype(float)
	d,h,m,s = [i.zfill(2) for i in df.Time.iloc[-1].strip().split(":")]
	ax1.clear()
	ax1.plot(df.current_time, df.Speed)#, title=f"DD:HH:MM:SS\n  {d}:{h}:{m}:{s}")
	ax1.axhline(df.Speed.mean(), color="red");
	ax1.axhline(df.Speed.quantile(0.25), color="green");
	ax1.axhline(df.Speed.quantile(0.75), color="green");
	plt.title(f"DD:HH:MM:SS\n  {d}:{h}:{m}:{s}")
	plt.xticks(rotation=90)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
' | python3
}

x=-1

ifstat 1s 1 | grep wlxd037459bf2ea
if [[ $? -eq 0 ]]; then
	wifi_chip=wlxd037459bf2ea
else
	wifi_chip=wlp3s0
fi

main () {
	let "n++"
	current=$(ifstat -i $wifi_chip 1s 1 | awk 'NR==3 {print $1}')
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

	current_time=$(date +%T)

	let "x++"
	if [[ $(( $x % 20 )) == 0 ]]; then
		x=0
		echo -e "--Speed--|--Total--|----Avg-----|----Time----|current_time|----Downloaded----" | grep --color=auto '\|current_time\|Speed\|Total\|Avg\|Time\|Downloaded\|-\||'
	fi
	echo -e "$current_ | $total_ | $avg_ | $time_ | $current_time   | $downloaded_size_mb_ M, $downloaded_size_gb_ G" | tee -a /home/amir/.speed_hist.csv
}

control_c() {
	plot
	exit
}

trap control_c SIGINT



(live_plot &)
while true ; do 
   main
   sleep $secs_to_sleep
done





