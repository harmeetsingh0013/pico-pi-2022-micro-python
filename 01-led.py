from machine import Pin
from time import sleep

myLED=Pin('LED', Pin.OUT)
while True:
    myLED.on()
    sleep(.01)
    myLED.off()
    sleep(.02)