#!/bin/sh
# btnlaunch.sh
# navigate to home directory, then to this directory, then execute python script, then back home


cd /
cd home/pi/internet-status-led
sudo python3 networkLED.py
cd /
