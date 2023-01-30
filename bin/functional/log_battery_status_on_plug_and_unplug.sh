#!/usr/bin/bash
echo -e  "$(upower -d   | grep -E "energy:|voltage|energy-full:|energy-full-design:|energy-rate:|capacity:|TimeToEmpty:|time to full:|time to empty:|state|to\ full|percentage" | sort -u | sed 's/^    //g' | sed 's/:\ \{1,\}/,/g')\nDate,$(date +%D-%T)" | cut -d, -f2  | paste -sd "," >> /home/amir/github/Amir-personal/battery_status_on_plug_and_unplug.csv
