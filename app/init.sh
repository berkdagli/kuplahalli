#!/bin/bash

export FLASK_APP=/home/pi/Desktop/kuplahalli/main.py
export FLASH_ENV=development
python3 -m flask run --host=0.0.0.0
