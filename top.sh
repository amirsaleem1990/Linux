for i in {1..10} ; do top -n 1 | grep "amir\|root" | sed 's/\ \{1,\}/,/g' | cut -d "," -f13 > temp.txt; done ; cat temp.txt | uniq | sort ; del -rf temp.txt
