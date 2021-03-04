#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt install -y ipython3
if [[ $? != 0 ]]; then echo "sudo apt install -y ipython3"; exit ; fi
sudo apt install -y python3-pip
if [[ $? != 0 ]]; then echo "sudo apt install -y python3-pip"; exit ; fi
sudo apt install -y feh
if [[ $? != 0 ]]; then echo "sudo apt install -y feh"; exit ; fi
sudo apt install -y xsel # # to work my alis <copyto>
if [[ $? != 0 ]]; then echo "sudo apt install -y xsel # # to work my alis <copyto>"; exit ; fi
sudo apt install -y gnustep-gui-runtime #gopen
if [[ $? != 0 ]]; then echo "sudo apt install -y gnustep-gui-runtime #gopen"; exit ; fi
sudo apt install -y vokoscreen
if [[ $? != 0 ]]; then echo "sudo apt install -y vokoscreen"; exit ; fi
sudo apt install -y git
if [[ $? != 0 ]]; then echo "sudo apt install -y git"; exit ; fi
sudo apt install -y speedtest-cli
if [[ $? != 0 ]]; then echo "sudo apt install -y speedtest-cli"; exit ; fi
sudo apt install -y pinta
if [[ $? != 0 ]]; then echo "sudo apt install -y pinta"; exit ; fi
sudo apt install -y nautilus-dropbox
if [[ $? != 0 ]]; then echo "sudo apt install -y nautilus-dropbox"; exit ; fi
sudo apt install -y tmux
if [[ $? != 0 ]]; then echo "sudo apt install -y tmux"; exit ; fi
sudo apt install -y nethogs
if [[ $? != 0 ]]; then echo "sudo apt install -y nethogs"; exit ; fi
sudo apt install -y tree
if [[ $? != 0 ]]; then echo "sudo apt install -y tree"; exit ; fi
sudo apt install -y gdebi-core
if [[ $? != 0 ]]; then echo "sudo apt install -y gdebi-core"; exit ; fi
sudo apt install -y ffmpeg
if [[ $? != 0 ]]; then echo "sudo apt install -y ffmpeg"; exit ; fi
sudo apt install -y xsel
if [[ $? != 0 ]]; then echo "sudo apt install -y xsel"; exit ; fi
sudo apt install -y translate-shell
if [[ $? != 0 ]]; then echo "sudo apt install -y translate-shell"; exit ; fi
sudo apt install -y htop
if [[ $? != 0 ]]; then echo "sudo apt install -y htop"; exit ; fi
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
if [[ $? != 0 ]]; then echo "sudo apt install -y apt-transport-https ca-certificates curl software-properties-common"; exit ; fi
curl -fsSL https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
if [[ $? != 0 ]]; then echo "curl -fsSL https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -"; exit ; fi
sudo add-apt-repository "deb https://download.sublimetext.com/ apt/stable/"
if [[ $? != 0 ]]; then echo "sudo add-apt-repository "deb https://download.sublimetext.com/ apt/stable/""; exit ; fi
sudo apt update
sudo apt install sublime-text
if [[ $? != 0 ]]; then 
	sudo snap install --classic sublime-text
	if [[ $? != 0 ]] ; then
		echo "sudo apt install sublime-text"; exit
	fi
fi
sudo snap install vlc
if [[ $? != 0 ]]; then echo "sudo snap install vlc"; exit ; fi
sudo apt-get install -y gdebi
if [[ $? != 0 ]]; then echo "sudo apt-get install -y gdebi"; exit ; fi
wget download.opensuse.org/repositories/home:/colomboem/xUbuntu_16.04/amd64/dukto_6.0-1_amd64.deb
if [[ $? != 0 ]]; then echo "wget download.opensuse.org/repositories/home:/colomboem/xUbuntu_16.04/amd64/dukto_6.0-1_amd64.deb"; exit ; fi
sudo gdebi dukto_6.0-1_amd64.deb
if [[ $? != 0 ]]; then echo "sudo gdebi dukto_6.0-1_amd64.deb"; exit ; fi
rm -r dukto_6.0-1_amd64.deb
if [[ $? != 0 ]]; then echo "rm -r dukto_6.0-1_amd64.deb"; exit ; fi
# firefox https://cloud.r-project.org/
sudo apt-get update
sudo apt-get install -y r-base r-base-dev libatlas3-base libopenblas-base
# if [[ $? != 0 ]]; then echo "firefox https://cloud.r-project.org/"; exit ; fi
# read -p "Install R manually, and then pres any key: "
# if [[ $? != 0 ]]; then echo "read -p Install R manually, and then pres any key"; exit ; fi
sudo apt-get -y install openjdk-11-jdk
if [[ $? != 0 ]]; then echo "sudo apt-get -y install openjdk-11-jdk"; exit ; fi
sudo apt-get -y install r-cran-rjava
if [[ $? != 0 ]]; then echo "sudo apt-get -y install r-cran-rjava"; exit ; fi
sudo R CMD javareconf
if [[ $? != 0 ]]; then echo "sudo R CMD javareconf"; exit ; fi
sudo apt-get install -y libcurl4-openssl-dev
if [[ $? != 0 ]]; then echo "sudo apt-get install -y libcurl4-openssl-dev"; exit ; fi
sudo apt-get install -y libxml2-dev
if [[ $? != 0 ]]; then echo "sudo apt-get install -y libxml2-dev"; exit ; fi
sudo apt-get install -y libssl-dev
if [[ $? != 0 ]]; then echo "sudo apt-get install -y libssl-dev"; exit ; fi
wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/r_essential_packages.R
sudo Rscript r_essential_packages.R
if [[ $? != 0 ]]; then echo "sudo Rscript r_essential_packages.R"; exit ; fi
sudo apt install -y jupyter-core
if [[ $? != 0 ]]; then echo "sudo apt install -y jupyter-core"; exit ; fi
pip3 install jupyterlab
if [[ $? != 0 ]]; then echo "pip3 install jupyterlab"; exit ; fi
sudo apt-get install -y jupyter-client
if [[ $? != 0 ]]; then echo "sudo apt-get install -y jupyter-client"; exit ; fi
R_in_jupyter.R
wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/R_in_jupyter.R
sudo Rscript R_in_jupyter.R
if [[ $? != 0 ]]; then echo "sudo Rscript R_in_jupyter.R"; exit ; fi
curl https://download1.rstudio.org/desktop/bionic/amd64/rstudio-1.2.1335-amd64.deb > rstudio.deb
if [[ $? != 0 ]]; then echo "curl https://download1.rstudio.org/desktop/bionic/amd64/rstudio-1.2.1335-amd64.deb > rstudio.deb"; exit ; fi
sudo gdebi -n rstudio*.deb
if [[ $? != 0 ]]; then echo "sudo gdebi -n rstudio*.deb"; exit ; fi
wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/set_startupscript.py
if [[ $? != 0 ]]; then echo "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/set_startupscript.py"; exit ; fi
ipython3 set_startupscript.py
if [[ $? != 0 ]]; then echo "ipython3 set_startupscript.py"; exit ; fi
rm -f set_startupscript.py
if [[ $? != 0 ]]; then echo "rm -f set_startupscript.py"; exit ; fi
wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/ubuntu-18.04-new-os-installations/alias.txt
if [[ $? != 0 ]]; then echo "wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/alias.sh"; exit ; fi
cat alias.txt >> ~/.bashrc
if [[ $? != 0 ]]; then echo "cat alias.txt >> ~/.bashrc"; exit ; fi
source ~/.bashrc 
sudo mkdir /amir_bin/
echo 'PATH="/amir_bin/:$PATH"' >> ~/.bashrc ; source  ~/.bashrc
if [[ $? != 0 ]]; then echo "source ~/.bashrc "; exit ; fi
rm -f alias.txt
if [[ $? != 0 ]]; then echo "rm -f alias.txt"; exit ; fi
pip3 install youtube-dl
if [[ $? != 0 ]]; then echo "pip3 install youtube-dl"; exit ; fi

pip3 install xlrd==1.2.0
if [[ $? != 0 ]]; then echo "pip3 install xlrd==1.2.0"; exit ; fi

pip3 install bs4
if [[ $? != 0 ]]; then echo "pip3 install bs4"; exit ; fi
pip3 install lxml
if [[ $? != 0 ]]; then echo "pip3 install lxml"; exit ; fi
pip3 install selenium
if [[ $? != 0 ]]; then echo "pip3 install selenium"; exit ; fi
pip3 install tabulate
if [[ $? != 0 ]]; then echo "pip3 install tabulate"; exit ; fi
pip3 install pandas
if [[ $? != 0 ]]; then echo "pip3 install pandas"; exit ; fi
pip3 install sklearn 
if [[ $? != 0 ]]; then echo "pip3 install sklearn " ; fi
pip3 install pandas_profiling 
if [[ $? != 0 ]]; then echo "pip3 install pandas_profiling " ; fi
pip3 install clipboard 
if [[ $? != 0 ]]; then echo "pip3 install clipboard " ; fi
pip3 install termcolor
if [[ $? != 0 ]]; then echo "pip3 install termcolor" ; fi
pip3 install tqdm
if [[ $? != 0 ]]; then echo "pip3 install tqdm"; exit ; fi
curl -fsSL https://get.docker.com -o get-docker.sh
if [[ $? != 0 ]]; then echo "curl -fsSL https://get.docker.com -o get-docker.sh"; exit ; fi
sudo sh get-docker.sh
if [[ $? != 0 ]]; then echo "sudo sh get-docker.sh"; exit ; fi
wget wget https://raw.githubusercontent.com/amirsaleem1990/git/master/github%20initial%20setup
bash 'github initial setup'
