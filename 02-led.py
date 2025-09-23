from machine import Pin
from time import sleep

redLED = Pin(15, Pin.OUT)
while True:
    redLED.value(1)
    sleep(0.5)
    redLED.value(0)
    sleep(0.5)