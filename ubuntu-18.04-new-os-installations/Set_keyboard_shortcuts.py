#!/usr/bin/python3
import subprocess
import sys

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
        subprocess.call(["/bin/bash", "-c", cmd])

# https://itectec.com/ubuntu/ubuntu-how-to-set-custom-keyboard-shortcuts-from-terminal/

lst = [
['system monitor',            'gnome-system-monitor',                '<Alt>p'              ],
['pinta',                     'pinta',                               '<Super>]'            ],
['screen_shot_selected_area', '/amir_bin/screen_shot_selected_area', '<Alt>a'              ],
['screen_shot_full_window',   '/amir_bin/screen_shot_full_window',   '<Alt>s'              ],
['touch_on_off',              '/amir_bin/touch_on_off',              '<Shift><Control><f9>'],
['Paste',                     '/home/amir/Paste',                    '<Control>1'          ],
['Mn',                        '/usr/bin/xdotool key space',          '<Shift><Control>m'   ],
['Night_light_modify shiny',  '/amir_bin/Night_light_modify +' ,     '<Control><Alt>+'     ],
['Night_light_modify dark',   '/amir_bin/Night_light_modify -' ,     '<Control><Alt>-'     ],
['night_light',               '/amir_bin/night_light',               '<Control><Alt>n'     ],
['namaz',                     '/amir_bin/namaz',                     '<Shift><Control>n'   ]
]

for i in lst:
    name, command, key_combination = i
    func(name, command, key_combination)

#python3 script.py '<name>' '<command>' '<key_combination>'
#python3 script.py 'open gedit' 'gedit' '<Alt>7'

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
