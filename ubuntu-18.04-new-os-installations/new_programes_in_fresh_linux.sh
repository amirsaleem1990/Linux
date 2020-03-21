#!/bin/bash
sudo apt-get update
sudo apt-get upgrade

sudo apt install -y ipython3
sudo apt install -y python3-pip

sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo add-apt-repository "deb https://download.sublimetext.com/ apt/stable/"
sudo apt update
sudo apt install sublime-text

sudo apt-get -y install vokoscreen
sudo apt -y install git
sudo apt install -y speedtest-cli
sudo snap install vlc
sudo apt-get -y install pinta
sudo apt install -y nautilus-dropbox

sudo apt-get install -y gdebi
wget download.opensuse.org/repositories/home:/colomboem/xUbuntu_16.04/amd64/dukto_6.0-1_amd64.deb
sudo gdebi dukto_6.0-1_amd64.deb
rm -r dukto_6.0-1_amd64.deb



sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo apt update
sudo apt install -y r-base r-base-core r-recommended

sudo apt install -y tmux

sudo apt-get -y install openjdk-11-jdk
sudo apt-get -y install r-cran-rjava
sudo R CMD javareconf

sudo apt-get install -y libcurl4-openssl-dev
sudo apt-get install -y libxml2-dev
sudo apt-get install -y libssl-dev

sudo Rscript r_essential_packages.R

# to work my alis <copyto>
sudo apt install xsel

#jupyter
sudo apt install -y jupyter-core
pip3 install jupyterlab
sudo apt-get install -y jupyter-client
sudo Rscript R_in_jupyter.R

# gopen
sudo apt install -y gnustep-gui-runtime

#rstudio
curl https://download1.rstudio.org/desktop/bionic/amd64/rstudio-1.2.1335-amd64.deb > rstudio.deb
sudo gdebi -n rstudio*.deb


# start-up applications
wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/set_startupscript.py
ipython3 set_startupscript.py
rm -f set_startupscript.py

# add aliases to .bashrc file
wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/alias.sh
cat alias.txt >> ~/.bashrc
source ~/.bashrc 
rm -f alias.txt




sudo apt install -y nethogs
sudo apt install -y tree
sudo apt install -y gdebi-core
sudo apt install -y ffmpeg
sudo apt install -y xsel
pip3 install youtube-dl
pip3 install bs4
pip3 install lxml
pip3 install selenium
pip3 install tabulate
pip3 install pandas
pip3 install sklearn pandas_profiling clipboard tqdm



sudo apt install -y translate-shell
