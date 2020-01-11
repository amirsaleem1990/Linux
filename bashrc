# export HISTTIMEFORMAT="%d/%m/%y %T "
# function open () { for i in  "$@"; do xdg-open $i ; done & }

# hack to launch bicon if not launched
sudo apt update
sudo apt install libfribidi0 libfribidi-dev
download from here : https://launchpad.net/~behnam/+archive/ubuntu/ppa/+build/574787/+files/bicon_0.2.0-1ubuntu0~ppa4_amd64.deb
sudo dpkg -i bicon_0.2.0-1ubuntu0~ppa4_amd64.deb

# if ! [[ "$(ps -p $(ps -p $(echo $$) -o ppid=) -o comm=)" =~ 'bicon'* ]]; then
#   bicon.bin
# fi



if youe need only your name in prompt, not computer name.

commit these lines:
	if [ "$color_prompt" = yes ]; then
		PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
	else
		PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
	fi

and add this line:
	PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u:\[\033[01;34m\]\w\[\033[00m\]\$ '