# Create a 32GB file
dd if=/dev/zero of=/media/sdb2/swapfile.img bs=1G count=32

# change permitions
sudo chmod 0600 /media/sdb2/swapfile.img

# Add an entry to fstab file
echo -e "\n/media/sdb2/swapfile.img swap swap sw 0 0" | sudo tee -a /etc/fstab > /dev/null

# make a swap
sudo mkswap /media/sdb2/swapfile.img


# On the swap
sudo swapon  /media/sdb2/swapfile.img

