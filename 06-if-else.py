from machine import Pin
import time

led = Pin(15, Pin.OUT)
while True:
    CMD = input('What is your command? (ON/OFF/TOGGLE): ')
    if CMD == 'ON':
        led.value(1)
    if CMD == 'OFF':
        led.value(0)
    if CMD == 'TOGGLE':
        led.toggle()