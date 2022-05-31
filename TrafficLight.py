#TraficLightPi.py
from gpiozero import LED
from time import sleep
from ping3 import ping
from threading import Thread

### set your variables here
# addresses to ping
redAddress = "google.com"
yellowAddress = "aws.amazon.com"
greenAddress = "192.168.1.1"
# wait this many seconds between pings
timeBetweenPings = 60
# GPIO pins for each light
red = LED(17)
yellow = LED(22)
green = LED(27)

### functions
# ping test
def diditping(ipaddress):
    tryping = ping(ipaddress)
    if tryping == False:
        return False
    else:
        return True
# lamp test
def lamptest():
    red.on()
    sleep(.5)
    yellow.on()
    sleep(.5)
    green.on()
    sleep(.5)
    sleep(1)
    red.off()
    sleep(.5)
    yellow.off()
    sleep(.5)
    green.off()
    sleep(.5)

### main loop
def main_loop():
    r = blinkred()
    y = blinkyellow()
    g = blinkgreen()
    if diditping(redAddress) == False:
        r.start()
    else:
        red.on()
    if diditping(yellowAddress) == False:
        y.start()
    else:
        yellow.on()
    if diditping(greenAddress) == False:
        g.start()
    else:
        green.on()
    sleep(timeBetweenPings)
    r.stop()
    y.stop()
    g.stop()

### threads
# blink red
class blinkred(Thread):
    def __init__(self):
        super(blinkred, self).__init__()
        self._keepgoing = True
    def run(self):
        while (self._keepgoing):
            print('Blinking Red')
            red.on()
            sleep(1)
            red.off()
            sleep(.25)
    def stop(self):
        self._keepgoing = False
# blink yellow
class blinkyellow(Thread):
    def __init__(self):
        super(blinkyellow, self).__init__()
        self._keepgoing = True
    def run(self):
        while (self._keepgoing):
            print('Blinking Yellow')
            yellow.on()
            sleep(1)
            yellow.off()
            sleep(.25)
    def stop(self):
        self._keepgoing = False
# blink green
class blinkgreen(Thread):
    def __init__(self):
        super(blinkgreen, self).__init__()
        self._keepgoing = True
    def run(self):
        while (self._keepgoing):
            print('Blinking Green')
            green.on()
            sleep(1)
            green.off()
            sleep(.25)
    def stop(self):
        self._keepgoing = False

### RUNTIME
# run lamp test once on startup
lamptest()
# run main loop forver
while True:
    main_loop()
