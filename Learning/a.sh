declare	-i SUM=0

while read X ; do 
	SUM+=$X; 
done < bash_challange_5.sh 



echo $SUM
