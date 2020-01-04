#!/usr/bin/ipython3
from PIL import Image, ImageDraw, ImageFont 
import os
W, H = (2500,300)
im = Image.new('RGB', (W, H), color = (73, 109, 137))
fnt = ImageFont.truetype('/home/amir/.cache/torbrowser/download/tor-browser_en-US/Browser/fonts/Arimo-BoldItalic.ttf', 40)
draw = ImageDraw.Draw(im)
msg = list(os.popen("todo"))[2:4]
msg = "\n\nGoal: ".join([i[i.find(" : ")+3 : ].strip() for i in msg])
draw.text((0,0), "\n" + msg, font=fnt, fill=(255, 255, 0))
import datetime
date = str(datetime.datetime.now()).split()[0]
file_name = f'/home/amir/.local/share/Trash/files/todo_{date}.png'
im.save(file_name)
os.system(f"gopen {file_name}")