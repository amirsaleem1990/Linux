while :; do 
	e=`bash a.sh  | grep -v 'sftp>' | wc -l`
	if [[ $e != 1 ]]; then
		vokoscreen
	else
		sleep 5m
	fi
done