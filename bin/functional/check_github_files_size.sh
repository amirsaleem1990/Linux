#!/bin/bash
if [[ -z $1 ]]; then
	exit
fi

echo "
#################################################################################
# This script will loop over all local github repos, and find files that are    # 
# grater than 50 MB, beacuse we cannot push file > 50MB to github, if there     #
# any file > 50MB i'll copy its path and size in                                #
# </tmp/.GIT_FILES_GRATER_THAN_50_MB> and opeh file in sublime, as well         #
# as print out those details on terminal, and exit                              #
################################################################################# 
"

cd /home/amir/github/
rm -f /tmp/.GIT_FILES_GRATER_THAN_50_MB
file_greater_than_one=0
IFS=$'\n'
echo -e "\n\nThese big files are not included in the git_ignore_file\n"
n=0
for i in $(find . -size  +51199k | grep -v  '^.\/\.' | grep -v '\.pack$\|lfd-projects') ; do  
	file_name=$(basename $i)
	repo_name=$(echo $i | cut -d/ -f2)

	cd /home/amir/github/"$repo_name"

	# git_ignore_file=/home/amir/github/$(echo $i|  sed 's/^\.\///g' | cut -d/ -f1)/.gitignore
	big_file_name=$(echo $i | rev | cut -d/ -f1 | rev)
	
	# grep $big_file_name $git_ignore_file >/dev/null

	# if [[ $? -eq 0 ]]; then
	# 	continue
	# fi


	# git_lfs_files=$(cat `find /home/amir/github -name ".gitattributes"` | grep $file_name | wc -l)
	# if [[ $git_lfs_files > 0 ]]; then
	# continue
	# fi

	git check-ignore "/home/amir/github/$i" >/dev/null
	if [[ $? -eq 0 ]]; then
		continue
	fi

	let "n++"

	file_greater_than_one=$(( $file_greater_than_one + 1 )) 
	du -sh "/home/amir/github/$i" >> /tmp/.GIT_FILES_GRATER_THAN_50_MB
	du -sh "/home/amir/github/$i"
done

if [[ $file_greater_than_one > 0 ]]; then
	IFS=$'\n'
	RED='\033[0;31m'
	NC='\033[0m' # No Color
	echo -e "\n\n${RED}These files are > 50MB, we need files < 50MB\nAdd this/theese file/s to .gitignore or move them from repository, and try again${NC}\n\n"
	# # echo -e "\n\nThis/these file/s is/are > 50MB, we need files < 50MB\nAdd this/theese file/s to .gitignore or move them from repository, and try again\n\n" >> /tmp/.GIT_FILES_GRATER_THAN_50_MB
	# # subl /tmp/.GIT_FILES_GRATER_THAN_50_MB
	# echo -e "\nAre these files in .gitignore, and you're sure that they can't be pushed? [y|n] "
	# read ans
	# if [[ $ans == "y" ]]; then
	# 	exit
	# fi
	exit 2
fi
