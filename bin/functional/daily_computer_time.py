#!/usr/bin/python3

import amir_analysis_functions
import datetime

def daily_computer_time(DELAY_MINUTES):
	conn = amir_analysis_functions.connect_to_my_db()
	cursor = conn.cursor()
	today = str(datetime.date.today())
	current_time = str(datetime.datetime.now().time()).split(".")[0]
	#cursor.execute("PRAGMA journal_mode=wal")
	cursor.execute(
		"INSERT INTO daily_computer_use_duration (date, delay_minutes, is_computer_locked, current_time) VALUES (?, ?, ?, ?)", 
		(today, DELAY_MINUTES, int(amir_analysis_functions.is_computer_locked()), current_time)
		)
	conn.commit()
	conn.close()


DELAY_MINUTES=3
while True:
	daily_computer_time(DELAY_MINUTES)
	time.sleep(DELAY_MINUTES)
