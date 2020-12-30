export SSHPASS=YOUR_PASSWORD
sshpass -e sftp -oBatchMode=no -b - host_name@IP << !
   cd /home/finca/
   ls
   bye
!
