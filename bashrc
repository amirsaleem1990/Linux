day_of_week=`date +%u`
if   [[ $day_of_week = 6 ]] ; then
    poweroff
elif [[ $day_of_week = 7 ]] ; then
    if [[ `date +%H | sed 's/^0//g'` < 21 ]] ; then
        poweroff
    fi
fi

replace
	HISTSIZE=100000
	HISTFILESIZE=-1

	PS1='\[\033[01;32m\]`date  +%d-%B-%y\ %H:%M:%S`:\[\033[01;34m\]\w\[\033[00m\]\$ '
	PS1='\[\033[01;32m\]\t:\[\033[01;34m\]\w\[\033[00m\]\$ '
	PS1='\[\e]0;\u@\h: \w\a\]\[\033[01;32m\]\D{%d-%b}|\t:\[\033[01;34m\]\w\[\033[00m\]\$ '
	PS1='\[\e]0;\u@\h: \w\a\]\e[1m\e[20m\D{%d-%b}|\t:\[\033[01;34m\]\w\[\033[00m\]\$ '
	PS1='\[\e]0;\u@\h: \w\a\]\e[7m\D{%d-%b}|\t\e[27m:\w\$ '
	PS1='\[\e]0;\w\a\]\e[7m\D{%d-%b}|\t\e[27m:\e[1m\w\e[21m\033[00m\]\$ '

add:
	PATH=$PATH:/amir_bin
	export PYTHONPATH="/amir_bin/"
	bind '"\C-p": "\C-e\C-u xclip -sel cli <<"EOF"\n\C-y\nEOF\n\C-y"' 

