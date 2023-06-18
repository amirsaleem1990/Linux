#!/home/virtual_envs/time_table_venv/bin/ipython3
import pandas as pd
import numpy as np
import datetime
import subprocess
import os
# import dataframe_image as dfi
import sys

# HTML_FILE_NAME = "/home/amir/.office_time_table.html"
HTML_FILE_NAME = "/home/amir/.office_time_table.html"
PNG_FILE_NAME = "/home/amir/.office_time_table.png"


if len(sys.argv) == 2:
    START = sys.argv[1]
else:
    START = "08:30"

def add_first_two_row_in_actual_dataframe(df):
    """
    For batter readability for human when reading png file 
    """

    df = df.reset_index().rename(columns={"index" : ''})
    df2 = pd.DataFrame(df.columns.to_list()).T
    df2.columns = df.columns
    df = pd.concat([df2, df]).reset_index(drop=True)
    df.columns = list(range(df.shape[1]))

    return df


def time_to_minutes(x):
    h,m = x.lstrip("0").split(":")
    h = int(h)
    if m.startswith("0"):
        m = m[1]
    m = int(m)
    return h * 60 + m

def minutes_to_time(x):
    h = str(int(x//60))
    m = str(int(x%60))
    if len(h) == 1:
        h = "0" + h
    if len(m) == 1:
        m = "0" + m
    return f"{h}:{m}"
        
def add(time, hours):
    return minutes_to_time(time_to_minutes(time) + int(hours*60))

def f(row):
    if row.iloc[0] != todays_day_name:
        return ['']*len(row)
    return ['background-color: red' if i else '' for i in condition.to_list()]


def creating_a_dataframe():
    subjects = ["English", "ML", "SQL", "Math", "Python"]
    x = [(START, add(START, 0.5))]
    for _ in range(len(subjects)-1): 
        x.append(
            (x[-1][-1], 
             add(x[-1][-1], 0.5)
            )
        )
    columns = [f"{i[0]} - {i[1]}" for i in x]
    arrays = [columns, subjects]
    columns = pd.MultiIndex.from_arrays(arrays, names=('Time', 'Subject'))
    df = (
        pd
        .DataFrame(np
        .array((["Learaning", "Practice"]*13)[:25])
        .reshape(5,5), index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], columns = columns)
    )
    return df


color_maping_dict = {
    "Learaning": "green",
    "Practice": "blue",
}

df = creating_a_dataframe()

c = (
    pd
    .DataFrame(
        pd.DataFrame(df
                     .columns
                     .to_list()
                    )
        [0]
        .str
        .replace(" ", "")
        .str
        .split("-")
        .apply(
            lambda x: (time_to_minutes(x[0]), time_to_minutes(x[1]))
        )
        .to_list(), 
        columns=["start", "end"]
    )
)
c.index = df.index

todays_day_name = datetime.datetime.now().strftime("%A")

t = datetime.datetime.now()
cm = t.hour * 60 + t.minute

# todays_day_name = "Friday"
# cm = 601


df = add_first_two_row_in_actual_dataframe(df)
condition = ((c.start <= cm) & (c.end >= cm))
condition = pd.concat([pd.Series([None],), condition]).fillna(False)

df = df.style.applymap(lambda val: "background: " + color_maping_dict.get(val, 'orange')).apply(f, axis=1)

html = df.render()

# import imgkit
# # https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
# options = {
#     'zoom' : .5,
#     'quality' : 100,
#     'width' : 3,
#     # 'T': '0.75in', # margin-top
#     # 'R': '0.75in', # margin-right
#     # 'B': '0.75in', # margin-bottom
#     # 'L': '0.75in', # margin-left
#     # 'no-outline': None
# }
# imgkit.from_string(html, PNG_FILE_NAME, options = options)
# os.system(f"feh -F {PNG_FILE_NAME}")

# df.to_html(HTML_FILE_NAME)
# os.system(f"gopen {HTML_FILE_NAME}")



# dfi.export(
#     styled_df,
#     PNG_FILE_NAME
# )

open(HTML_FILE_NAME, 'w').write(html)
subprocess.call(
    f'wkhtmltoimage -f png  --zoom 1 --disable-smart-width --minimum-font-size 30 --width 1270 --height 360 {HTML_FILE_NAME} {PNG_FILE_NAME}; feh -F {PNG_FILE_NAME}', shell=True
    ) # wkhtmltoimage 0.12.6

