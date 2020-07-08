from time import sleep
import subprocess


#VARIABLES OF WHAT WE NEED

#Names of devices on network
names = ["Colorbox","dud"]

# MAC addresses of devices make sure they are in the same order as the names
macs = ["b8:27:eb:cc:e4:a4","xx:xx:xx:xx:xx:xx"]

#how many times run
counter_mes = '''times run: %d'''
count = 0


#functions
#first up is the scan itself.

def arp_scan():
        output = subprocess.check_output("sudo arp-scan -l", shell=True)
        arr = str(output, 'utf-8')
        for i in range(len(names)):
                if macs[i] in arr:
                        print(names[i] + " is present")
                else:
                        print(names[i] + " is NOT present")
# the above runs the arp-scan and checks the results (after they are converted to a string for python3) then prints out whos online


#and the program itself

while True:
    print("starting scan")
    arp_scan()
    sleep(1)
    print("scan complete")
    count =+1
    print(counter_mes %count)
    print("sleeping until next scan")
    sleep(30)
