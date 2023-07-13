#!/bin/bash

if [ "$1" = "--play" ]; then
    python main.py
else
    # Default behavior, do something else or show an error message
    echo "Invalid command. Please use '--play' to execute the GUI script."
fi
