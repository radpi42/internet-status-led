import time
from gpiozero import LED
import os
import urllib.request

r_sand = LED(6)
r_pihole = LED(13)
g_phone = LED(19)
y_blkbox = LED(26)

def check():
    try:
        result = urllib.request.urlopen("http://www.google.com").geturl()
        return True
    except:
        return False  

while True:
    while check() == True:
        print('connected')
        r_sand.on()
        time.sleep(1)
        r_sand.off()
        time.sleep(1)
    else:
        r_sand.off()
        print('No connection')
        time.sleep(2)


    


# def ping_pihole(192.168.2.112):
#      return not os.system('ping %s -n 1' % (address,))
# 
