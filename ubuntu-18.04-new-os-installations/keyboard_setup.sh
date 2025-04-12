#!/bin/bash

# https://blog.simos.info/the-keyboard-layout-editor/
# ا,أ,إ,ب,پ‎,ت,ٹ,ث,ج,چ,ح,خ,د,ڈ,ذ,ر‎,ڑ,ز,س,ش,ص,ض,ط,‎ظ,ع,غ,ف,ق,ك,گ,ل,م,ن,‎ں,و,ه,ھ,ء‎,ي,ى‎,ے

mkdir ~/.aa
cp /home/amir/github/Linux/ubuntu-18.04-new-os-installations/keyboard-layout-creator.zip ~/.aa
cd ~/.aa
unzip keyboard-layout-creator.zip
rm -f keyboard-layout-creator.zip
cd keboard-layout-creator/
sudo cp amir_keyboard_linux_arabic_urdu /usr/share/X11/xkb/symbols/

echo -e "Go to the end of the <layoutList> section (search for </layoutList>). Add the following after the last </layout> tag
<layout>
 <configItem>
   <name>Amir</name>
   <shortDescription>Amir_personal_keyboard</shortDescription>
   <description>Amir_keyboard</description>
   <languageList>
      <iso639Id>ara</iso639Id>
      <iso639Id>urd</iso639Id>
   </languageList>
 </configItem>
 <variantList/>
</layout>"
sleep 3s
sudo subl /usr/share/X11/xkb/rules/evdev.xml


read -p "Save the evdev.xml file, and then press any key "

echo " Add
amir_keyboard_linux_arabic_urdu     Amir_personal_keyboard
at the very end of evdev.lst
"
sleep 3s
sudo subl /usr/share/X11/xkb/rules/evdev.lst
read -p "Save the evdev.lst file, and then press any key "


echo "
change input language to amir_keyboard_linux_arabic_urdu (from settings)
"

sudo dpkg-reconfigure xkb-data
sudo systemctl restart keyboard-setup
gnome-control-center region
rm -f ~/.aa || DEL -rf ~/.aa

echo "
DONE!!

NOTE: if you need another version of keyboad, create your own layout using this application:
/home/amir/github/Linux/ubuntu-18.04-new-os-installations/keboard-layout-creator/keyboardlayouteditor/KeyboardLayoutEditor
"