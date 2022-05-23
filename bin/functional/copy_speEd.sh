#!/usr/bin/bash
if [[ -z $1 ]]; then
	sleep_secs=10
else
	sleep_secs=$1
fi
size=$(du -s -BM 2>/dev/null | cut -d'M' -f1)

/usr/bin/rm -f /home/amir/.copyt_speed.txt
/usr/bin/rm -rf /tmp/multipage_pdf.pdf

main(){
	current_size=$(du -s -BM 2>/dev/null | cut -d'M' -f1)
	echo -e "$(date +%T)\t$current_size MB\t$(echo $current_size-$size|bc -l) MB\t$(find . 2>/dev/null| wc -l)" | tee -a /home/amir/.copyt_speed.txt
	size=$current_size
}

plot(){
echo '
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
def f(x):
	x = list(map(int, x.split(":")))
	return x[0]*60*60 + x[1]*60 + x[2]
df = pd.read_table("/home/amir/.copyt_speed.txt", names=["time", "total_size", "incremental_size", "files_count"])
waiting_time = int(df.time.iloc[:2].apply(f).diff().iloc[1])
df = (
	df
	.assign(
		incremental_size = df.incremental_size.str.replace(" MB", "").astype(int),
		total_size = df.total_size.str.replace(" MB", "").astype(int)
	)
	.where(lambda x:x.incremental_size>=0)
	.dropna()
	.set_index("time")
)
with PdfPages("/tmp/multipage_pdf.pdf") as pdf:
	for col in df.columns.to_list():
		(
			df
			[[col]]
			.plot(
				figsize=(20,7), 
				grid=True, 
				title=col,
				ylabel="MB"
			)
		)
		pdf.savefig()
		plt.close()
' | python3
}

control_c() {
	echo -e "\nSee /home/amir/.copyt_speed.txt\n"
	plot
	evince /tmp/multipage_pdf.pdf
	exit
}

trap control_c SIGINT

while true ; do 
   main
   sleep $sleep_secs
done