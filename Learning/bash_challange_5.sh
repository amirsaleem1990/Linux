# https://itsfoss.com/bash-challenge-5/
declare	-i SUM=0

while read X ; do 
	if [[ ${X:0:1} == "0" ]]
	then
		X="${X:1}"
	fi

	SUM+=$X;
done < sample.data 



echo $SUM
