#/bin/bash

# Code to remove all existing VPN connections.
# List all VPN connections (both active and inactive)
vpn_connections=$(nmcli connection show | grep vpn | awk '{print $1}')

# Check if any VPN connections exist
if [ -z "$vpn_connections" ]; then
    echo "No VPN connections found."
else
    # Loop through each VPN connection and delete it
    for connection in $vpn_connections; do
        echo "Removing VPN connection: $connection"
        nmcli connection delete "$connection"
    done
    echo "All VPN connections have been removed."
fi
