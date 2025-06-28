#!/usr/bin/bash

there=$1
if [[ -z $1 ]]; then
    read -p "Enter absolute path fore THERE: " there
fi

here=$(pwd)

echo $there | grep '/$' > /dev/null
if [[ $? -eq 0 ]] ; then
    # Exclude last character 'https://stackoverflow.com/questions/27658675/how-to-remove-last-n-characters-from-a-string-in-bash'
    there=${there:0:${#there}-1}
fi

echo "$here" > /tmp/here_dir
echo "$there" > /tmp/there_dir

file_name=/tmp/here_there.txt
comma_file=/tmp/coma_files

/usr/bin/rm $file_name 2> /dev/null
/usr/bin/rm $comma_file 2> /dev/null

IFS=$'\n'
for i in $(ls -a . "$there" | grep -v '/:'  | grep -v ^$ | sort -u); do
    echo "$i" | grep -o ',' > /dev/null
    if [[ $? -eq 0 ]]; then
        echo "$i" >> $comma_file
        continue
    fi

    here_kb=
    there_kb=

    test -e "./$i"
    if [[ $? -eq 0 ]]; then
        here_kb=$(du -sk "./$i" 2>/dev/null | awk '{print $1}')
    fi

    test -e "$there/$i"
    if [[ $? -eq 0 ]]; then
        there_kb=$(du -sk "$there/$i" 2>/dev/null | awk '{print $1}')
    fi
    echo "$i,$here_kb,$there_kb" >> $file_name
done

# echo $file_name | column -t -s,

/home/amir/.venv_base/bin/python3 /amir_bin/remove_files_and_folders_that_are_here_and_there_FROM_HERE_python_part.py