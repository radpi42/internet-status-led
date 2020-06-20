from gpiozero import LED, PingServer
from gpiozero.tools import negated
from signal import pause
import socket
import os

def pingip():
    testIP = "8.8.8.8"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((testIP, 0))
    ipaddr = s.getsockname()[0]
    host = socket.gethostname()
    print ("IP:", ipaddr, " Host:", host)

connected = LED(18)
no_internet = LED(2)

ping = pingip()



connected.source = ping
connected.source_delay = 1.5
no_internet.source = negated(connected)


pause()