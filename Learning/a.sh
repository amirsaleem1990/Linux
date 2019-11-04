declare	-i SUM=0

while read X ; do
	echo "SUM: $SUM, X:$X" 
	if [[ ${X:0:1} == "0" ]]
	then
		X="${X:1}"
	else
		SUM+=$X;
	fi 
done < bash_challange_5.sh 



echo $SUM
