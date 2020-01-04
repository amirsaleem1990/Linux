#!/bin/bash
IFS=$'\n'
for folder in $(ls -d */) ;  do 
	cd `echo $folder`
	echo $folder
	sum=0
	for i in `find . -iname  "*.pdf"` ; do 
		f=`pdfinfo $(echo $i) | grep Pages\: | sed 's/Pages:          //g'`
		sum=$(( $sum + $f ))
	done
	echo "Pages: $sum  | Books: `find . -iname '*.pdf' | wc -l`" 
	cd ../
done
