#!/bin/bash
echo "
#################################################################################
# This script will loop over all local github repos, and find files that are    # 
# grater than 50 MB, beacuse we cannot push file > 50MB to github, if there     #
# any file > 50MB i'll copy its path and size in                                #
# </home/amir/.GIT_FILES_GRATER_THAN_50_MB> and opeh file in sublime, as well   #
# as print out those details on terminal, and exit                              #
################################################################################# 
"
cd /home/amir/github/
rm -f /home/amir/.GIT_FILES_GRATER_THAN_50_MB
file_greater_than_one=0
IFS=$'\n'
echo -e "\nThese big files are not included in the git_ignore_file"
n=0
for i in $(find . -size  +51199k | grep -v  '^.\/\.' | grep -v '\.pack$\|lfd-projects') ; do  
	file_name=$(basename $i)
	git_ignore_file=/home/amir/github/$(echo $i|  sed 's/^\.\///g' | cut -d/ -f1)/.gitignore
	big_file_name=$(echo $i | rev | cut -d/ -f1 | rev)
	
	grep $big_file_name $git_ignore_file >/dev/null

	if [[ $? -ne 0 ]]; then
		let "n++"
	else
		continue
	fi

	# git_lfs_files=$(cat `find /home/amir/github -name ".gitattributes"` | grep $file_name | wc -l)
	# if [[ $git_lfs_files > 0 ]]; then
	# continue
	# fi
	file_greater_than_one=$(( $file_greater_than_one + 1 )) 
	du -sh $i >> /home/amir/.GIT_FILES_GRATER_THAN_50_MB
	du -sh $i
done

if [[ $file_greater_than_one > 0 ]]; then
	IFS=$'\n'
	RED='\033[0;31m'
	NC='\033[0m' # No Color
	echo -e "\n\n${RED}These files are > 50MB, we need files < 50MB\nPrepare these files and try again${NC}\n\n"
	echo -e "\n\nThese files are > 50MB, we need files < 50MB\nPrepare these files and try again\n\n" >> /home/amir/.GIT_FILES_GRATER_THAN_50_MB

	#subl /home/amir/.GIT_FILES_GRATER_THAN_50_MB
	echo -e "\nAre these files in .gitignore, and you're sure that they can't be pushed? [y|n] "
	read ans
	if [[ $ans == "y" ]]; then
		exit
	fi
	exit 2
fi
