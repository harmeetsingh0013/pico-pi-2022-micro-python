import machine
from time import sleep
from machine import Pin

potPin = 28
myPot = machine.ADC(potPin)

red = Pin(15, Pin.OUT)
yellow = Pin(12, Pin.OUT)
green = Pin(13, Pin.OUT)

while True:
    potVal = myPot.read_u16()
    #myValue = int( (potVal / 65536) * 100)
    myValue = (100/65376) * potVal - (160 * 100 / 65376)
    
    print(myValue)
    
    if(myValue <= 79):
        red.value(0)
        yellow.value(0)
        green.value(1)
    if(myValue >=80 and myValue <= 94):
        red.value(0)
        yellow.value(1)
        green.value(0)
    if(myValue >= 95):
        red.value(1)
        yellow.value(0)
        green.value(0)
    sleep(.5) 