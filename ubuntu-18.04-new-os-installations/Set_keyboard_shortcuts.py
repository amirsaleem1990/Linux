#!/usr/bin/python3

# Copied from:
    # https://itectec.com/ubuntu/ubuntu-how-to-set-custom-keyboard-shortcuts-from-terminal/

import subprocess
import sys
import os

def func(name, command, key_combination):
    # defining keys & strings to be used
    key = "org.gnome.settings-daemon.plugins.media-keys custom-keybindings"
    subkey1 = key.replace(" ", ".")[:-1]+":"
    item_s = "/"+key.replace(" ", "/").replace(".", "/")+"/"
    firstname = "custom"
    # get the current list of custom shortcuts
    get = lambda cmd: subprocess.check_output(["/bin/bash", "-c", cmd]).decode("utf-8")
    array_str = get("gsettings get "+key)
    # in case the array was empty, remove the annotation hints
    command_result = array_str.lstrip("@as")
    current = eval(command_result)
    # make sure the additional keybinding mention is no duplicate
    n = 1
    while True:
        new = item_s+firstname+str(n)+"/"
        if new in current:
            n = n+1
        else:
            break
    # add the new keybinding to the list
    current.append(new)
    # create the shortcut, set the name, command and shortcut key
    cmd0 = 'gsettings set '+key+' "'+str(current)+'"'
    cmd1 = 'gsettings set '+subkey1+new+" name '"+name+"'"
    cmd2 = 'gsettings set '+subkey1+new+" command '"+command+"'"
    cmd3 = 'gsettings set '+subkey1+new+" binding '"+key_combination+"'"

    for cmd in [cmd0, cmd1, cmd2, cmd3]:
        # print(cmd)
        subprocess.call(["/bin/bash", "-c", cmd])


os.system("""gsettings set org.gnome.settings-daemon.plugins.media-keys terminal "['<Alt>t']" """)
os.system("""gsettings set org.gnome.settings-daemon.plugins.media-keys home "['<Super>e']" """)
os.system("""gsettings set org.gnome.settings-daemon.plugins.media-keys www "['<Super>w']" """)



lst = [
['system monitor',            'gnome-system-monitor',                '<Alt>p'              ], # ALT + p 
['pinta',                     'pinta',                               '<Super>bracketright' ], # Super + ]
['screen_shot_selected_area', '/amir_bin/screen_shot_selected_area', '<Alt>a'              ], # ALT + a
['screen_shot_full_window',   '/amir_bin/screen_shot_full_window',   '<Alt>s'              ], # ALT + s
['touch_on_off',              '/amir_bin/touch_on_off',              '<Primary><Shift>F9'  ], # SHFT + CTRL + F9
['Paste',                     '/home/amir/Paste',                    '<Control>1'          ], # CTRL + 1
['Mn',                        '/usr/bin/xdotool key space',          '<Shift><Control>m'   ], # SHIFT + CTRL + m
['Night_light_modify shiny',  '/amir_bin/Night_light_modify +' ,     '<Primary><Alt>equal' ], # CTRL + ALT + =
['Night_light_modify dark',   '/amir_bin/Night_light_modify -' ,     '<Primary><Alt>minus' ], # CTRL + ATL + -
['night_light',               '/amir_bin/night_light',               '<Control><Alt>n'     ], # CTRL + ALT + n
['namaz',                     '/amir_bin/namaz',                     '<Shift><Control>n'   ], # SHIFT + CTRL + n
['align_pandas_code',         '/amir_bin/align_pandas_code',         '<Alt>e'              ]  # ALT + e
['vs_code_click_in_terminal', '/amir_bin/vs_code_click_in_terminal.sh', ''                 ],
['vs_code_click_in_terminal_back_click', '/amir_bin/vs_code_click_in_terminal.sh 1', ''    ],
['screen_shot_all_screens',   '/amir_bin/screen_shot_all_screens',   '<Control><Alt>a'     ],
]

for i in lst:
    func(*i)

#python3 this_script.py '<name>' '<command>' '<key_combination>'
#python3 this_script.py 'open gedit' 'gedit' '<Alt>7'

#Super key:                 <Super>
#Control key:               <Primary> or <Control>
#Alt key:                   <Alt>
#Shift key:                 <Shift>
#numbers:                   1 (just the number)
#Spacebar:                  space
#Slash key:                 slash
#Asterisk key:              asterisk (so it would need `<Shift>` as well)
#Ampersand key:             ampersand (so it would need <Shift> as well)

#a few numpad keys:
#Numpad divide key (`/`):   KP_Divide
#Numpad multiply (Asterisk):KP_Multiply
#Numpad number key(s):      KP_1
#Numpad `-`:                KP_Subtract
