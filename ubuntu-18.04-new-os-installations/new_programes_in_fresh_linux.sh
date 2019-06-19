sudo apt install -y curl
sudo apt install -y ipython3
sudo apt install -y python3-pip

wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add - && sudo apt-get install apt-transport-https && echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install -y sublime-text

sudo apt-get -y install vokoscreen

sudo apt -y install git

sudo apt install -y speedtest-cli

sudo apt-get install -y gdebi
wget download.opensuse.org/repositories/home:/colomboem/xUbuntu_16.04/amd64/dukto_6.0-1_amd64.deb
sudo gdebi dukto_6.0-1_amd64.deb
rm -r dukto_6.0-1_amd64.deb


sudo apt-get update && sudo snap install vlc

sudo apt-get -u install pinta


wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf - && ~/.dropbox-dist/dropboxd
sudo apt install -y nautilus-dropbox


sudo apt install -y apt-transport-https software-properties-common
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
sudo apt-get update
sudo apt install -y r-base-core

sudo apt install tmux

sudo apt-get install openjdk-11-jdk
sudo apt-get -y install r-cran-rjava
sudo R CMD javareconf

sudo apt-get install -y libcurl4-openssl-dev
sudo apt-get install -y libxml2-dev
sudo apt-get install -y libssl-dev


sudo Rscript r_essential_packages.R

# to work my alis <copyto>
sudo apt install xsel

#jupyter
sudo apt install -y jupyter-notebook
sudo pip3 install jupyterlab
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
wget https://raw.githubusercontent.com/amirsaleem1990/Linux/master/alias.txt
cat alias.txt >> ~/.bashrc
source ~/.bashrc 
rm -f alias.txt
