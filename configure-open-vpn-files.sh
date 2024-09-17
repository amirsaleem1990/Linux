#!/bin/bash

# Directory containing the .ovpn files
VPN_DIR="/home/amir/Downloads/PP"

# VPN credentials (hardcoded for VPNBook)
USERNAME="vpnbook"
PASSWORD="k8bx52n"

Find all .ovpn files in the directory
OVPN_FILES=($(find "$VPN_DIR" -name "*.ovpn"))

if [ ${#OVPN_FILES[@]} -eq 0 ]; then
    echo "No .ovpn files found in $VPN_DIR"
    exit 1
fi

# # Specific OVPN file to use
# OVPN_FILE="/home/amir/Downloads/VPNBOOK_2/vpnbook-us1-udp53.ovpn"

# Loop through each .ovpn file
for OVPN_FILE in "${OVPN_FILES[@]}"; do

    # Extract the VPN name from the filename (assuming filename format is 'vpn_name.ovpn')
    VPN_NAME="${OVPN_FILE##*/}" 
    VPN_NAME="${VPN_NAME%.ovpn}"

    echo "Importing and connecting to VPN: $VPN_NAME"

    # Use nmcli to import the connection
    nmcli connection import type openvpn file "$OVPN_FILE"

    # If the import was successful, modify with username and password
    if [ $? -eq 0 ]; then
        nmcli connection modify "$VPN_NAME" vpn.user-name "$USERNAME" vpn.secrets "password=$PASSWORD"
        
        # Attempt to bring up the connection
        nmcli connection up "$VPN_NAME"
        
        # Check if the connection was successful
        if [ $? -ne 0 ]; then
            echo "Failed to connect to VPN: $VPN_NAME"
            
            # Provide guidance if connection fails
            echo "Please check for authentication issues. Ensure the username and password are correct."
        else
            echo "Connected to VPN: $VPN_NAME successfully."
        fi
    else
        echo "Failed to import VPN connection: $VPN_NAME"
    fi
done