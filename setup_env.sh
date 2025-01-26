#!/bin/bash

# Check if pyenv is installed
if ! command -v pyenv &> /dev/null
then
    echo "pyenv could not be found. Please install pyenv first."
    exit
fi

# Set the Python version and virtual environment name
PYTHON_VERSION=3.10.0
VENV_NAME=stream

# Install the specified Python version if not already installed
if ! pyenv versions --bare | grep -q "^$PYTHON_VERSION$"; then
    pyenv install $PYTHON_VERSION
fi

# Create the virtual environment if it doesn't exist
if ! pyenv virtualenvs --bare | grep -q "^$VENV_NAME$"; then
    pyenv virtualenv $PYTHON_VERSION $VENV_NAME
fi

# Set the local pyenv version to the virtual environment
pyenv local $VENV_NAME

# Install the dependencies
pip install -r requirements.txt

echo "Virtual environment setup complete. To activate, run 'pyenv activate $VENV_NAME'"