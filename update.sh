#!/bin/bash

# sourcing directories and IP addresses from .env file
source .env

# List of Raspberry Pi IP addresses
# RASPBERRY_PI_IPS is a space-separated string, like this:
# RASPBERRY_PI_IPS = "192.168.1.10 192.168.1.11 192.168.1.12"
IFS=' ' read -r -a RASPBERRY_PI_IPS <<< "$RASPBERRY_PI_IPS"

# Make sure that your .env file also contains both PROJECT_DIR and DEST_DIR
# PROJECT_DIR is the code on your machine
# DEST_DIR is the directory where the code lives on your raspberry pi
# DEST_DIR will likely just be "/home/pi"

for ip in "${RASPBERRY_PI_IPS[@]}"; do
    echo "Deploying to Raspberry Pi at $ip"
    scp -r $PROJECT_DIR pi@$ip:$DEST_DIR
done

echo "Deployment complete"