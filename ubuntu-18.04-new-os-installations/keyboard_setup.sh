#!/bin/bash

mkdir ~/.aa
cp /home/amir/github/Linux/ubuntu-18.04-new-os-installations/keyboard-layout-creator.zip ~/.aa
cd ~/.aa
unzip keyboard-layout-creator.zip
rm -f keyboard-layout-creator.zip
cd keboard-layout-creator/
sudo cp amir_keyobard_linux_arabic_urdu /usr/share/X11/xkb/symbols/
sudo subl /usr/share/X11/xkb/rules/evdev.xml


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

sudo dpkg-reconfigure xkb-data
systemctl restart keyboard-setup
gnome-control-center region
rm -f ~/.aa || DEL -rf ~/.aa
