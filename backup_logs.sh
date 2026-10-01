#!/bin/bash

# Define variables
LOG_DIR="/home/ubuntu/fastapi-backend/logs"
BACKUP_DIR="/home/ubuntu/backups"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="${BACKUP_DIR}/logs_backup_${TIMESTAMP}.tar.gz"

# Check if the backup directory exists. If not, create it.
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Creating backup directory at $BACKUP_DIR..."
    mkdir -p "$BACKUP_DIR"
fi

# Create the compressed backup
echo "Starting backup of $LOG_DIR..."
tar -czf "$BACKUP_FILE" "$LOG_DIR"

# Check if the tar command succeeded
if [ $? -eq 0 ]; then
    echo "Backup successfully created: $BACKUP_FILE"
    exit 0
else
    echo "Error: Backup failed!"
    exit 1
fi
