#!/bin/sh

set -e

echo "Installing python3 if it's not installed..."
which python3 || brew install python3

echo "Activating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "Installing python dependencies..."
pip install --upgrade pip
pip install -r requirements-dev.txt