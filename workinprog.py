import time
from gpiozero import LED
import subprocess
import urllib.request

# LED variables

r_sand = LED(6)
r_pihole = LED(13)
g_internet = LED(26)
y_blkbox = LED(19)
running = LED(21)

#local device address as variables

blkbox = "192.168.2.110"
colorbox = "192.168.2.112"


#command to find raspberry pis via ping

blkbox_c = ['ping', "-c", '5', blkbox]
colorbox_c = ['ping', "-c", '5', colorbox]

#function to check for Pis via ping


def checkblkbox():
    try:
        blkbox_res = subprocess.run(blkbox_c, capture_output=False)
        return True
    except:
        return False
    
def checkcolorbox():
    try:
        colorbox_res = colorbox_res = subprocess.run(colorbox_c, capture_output=False)
        return True
    except:
        return False


#this is the function that checks if you can reach google and sets a variable as true or false
    

def checkgoog():
    try:
        r_goog = urllib.request.urlopen("http://www.google.com").geturl()
        return True
    except:
        return False


#THECODE

while True:
    running.on()
    if checkcolorbox() == True:
        print("Pihole online")
        r_pihole.on()
        time.sleep(2)   
    else:
        r_pihole.off()
        print('could not connect to pihole')
        time.sleep(2)
    
    if checkblkbox() == True:
        print("blackbox online")
    
    else:
        print('could not connect to blackbox')
    
    if checkgoog() == True:
        print("Internet Connection Established")
        g_internet.on()
        time.sleep(2)
        
    else:
        g_internet.off()
        print('no internet')
        time.sleep(2)

