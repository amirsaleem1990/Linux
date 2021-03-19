day_of_week=`date +%u`
if   [[ $day_of_week = 6 ]] ; then
    poweroff
elif [[ $day_of_week = 7 ]] ; then
    if [[ `date +%H | sed 's/^0//g'` < 21 ]] ; then
        poweroff
    fi
fi


PS1='\[\033[01;32m\]`date  +%d-%B-%y\ %H:%M:%S`:\[\033[01;34m\]\w\[\033[00m\]\$ '
PS1='\[\033[01;32m\]\t:\[\033[01;34m\]\w\[\033[00m\]\$ '
PS1='\[\e]0;\u@\h: \w\a\]\[\033[01;32m\]\D{%d-%b}|\t:\[\033[01;34m\]\w\[\033[00m\]\$ '

PATH=$PATH:/amir_bin
export PYTHONPATH="/amir_bin/"

bind '"\C-p": "\C-e\C-u xclip -sel cli <<"EOF"\n\C-y\nEOF\n\C-y"' 

