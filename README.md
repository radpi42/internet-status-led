# internet-status-led
turns on an LED when connected to local network and internet


to run at start up via crontab use this guide
https://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/


Crontab set up

basically 
step 1
make a start up scrip



##########################

nano networklauncher.sh

###################

#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/internet-status-led
sudo python3 networkLED.py
cd /


###############

then make it excutable:

#command#
chmod 755 networkledlauncher.sh

#Now test it, by typing in:#

sh networkledlauncher.sh

######

Next we need to make a directory for the any errors in crontab to go.

########

this repo has the logs directory already made


next we schedule it in crontab
first enter

crontab -e

Then enter

@reboot sh /home/pi/internet-status-led/netowrkledlauncher.sh >/home/pi/internet-status-led/logs/cronlog 2>&1

now reboot and hope you didnt mess up
