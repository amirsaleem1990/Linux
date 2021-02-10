1- start adb server ................ adb start-server

2- Connect to mobile:
	a- via USB
		mobile ko computer sy via cable connect karen
	b- Wireless
		mobile ko computer sy via cable connect karen
		adb tcpip 5555 # ye msg show ho ga <restarting in TCP mode port: 5555>
		adb connect YOUR_MOBILE_IP_ADDRESS # eg: 192.168.100.74
		computer sy cable detetch kar den.

3- adb push file_to_push_path /sdcard/

4- list all files in mobile ............ adb shell ls
5- list all (recursive) files in mobile ............ adb shell ls -R /

4- adb pull file_path_in_mobile .
# https://forum.xda-developers.com/android/general/guide-installing-adb-fastboot-linux-adb-t3478678
# https://www.online-tech-tips.com/smartphones/how-to-use-adb-wirelessly-on-your-android/







