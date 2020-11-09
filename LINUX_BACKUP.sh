#!/bin/bash

cd /home/amir/

if cat /proc/mounts | grep -qs 450GB; then
    echo -e "\n\nPartition Already Mounted"
else
	echo -e "\n\nMounting Partition"
    echo `echo tradersUbuntu` | sudo -S -k mount /dev/sdb2 /media/450GB/ || echo `echo UBUNTU1990` | sudo -S -k mount /dev/sdb2 /media/450GB/
fi


while :; do
	p=`cat /home/amir/.Local_backup_permision`
	if [[ $p == True ]]; then 
		rsync -rvxu  /home/amir/ /media/450GB/LINUX_BACKUP/
		echo "`date +%s`" > /home/amir/.Last_local_backup_time
	fi
	sleep 3600 # 1 hour
done
