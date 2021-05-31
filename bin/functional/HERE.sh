# dir=`pwd | sed 's/500GB/amir\/667567ED09032BEE/g'`
# dir=/media/amir/Data_2/raw_synced_data/raw_synced_data
echo -en "Enter THERE location:\n\t" 
read -e dir
before_size=`du -sh $dir`
before_count=`ls $dir | wc -l`
IFS=$'\n'
for i in `find . -maxdepth 1 -type f `; do 
	i=`echo $i | sed 's/^\.\///g'`
	test -e $dir/$i
	if [[ $? == 0 ]]; then
		here=`du -sh $i | sed 's/\t/,/g' | cut -d, -f1 2>/dev/null`
		there=`du -sh $dir/$i | sed 's/\t/,/g' | cut -d, -f1 2>/dev/null`
		if [[ $here == $there ]];then
			echo ">> Same size: $dir/$i, so deleted"
			DEL -rf $dir/$i 2>/dev/null || sudo rm -rf $dir/$i
 		else
			h_=`echo "${here: -1}"`
			t_=`echo "${there: -1}"`
			if [[ $h_ == $t_ ]]; then
				h=`echo $here  | sed 's/[K,M,G]//g' | sed 's/\.0$//g'`
				t=`echo $there | sed 's/[K,M,G]//g' | sed 's/\.0$//g'`
				# if [[ $h -gt $t ]];then
				if [[ $h -gt $t || $h -eq $t ]]; then
					# echo $i $h $t
					# DEL -rf $dir/$i
					DEL -rf $dir/$i 2>/dev/null || sudo rm -rf $dir/$i
				else
					# :
					# echo $h $t
					# echo -e "$i\t$here\t$there"
					# read ans
					# if [[ $ans == "d" ]]; then
					# DEL -rf $dir/$i
					sudo cp $dir/$i .
					# fi
				fi
			fi
		fi
	fi
done

after_size=`du -sh $dir`
after_count=`ls $dir | wc -l`

echo "---- Before ----"
echo "Size : $before_size"
echo "Count: $before_count"

echo ""
echo "---- After ----"
echo "Size : $after_size"
echo "Count: $after_count"