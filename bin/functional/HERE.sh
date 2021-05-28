# dir=`pwd | sed 's/500GB/amir\/667567ED09032BEE/g'`
dir=/media/amir/667567ED09032BEE/LFD/Kash_raw_data/raw_synced_data

IFS=$'\n'
for i in `find . -maxdepth 1 -type f `; do 
	i=`echo $i | sed 's/^\.\///g'`
	test -e $dir/$i
	if [[ $? == 0 ]]; then
		here=`du -sh $i | sed 's/\t/,/g' | cut -d, -f1 2>/dev/null`
		there=`du -sh $dir/$i | sed 's/\t/,/g' | cut -d, -f1 2>/dev/null`
		if [[ $here == $there ]];then
			# echo $i
			DEL -rf $dir/$i
		else
			:
			h_=`echo "${here: -1}"`
			t_=`echo "${there: -1}"`
			if [[ $h_ == $t_ ]]; then
				h=`echo $here  | sed 's/[K,M,G]//g' | sed 's/\.0$//g'`
				t=`echo $there | sed 's/[K,M,G]//g' | sed 's/\.0$//g'`
				if [[ $h -gt $t ]];then
					echo $i $h $t
					DEL -rf $dir/$i
				else
					:
					# echo $h $t
					# echo -e "$i\t$here\t$there"
					# read ans
					# if [[ $ans == "d" ]]; then
					# 	DEL -rf $dir/$i
					# fi
				fi
			fi
		fi
	fi
done
