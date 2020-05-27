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
for i in `find . -size  +51199k | grep -v  '^.\/\.'` ; do  
	if [[ `echo $i | grep .pack$` ]] ; then 
		continue
	fi
	# if [[ `echo $i | grep .git` ]]; then
	# 	continue
	# fi
	if [[ `echo $i | grep lfd-projects` ]]; then
		continue
	fi
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

	subl /home/amir/.GIT_FILES_GRATER_THAN_50_MB
	exit 2
fi