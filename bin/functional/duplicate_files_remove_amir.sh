#!/bin/bash

start=$(date +%s)
output_file="/tmp/file_metadata_report.txt"

# Clear previous output
> "$output_file"

read -e -p "Enter full path of <THERE>: " there
while [ ! -d "$there" ]; do
	read -e -p "Enter full path of <THERE> (a directory) : " there
done

# Process each file found by rdfind (or just all files in a directory)
find . "$there" -type f | while read -r file; do
    size=$(stat -c "%s" "$file")
    first_bytes=$(head -c 100 "$file" | xxd -p)  # First 100 bytes in hex
    last_bytes=$(tail -c 100 "$file" | xxd -p)   # Last 100 bytes in hex
    checksum=$(sha256sum "$file" | awk '{print $1}')  # SHA-256 checksum

    # Append to report
    echo "File: $file" >> "$output_file"
    echo "Size: $size bytes" >> "$output_file"
    echo "First 100 bytes (hex): $first_bytes" >> "$output_file"
    echo "Last 100 bytes (hex): $last_bytes" >> "$output_file"
    echo "SHA-256: $checksum" >> "$output_file"
    echo "-----" >> "$output_file"
done

echo "Report generated: $output_file"
end=$(date +%s)
time_consumed=$(echo "$end - $start" | bc -l)
echo $time_consumed

current_dateTime=$(date +%d-%m-%Y_%T)

python3 -c '
import sys

x = open("/tmp/file_metadata_report.txt", "r").read()
x = x.split("-----")
x = [i.strip() for i in x]
outer_lst = []
for chunk in x:    
    inner_lst = []
    for line in chunk.splitlines():
        if ("File:" in line) or ("Size:" in line) or ("First 100 bytes (hex):" in line) or ("Last 100 bytes (hex):" in line) or ("SHA-256:" in line):
            inner_lst.append(line[line.index(":")+1:].strip())
        else:
            inner_lst[-1] += line.strip()
    outer_lst.append(inner_lst)
import pandas as pd
df = pd.DataFrame(outer_lst, columns=["File", "Size", "First 100 bytes (hex)", "Last 100 bytes (hex)", "SHA-256"])
df.to_csv(f"/tmp/{sys.argv[2]}.txt", index=False)
print(df.head(1)) 
' -- "$current_dateTime"