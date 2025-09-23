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
    print("")
    print("Please select any color?")
    color = input("RED, GREEN, BLUE, MEGENTA, YELLOW, CYAN, ORANGE, WHITE: ")
    
    if color == 'RED':
        redBright = 65550
        greenBright = 0
        blueBright = 0
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
        
    if color == 'GREEN':
        redBright = 0
        greenBright = 65550
        blueBright = 0
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
        
    if color == 'BLUE':
        redBright = 0
        greenBright = 0
        blueBright = 65550
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
        
    if color == 'MAGENTA':
        redBright = 65550
        greenBright = 0
        blueBright = 65550
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
        
    if color == 'CYAN':
        redBright = 0
        greenBright = 65550
        blueBright = 65550
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
        
    if color == 'YELLOW':
        redBright = 65550
        greenBright = 65550
        blueBright = 0
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
        
    if color == 'ORANGE':
        redBright = 65550
        greenBright = 5000
        blueBright = 0
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
        
    if color == 'WHITE':
        redBright = 65550
        greenBright = 65550
        blueBright = 65550
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        blueLED.duty_u16(blueBright)
        
    sleep(.1)