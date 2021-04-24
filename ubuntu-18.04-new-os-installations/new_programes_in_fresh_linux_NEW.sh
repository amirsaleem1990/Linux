# !/bin/bash
mkdir -p /home/amir/.local/share/Trash/files

echo "If you execute this script with sudo please enter any key to proceed, else terminate this script and execute it with sudo"
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


func_ "sudo apt-get update"
func_ "sudo apt-get -y upgrade"
func_ "sudo apt install -y ipython3"
func_ "sudo apt install -y python3-pip"
func_ "sudo apt install -y feh"
func_ "sudo apt install -y xsel"
func_ "sudo apt install -y gnustep-gui-runtime"
func_ "sudo apt install -y vokoscreen"
func_ "sudo apt install -y git"
func_ "sudo apt install -y speedtest-cli"
func_ "sudo apt install -y pinta"
func_ "sudo apt install -y nautilus-dropbox"
func_ "sudo apt install -y tmux"
func_ "sudo apt install -y nethogs"
func_ "sudo apt install -y tree"
func_ "sudo apt install -y gdebi-core"
func_ "sudo apt install -y ffmpeg"
func_ "sudo apt install -y translate-shell"
func_ "sudo apt install -y htop"
func_ "sudo apt install -y apt-transport-https"
func_ "sudo apt install -y ca-certificates"
func_ "sudo apt install -y curl"
func_ "sudo apt install -y software-properties-common"

func_ "curl -fsSL https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -"
func_ "sudo add-apt-repository 'deb https://download.sublimetext.com/ apt/stable/'"
func_ "sudo apt install sublime-text"
if [[ $? != 0 ]]; then 
	func_ "sudo snap install --classic sublime-text"
fi
func_ "sudo snap install vlc"
func_ "sudo apt-get install -y gdebi"
func_ "firefox http://download.opensuse.org/repositories/home:/colomboem/xUbuntu_16.04/amd64/dukto_6.0-1_amd64.deb"
func_ "sudo dpkg -i Downloads/dukto*"
# func_ "sudo gdebi dukto_6.0-1_amd64.deb"
# rm -r dukto_6.0-1_amd64.deb

# func_ "sudo apt-get install -y r-base r-base-dev libatlas3-base libopenblas-base"
# firefox https://cloud.r-project.org/
sudo apt-get install -y r-base r-base-dev libatlas3-base libopenblas-base  >> /home/amir/results.txT
if [[ $? != 0 ]]; then echo "firefox https://cloud.r-project.org/"; exit ; fi
read -p "Install R manually, and then pres any key: "
if [[ $? != 0 ]]; then echo "read -p Install R manually, and then pres any key"; exit ; fi

func_ "sudo apt-get -y install openjdk-11-jdk"
func_ "sudo apt-get -y install r-cran-rjava"
func_ "sudo R CMD javareconf"
func_ "sudo apt-get install -y libcurl4-openssl-dev"
func_ "sudo apt-get install -y libxml2-dev"
func_ "sudo apt-get install -y libssl-dev"
func_ "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/r_essential_packages.R"
func_ "sudo Rscript r_essential_packages.R"
func_ "sudo apt install -y jupyter-core"
func_ "pip3 install jupyterlab"
func_ "pip3 install xlrd==1.2.0"
func_ "sudo apt-get install -y jupyter-client"
func_ "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/R_in_jupyter.R"
func_ "sudo Rscript R_in_jupyter.R"
func_ "curl https://download1.rstudio.org/desktop/bionic/amd64/rstudio-1.2.1335-amd64.deb > rstudio.deb"
func_ "sudo gdebi -n rstudio*.deb"
func_ "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/set_startupscript.py"
func_ "ipython3 set_startupscript.py"
rm -f set_startupscript.py  >> /home/amir/results.txT

#func_ "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/alias.txt"
func_ "wget https://github.com/amirsaleem1990/Linux/blob/master/alias"

if [[ $? != 0 ]]; 
	then echo "cat alias.txt >> ~/.bashrc"
	exit
fi
rm -f alias.txt

echo 'PATH="/amir_bin/:$PATH"' >> ~/.bashrc
source  ~/.bashrc

func_ "pip3 install youtube-dl"
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
func_ "pip3 install pickle"
func_ "pip3 install env"

func_ "curl -fsSL https://get.docker.com -o get-docker.sh"
func_ "sudo sh get-docker.sh"

func_ "wget https://raw.githubusercontent.com/amirsaleem1990/git/master/github%20initial%20setup"
func_ "bash 'github initial setup'"

# func_ "sudo mkdir /amir_bin/"
sudo ln -s  /home/amir/github/Linux/bin/functional/ /amir_bin

# func_ "pip3 install statsmodels"
# func_ "apm install ask-stack"
# func_ "apm install stack-overflow-help"



