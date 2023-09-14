#!/bin/bash

# sourcing directories and IP addresses from .env file
source .env

# List of Raspberry Pi IP addresses
IFS=' ' read -r -a RASPBERRY_PI_IPS <<< "$RASPBERRY_PI_IPS"

# Make sure that your .env file contains both PROJECT_DIR and DEST_DIR

# PROJECT_DIR is a space-separated string, like this:
# RASPBERRY_PIS="192.168.1.10 192.168.1.11 192.168.1.12"

# DEST_DIR will likely just be "/home/pi"

for ip in "${RASPBERRY_PI_IPS[@]}"; do
    echo "Deploying to Raspberry Pi at $ip"
    scp -r $PROJECT_DIR pi@$ip:$DEST_DIR
done

echo "Deployment complete"