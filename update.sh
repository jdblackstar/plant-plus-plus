#!/bin/bash

# List of Raspberry Pi IP addresses
RASPBERRY_PIS=(
    "192.168.1.10"
    "192.168.1.11"
    "192.168.1.12"
)

# Directory containing your project on your local machine
PROJECT_DIR="/path/to/your/project"

# Directory where you want to copy your project on the Raspberry Pi
DEST_DIR="/home/pi/"

for ip in "${RASPBERRY_PIS[@]}"; do
    echo "Deploying to Raspberry Pi at $ip"
    scp -r $PROJECT_DIR pi@$ip:$DEST_DIR
done

echo "Deployment complete"