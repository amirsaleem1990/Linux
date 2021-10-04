# !/bin/bash
mkdir -p /home/amir/.local/share/Trash/files

echo "If you execute this script with please enter any key to proceed, else terminate this script and execute it with sudo"
read ans

echo "\n\nRedirected to /home/amir/results.txT\n\n"
func_(){
	echo -e "\n\n>>>>>>>>>>>>>>>>>>>>>>>> Start: $1\n\n"
	eval $1 >> /home/amir/results.txT
	if [[ $? != 0 ]]; then 
		echo "FAIL: $1"
		exit
	fi
}

# @install.packages("FNN", "e1071", repos=repo)
# @install.packages("caret", repos=repo)
# @install.packages("swirl", repos=repo)

func_ "apt -y update"
func_ "apt -y upgrade"


func_ "apt install -y virtualbox-qt"
func_ "apt install -y screen"
func_ "apt install -y rdfind"
func_ "apt install -y xclip"
func_ "apt install -y dos2unix"
func_ "apt install -y net-tools"
func_ "apt install -y mlocate"
func_ "apt install -y testdisk"
func_ "apt install -y mysql-client-core*"
func_ "apt install -y vlc-bin"
func_ "apt install -y ipython3"
func_ "apt install -y python3-pip"
func_ "apt install -y feh"
func_ "apt install -y xsel"
func_ "apt install -y gnustep-gui-runtime"
func_ "apt install -y vokoscreen"
func_ "apt install -y git"
func_ "apt install -y speedtest-cli"
func_ "apt install -y pinta"
func_ "apt install -y nautilus-dropbox"
func_ "apt install -y tmux"
func_ "apt install -y nethogs"
func_ "apt install -y tree"
func_ "apt install -y gdebi-core"
func_ "apt install -y ffmpeg"
func_ "apt install -y translate-shell"
func_ "apt install -y htop"
func_ "apt install -y apt-transport-https"
func_ "apt install -y ca-certificates"
func_ "apt install -y curl"
func_ "apt install -y software-properties-common"
func_ "apt install -y jupyter-core"
func_ "apt install -y adb"
func_ "apt install -y imagemagick-6.q16hdri"
func_ "apt install -y python3-virtualenv"
func_ "apt install -y unrar"
func_ "apt install -y unrar-free"
func_ "apt install -y dolphin"
func_ "apt install -y nomacs"
func_ "apt install -y coreutils"
func_ "apt install -y mysql-server"
func_ "apt install -y gdebi"
func_ "apt install -y openjdk-11-jdk"
func_ "apt install -y r-cran-rjava"
func_ "apt install -y libcurl4-openssl-dev"
func_ "apt install -y libxml2-dev"
func_ "apt install -y libssl-dev"
func_ "apt install -y jupyter-client"
func_ "apt install -y gparted"
func_ "apt install -y youtube-dl"


func_ "snap install vlc"
func_ "snap install scrcpy"
func_ "snap install pdftk"
func_ "snap install googler"
func_ "snap install chromium"

func_ "curl -fsSL https://download.sublimetext.com/sublimehq-pub.gpg | apt-key add -"
func_ "add-apt-repository 'deb https://download.sublimetext.com/ apt/stable/'"
func_ "apt install sublime-text"
if [[ $? != 0 ]]; then 
	func_ "snap install --classic sublime-text"
fi

func_ "wget http://download.opensuse.org/repositories/home:/colomboem/xUbuntu_16.04/amd64/dukto_6.0-1_amd64.deb"

dpkg -i dukto*
if [[ $? != 0 ]]; then
	add-apt-repository ppa:rock-core/qt4
	apt-get update
	apt --fix-broken install
	apt install libqtgui4
	apt autoremove
else
	func_ "dukto installed"
fi

# func_ "gdebi dukto_6.0-1_amd64.deb"
rm -r dukto*.deb

# func_ "apt-get install -y r-base r-base-dev libatlas3-base libopenblas-base"
# firefox https://cloud.r-project.org/
# apt-get install -y r-base r-base-dev libatlas3-base libopenblas-base  >> /home/amir/results.txT
# if [[ $? != 0 ]]; then 
	# func_ "apt install r-cran-littler"
# if [[ $? != 0 ]]; then read -p "Install R manually, and then pres any key: "; fi

# func_ "R CMD javareconf"
# func_ "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/r_essential_packages.R"
# func_ "Rscript r_essential_packages.R"
func_ "pip3 install jupyterlab"
func_ "pip3 install xlrd==1.2.0"
# func_ "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/R_in_jupyter.R"
# func_ "Rscript R_in_jupyter.R"


func_ "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/set_startupscript.py"
func_ "ipython3 set_startupscript.py"
rm -f set_startupscript.py  >> /home/amir/results.txT

#func_ "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/alias.txt"
#func_ "wget https://github.com/amirsaleem1990/Linux/blob/master/alias"
func_ "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/alias"
# if [[ $? != 0 ]]; 
	#then echo "cat alias.txt >> ~/.bashrc"
	#exit
# fi
# cp .bashrc{,_backup}; cat .bashrc alias  > xmklk; mv xmklk .bashrc; rm -f xmklk; rm -f alias; source .bashrc


#echo 'PATH="/amir_bin/:$PATH"' >> ~/.bashrc
#source  ~/.bashrc

# func_ "pip3 install youtube-dl"
func_ "pip3 install bs4"
func_ "pip3 install lxml"
func_ "pip3 install selenium"
func_ "pip3 install tabulate"
func_ "pip3 install pandas"
func_ "pip3 install sklearn "
func_ "pip3 install pandas_profiling "
func_ "pip3 install clipboard "
func_ "pip3 install termcolor"
func_ "pip3 install tqdm"
func_ "pip3 install psutil"
func_ "pip3 install env"
func_ "pip3 install sqlalchemy"
func_ "pip3 install fpdf"
func_ "pip3 install pymysql"


#func_ "curl -fsSL https://get.docker.com -o get-docker.sh"
#func_ "sh get-docker.sh"

#func_ "wget https://raw.githubusercontent.com/amirsaleem1990/git/master/github%20initial%20setup"
#mv 'github initial setup' github_initial_setup
#func_ "bash github_initial_setup"

# func_ "mkdir /amir_bin/"
ln -s  /home/amir/github/Linux/bin/functional/ /amir_bin

# func_ "pip3 install statsmodels"
# func_ "apm install ask-stack"
# func_ "apm install stack-overflow-help"


# rstudio
#latest_rstudio_version=`python3 <<< "from bs4 import BeautifulSoup; import requests; print(BeautifulSoup(requests.get('https://www.rstudio.com/products/rstudio/download/#download').text, 'lxml').find('h3', {'id' : 'download'}).text.strip('RStudio Desktop '))"`
#latest_rstudio_download_link="https://download1.rstudio.org/desktop/bionic/amd64/rstudio-$latest_rstudio_version-amd64.deb"
#curl $latest_rstudio_download_link > rstudio-$latest_rstudio_version.deb
#func_ "gdebi -n rstudio*.deb"


# dukto
# add-apt-repository ppa:rock-core/qt4; add-apt-repository ppa:gezakovacs/ppa; apt update; apt-get install -y libqtgui4



echo -e "\n\n"
echo "Please set <nomacs> as default app as image viewer. and then entery any key ......"
gnome-control-center default-apps
read ans



# keyboad light ka time 100 seconds kar dya h, by default is ka time 1s hota h
echo 100s > /sys/devices/platform/dell-laptop/leds/dell\:\:kbd_backlight/stop_timeout

func_ "echo 100 > `locate kbd_backlight`"



echo "Apply this <'/home/amir/github/Linux/ubuntu-18.04-new-os-installations/Mount\ drive\ in\ linux\ and\ set\ auto-mount\ at\ boot\ -\ Tech\ Knowledge\ Base\ -\ jaytaala.com\ Confluence\ \(8_17_2021\ 1_41_49\ PM\).html'>"


echo -e "\n25 18   * * *   root    /amir_bin/lfd_off_notification" | sudo tee --append /etc/crontab # Remember about the (-a/--append) flag! Just tee works like > and will overwrite your file. tee -a works like >> and will write at the end of the file.

