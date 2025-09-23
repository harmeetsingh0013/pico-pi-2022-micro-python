from machine import Pin, PWM
from time import sleep

redPin = 13
greenPin = 14
bluePin = 15

redLED = PWM(Pin(redPin))
greenLED = PWM(Pin(greenPin))
blueLED = PWM(Pin(bluePin))

redLED.freq(1000)
redLED.duty_u16(0)

greenLED.freq(1000)
greenLED.duty_u16(0)

blueLED.freq(1000)
blueLED.duty_u16(0)

while True:
    redBrightness = 0 # values in between 0 to 65550
    greenBrightness = 0 # values in between 0 to 65550
    blueBrightness = 0 # values in between 0 to 65550
    
    redLED.duty_u16(redBrightness)
    greenLED.duty_u16(greenBrightness)
    blueLED.duty_u16(blueBrightness)
    
    sleep(.1)