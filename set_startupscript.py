name_and_command = {'diry' : 'bash /home/amir/github/Amir-personal/diry/bash-script.sh', 
'Expenses': 'firefox --new-tab https://docs.google.com/spreadsheets/d/1ynsGnyXW7EfYWiOUz0IBUMJqY8BD82gR-ieMzcsYS48/edit#gid=1046897338', 
'github-automatic-push' :'bash /home/amir/github/Amir-personal/github-automatic-push-loop.sh', 
'LFD mail' : 'https://mail.google.com/mail/u/1/',
'terminal' : 'gnome-terminal'}


import os
import sys
home = os.environ["HOME"]

for name, command in name_and_command.items():
	launcher = ["[Desktop Entry]", "Name=", "Exec=", "Type=Application", "X-GNOME-Autostart-enabled=true"]
	dr = home+"/.config/autostart/"
	if not os.path.exists(dr):
	    os.makedirs(dr)
	file = dr+name.lower()+".desktop"

	if not os.path.exists(file):
	    with open(file, "wt") as out:     
	        for l in launcher:
	            l = l+name if l == "Name=" else l
	            l = l+command if l == "Exec=" else l
	            out.write(l+"\n")
	else:
	    print("file exists, choose another name")