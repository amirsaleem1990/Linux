# export HISTTIMEFORMAT="%d/%m/%y %T "
# function open () { for i in  "$@"; do xdg-open $i ; done & }

# hack to launch bicon if not launched
# if ! [[ "$(ps -p $(ps -p $(echo $$) -o ppid=) -o comm=)" =~ 'bicon'* ]]; then
#   bicon.bin
# fi

if [ "$color_prompt" = yes ]; then
	# orignal
    # PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
    # amir modification
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi