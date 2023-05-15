#!/usr/bin/python3
import pandas as pd
import os
import matplotlib.pyplot as plt
os.system("""
IFS=$'\n'
for serv in $(ps aux | awk '{print $11}' | tail -n +2 | sort | uniq | grep  -v '\[' | grep -v \( | rev | cut -d/ -f1 | rev | sort | uniq); do 
    # x=$(pmap $(pgrep "$serv") 2>/dev/null) 
    # if [[ $? -ne 0 ]]; then
    #   continue
    # fi
    # x=$(echo "$x" | grep total | awk '{sum += $2} END {print sum/1024}' 2>/dev/null)
    x=$(ps aux | grep "$serv" | awk '{print $6/1024}' | paste -sd+ | bc)
    echo "$serv : $x"
done > /tmp/ram_consumption
""")
df = pd.read_csv("/tmp/ram_consumption", sep=" : ", header=None)
df.columns = ["Service", "Consumption"]
df = df.sort_values("Consumption", ascending=False)


def function(val):
    if val > 1024:
        val = f"{round(val/1024, 2)} GB"
    elif (val > 1) and (val < 1024):
        val = f"{round(val, 2)} MB"
    elif val < 1:
        val = f"{round(val*1024, 2)} KB"
    if len(val.split()[0].split(".")[1]) == 1:
        x = list(val)
        x.insert(x.index(".")+2, "0")
        val = ''.join(x)
    return val
print(round(df.Consumption.sum()/1024, 2), "GB")
df.set_index("Service").iloc[:15].Consumption.sort_values().plot(kind='barh')
plt.xlabel("MB")
memory_consumed = list(os.popen("""echo "scale=2; $(free --mega -w | head -n2 | tail -n1 | awk '{ sum = $3 + $5; print sum }')/1024"|bc -l"""))[0].strip()
plt.title(f"RAM Consumption | {round(df.Consumption.sum()/1024, 2)} GB | `free` command: {memory_consumed} GB")
plt.grid(True)
plt.show()
df.Consumption = df.Consumption.apply(function)
df.reset_index(drop=True)
print(df.to_string(index=False))