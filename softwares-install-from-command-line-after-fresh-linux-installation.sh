cd ~ 
# vlc
sudo apt-get update && sudo snap install vlc

# pinta
sudo apt-get update &&  sudo apt-get install pinta 

# dropbox
sudo apt-get update &&  wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf - && ~/.dropbox-dist/dropboxd && sudo apt install nautilus-dropbox

# sublime
sudo apt-get update &&  wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add - && sudo apt-get install apt-transport-https && echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list && sudo apt-get update && sudo apt-get install sublime-text


# conda R envoirment
sudo apt-get update &&  conda create -n Renv r-essentials mro-base && echo "***********************Renv envoirment created seccussfully********************" && source activate Renv && echo "********************Renv activated Succussfully********************" && conda install -c r r-dplyr && echo "********************dplyr installed Succussfully********************" && conda install -c r rstudio && echo "********************rstudio installed Succussfully********************"



# vokoscreen
sudo apt-get update &&  sudo apt-get install vokoscreen

# github
sudo apt update && sudo apt install git



# speedtest
sudo apt install speedtest-cli


# dukto
sudo apt-get install gdebi
wget download.opensuse.org/repositories/home:/colomboem/xUbuntu_16.04/amd64/dukto_6.0-1_amd64.deb
gdebi dukto_6.0-1_amd64.deb

