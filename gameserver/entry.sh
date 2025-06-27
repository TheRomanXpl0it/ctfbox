#!/bin/bash
ip route del default
ip route add default via 10.10.0.250
echo "127.0.0.1 flagid" >> /etc/hosts

# Base directory
BASE_DIR="/app/checkers"

# Find all directories containing checker.py
DIRS=$(find "$BASE_DIR" -type f -name "checker.py" -exec dirname {} \;)

# Loop through each directory
for dir in $DIRS; do
  echo "Processing directory: $dir"

  if [ -f "$dir/venv" ]; then
    echo "Deleting previous venv"
    rm -rf $dir/venv/
  else
    echo "No venv already present, skipping deletion."
  fi

  # Create virtual environment in the directory (in a folder named .venv)
  python3 -m venv "$dir/venv"
  
  # Check if requirements.txt exists and install dependencies
  if [ -f "$dir/requirements.txt" ]; then
    echo "Installing requirements from $dir/requirements.txt"
    $dir/venv/bin/pip install --upgrade pip
    $dir/venv/bin/pip install -r "$dir/requirements.txt"
  else
    echo "No requirements.txt found in $dir, skipping dependency installation."
  fi

done

./ctfserver
