#!/bin/bash

# Set Python virtual environment path
python=venv/bin/python

# Check if the virtual environment exists, if not, create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip & install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Run scripts
$python get_config.py && $python bot.py
