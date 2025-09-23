from machine import Pin
from time import sleep

led1 = Pin(12, Pin.OUT)
led2 = Pin(13, Pin.OUT)
led3 = Pin(14, Pin.OUT)
led4 = Pin(15, Pin.OUT)

while True:
    sleep(.5)

    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    
    sleep(.5)
    
    led1.value(1)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    
    sleep(.5)

    led1.value(0)
    led2.value(1)
    led3.value(0)
    led4.value(0)
    
    sleep(.5)
    
    led1.value(1)
    led2.value(1)
    led3.value(0)
    led4.value(0)
    
    sleep(.5)
    
    led1.value(0)
    led2.value(0)
    led3.value(1)
    led4.value(0)
    
    sleep(.5)
    
    led1.value(1)
    led2.value(0)
    led3.value(1)
    led4.value(0)
    
    sleep(.5)
    
    led1.value(0)
    led2.value(1)
    led3.value(1)
    led4.value(0)
    
    sleep(.5)
    
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(0)
    
    sleep(.5)
    
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(1)
    
    sleep(.5)
    
    led1.value(1)
    led2.value(0)
    led3.value(0)
    led4.value(1)
    
    sleep(.5)
    
    led1.value(0)
    led2.value(1)
    led3.value(0)
    led4.value(1)
    
    sleep(.5)
    
    led1.value(1)
    led2.value(1)
    led3.value(0)
    led4.value(1)
    
    sleep(.5)
    
    led1.value(0)
    led2.value(0)
    led3.value(1)
    led4.value(1)
    
    sleep(.5)
    
    led1.value(1)
    led2.value(0)
    led3.value(1)
    led4.value(1)
    
    sleep(.5)
    
    led1.value(0)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    
    sleep(.5)
    
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    
    sleep(.5)


