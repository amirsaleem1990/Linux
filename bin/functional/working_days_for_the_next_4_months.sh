#!/usr/bin/bash
workdays_in_month() {
  local M_Y="$1"
  # Reformat MM-YYYY to YYYY-MM-01 for the start date
  local DATE=$(echo "$M_Y" | awk -F'-' '{print $2"-"$1"-01"}') 
  # Get the target month number for loop termination
  local END_MONTH=$(echo "$M_Y" | awk -F'-' '{print $1}')
  local COUNT=0
  
  # Loop while the month of the current date matches the input month
  while [ "$(date -d "$DATE" +"%m")" = "$END_MONTH" ]; do
    # Get the day of the week: %u (1=Mon, ..., 5=Fri, 6=Sat, 7=Sun)
    if [ "$(date -d "$DATE" +"%u")" -le 5 ]; then
      COUNT=$((COUNT + 1))
    fi
    # Advance to the next day
    DATE=$(date -d "$DATE + 1 day" +"%Y-%m-%d")
  done
  
  echo "$COUNT"
}

next_month(){
	next_=$(date -d "$(echo "$1" | awk -F'-' '{print $2"-"$1"-01"}') + 1 month" +"%m-%Y")
	echo "$next_"
}

format_month_year(){
	result=$(date -d "$(echo "$1" | awk -F'-' '{print $2"-"$1"-01"}')" +"%b %Y")
	echo "$result"
}
current_month_year=$(date +%m-%Y)
N_MONTHS=4
total_weekdays=0
for i in $(seq 1 $N_MONTHS); do
	formatted_month_year=$(format_month_year $current_month_year)
	weekdays_count=$(workdays_in_month $current_month_year)
	echo -e "$formatted_month_year\t$weekdays_count"
	let "total_weekdays+=weekdays_count"
	current_month_year=$(next_month $current_month_year)
done
echo -en "Average weekdays in the upcomming $N_MONTHS months (including the current one): "
echo "scale=1; $total_weekdays/$N_MONTHS"|bc -l
