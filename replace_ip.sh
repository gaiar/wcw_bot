#!/bin/bash

# Define the file path, backup path, and IP addresses
CONFIG_FILE="config.yaml"
BACKUP_FILE="config.yaml.bak"
OLD_IP="46.128.211.233"
NEW_IP="5.28.64.136"

# Check if the config.yaml file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: $CONFIG_FILE does not exist."
    exit 1
fi

# Create a backup of the config.yaml file
cp "$CONFIG_FILE" "$BACKUP_FILE"
if [ $? -ne 0 ]; then
    echo "Error: Failed to create backup of $CONFIG_FILE."
    exit 1
fi

# Use sed to replace the old IP with the new IP
sed -i "s/$OLD_IP/$NEW_IP/g" "$CONFIG_FILE"

# Print a success message
echo "Replaced $OLD_IP with $NEW_IP in $CONFIG_FILE. Backup saved as $BACKUP_FILE."
