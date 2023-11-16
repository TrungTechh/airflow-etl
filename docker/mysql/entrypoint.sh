#!/bin/bash

# Define variables
CONTAINER_NAME="mysql"
MYSQL_USER="root"
MYSQL_PASSWORD="root"
DATABASE_NAME="bike_store"

# Check if a folder path is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <data_folder_name>"
    exit 1
fi

# Get the absolute path to the script's directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Assuming the data folder is a sibling to the docker folder
HOST_DATA_FOLDER="$SCRIPT_DIR/../bike_store_data/$1"
INIT_SQL_PATH="$SCRIPT_DIR/mysql/init.sql"
CONTAINER_DATA_PATH="/tmp/"

# Copy data folder and init.sql to the Docker container
ABSOLUTE_HOST_DATA_FOLDER="$(realpath "$HOST_DATA_FOLDER")"
ABSOLUTE_HOST_DATA_INIT_SQL="$(realpath "$INIT_SQL_PATH")"
docker cp "$ABSOLUTE_HOST_DATA_FOLDER" "$CONTAINER_NAME:$CONTAINER_DATA_PATH"
docker cp "$ABSOLUTE_HOST_DATA_INIT_SQL" "$CONTAINER_NAME:$CONTAINER_DATA_PATH/init.sql"

# Load data into MySQL table
docker exec -i "$CONTAINER_NAME" bash -c \
  "mysql --local-infile=1 -u$MYSQL_USER -p$MYSQL_PASSWORD $DATABASE_NAME -e \"source $CONTAINER_DATA_PATH/init.sql;\""

