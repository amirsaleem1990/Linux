declare	-i SUM=0

while read X ; do 
	if [[ ${X:0:1} == "0" ]]
	then
		X="${X:1}"
	fi
	SUM+=$X;
done < bash_challange_5.sh 



echo $SUM
