#!/usr/bin/bash 


echo "If you execute this script with please enter any key to proceed, else terminate this script and execute it with sudo"
read ans

mkdir -p /home/amir/.local/share/Trash/files
chown amir.amir /home/amir/.local/share/Trash/files -R

echo -e "\n\nRedirected to /home/amir/results.txT\n\n"
func_(){
	echo -e "\n\n>>>>>>>>>>>>>>>>>>>>>>>> Start: $1\n\n"
	eval $1 >> /home/amir/results.txT
	if [[ $? -ne 0 ]]; then 
		echo "FAIL: $1"
		exit
	fi
}

# @install.packages("FNN", "e1071", repos=repo)
# @install.packages("caret", repos=repo)
# @install.packages("swirl", repos=repo)

# Enable the battery percentage display next to the battery icon in the top-right corner of the screen
func_ "gsettings set org.gnome.desktop.interface show-battery-percentage true"
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
# func_ "apt install -y youtube-dl"
func_ "apt install -y googler"
func_ "apt install -y lz4json"
func_ "apt install -y sqlite3"
func_ "apt install -y aha"
func_ "apt install -y pylint"
func_ "apt install -y jupyter*"
func_ "apt install -y toilet"
func_ "apt install -y ifstat"
func_ "apt install -y python3.8-venv"
func_ "apt install -y azure-cli"
func_ "apt install -y azure-functions-core-tools-4"
func_ "apt install -y arp-scan"
func_ "apt install -y openssh-server"



func_ "snap install vlc"
func_ "snap install scrcpy"
func_ "snap install pdftk"
# func_ "snap install googler"
func_ "snap install chromium"
func_ "snap install yt-dlp"
func_ "snap install opera"
func_ "snap install code --classic"
func_ "snap install android-studio --classic"


func_ "curl -fsSL https://download.sublimetext.com/sublimehq-pub.gpg | apt-key add -"
func_ "add-apt-repository 'deb https://download.sublimetext.com/ apt/stable/'"
func_ "apt install sublime-text -y"
if [[ $? -ne 0 ]]; then 
	func_ "snap install --classic sublime-text"
fi

# func_ "wget http://download.opensuse.org/repositories/home:/colomboem/xUbuntu_16.04/amd64/dukto_6.0-1_amd64.deb"
# dpkg -i dukto*
# if [[ $? -ne 0 ]]; then
# 	func_ "apt -f install -y"
# 	if [[ $? -ne 0 ]] ;then
# 		add-apt-repository ppa:rock-core/qt4
# 		add-apt-repository ppa:gezakovacs/ppa
# 		apt update -y
# 		apt --fix-broken install -y
# 		apt install libqtgui4 -y
# 		apt autoremove -y
# 	fi
# fi
# rm -r dukto*.deb

apt install -y r-base r-base-dev libatlas3-base libopenblas-base  >> /home/amir/results.txT
if [[ $? -ne 0 ]]; then 
	func_ "apt install r-cran-littler -y"
fi

if [[ $? -ne 0 ]]; then 
	read -p "Install R manually, and then pres any key: "; 
	firefox https://cloud.r-project.org/
fi

func_ "R CMD javareconf"
func_ "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/r_essential_packages.R"
func_ "Rscript r_essential_packages.R"
func_ "pip3 install jupyterlab"
func_ "pip3 install xlrd==1.2.0"
func_ "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/R_in_jupyter.R"
func_ "Rscript R_in_jupyter.R"

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
func_ "pip3 install ipykernel"
func_ "pip3 install jupyter"
func_ "pip3 install youtube-dl==2021.12.17"
func_ "pip3 install django-browser-reload"
func_ "pip3 install faker"


func_ "curl -fsSL https://get.docker.com -o get-docker.sh"
func_ "sh get-docker.sh"

func_ "ln -s  /home/amir/github/Linux/bin/functional/ /amir_bin"

func_ "pip3 install statsmodels"
# func_ "apm install ask-stack"
# func_ "apm install stack-overflow-help"


# rstudio
latest_rstudio_version=`python3 <<< "from bs4 import BeautifulSoup; import requests; print(BeautifulSoup(requests.get('https://www.rstudio.com/products/rstudio/download/#download').text, 'lxml').find('h3', {'id' : 'download'}).text.strip('RStudio Desktop '))"`

echo -e "\nGetting latest rstudio download link  ....,,,,,,,"
latest_rstudio_download_link=$(python3 <<< "
from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup(requests.get('https://www.rstudio.com/products/rstudio/download/#download').text, 'lxml') 
for i in soup.select('a'):
    try:
        l = i['href']
        if l.endswith('.deb') and not '/debian' in l:
            print(i['href'])
    except:
        pass
")

echo -e "\nDownload latest rstudio  ....,,,,,,,"
curl $latest_rstudio_download_link > "rstudio-$latest_rstudio_version.deb"
# func_ "gdebi -n rstudio*.deb"

echo -e "\nInstalling rstudio ....,,,,,,,"
dpkg -i rstudio*.deb >> /home/amir/results.txT
if [[ $? -ne 0 ]]; then
	apt -f install -y
	func_ "dpkg -i rstudio*.deb"
fi


echo -e "\n\n"
echo "Please set <nomacs> as default app as image viewer. and then entery any key ......"
gnome-control-center default-apps
read ans


# keyboad light ka time 2m seconds kar dya h, by default is ka time 1m hota h
echo 2m > /sys/devices/platform/dell-laptop/leds/dell\:\:kbd_backlight/stop_timeout

func_ "echo 100 > `locate kbd_backlight`"

echo "Apply this <'/home/amir/github/Linux/ubuntu-18.04-new-os-installations/Mount\ drive\ in\ linux\ and\ set\ auto-mount\ at\ boot\ -\ Tech\ Knowledge\ Base\ -\ jaytaala.com\ Confluence\ \(8_17_2021\ 1_41_49\ PM\).html'>"


echo -e "\n25 18   * * *   root    /amir_bin/lfd_off_notification" | tee --append /etc/crontab 
# Remember about the (-a/--append) flag! Just tee works like > and will overwrite your file. tee -a works like >> and will write at the end of the file.



#lated
apt install texlive-lang-cyrillic texlive-latex-extra texlive-latex-recommended texlive-pictures texlive-latex-base libfontconfig1-dev libharfbuzz-dev libfribidi-dev libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev -y
apt install libfontconfig1-dev libharfbuzz-dev libclang-dev  libpq5



