from machine import Pin
from time import sleep

redLedPin = 26
greedLedPin = 27
blueLedPin = 28

myRedLed = Pin(redLedPin, Pin.OUT)
myGreenLed = Pin(greedLedPin, Pin.OUT)
myBlueLed = Pin(blueLedPin, Pin.OUT)

redButtonPin = 10
greenButtonPin = 11
blueButtonPin = 13

myRedButton = Pin(redButtonPin, Pin.IN, Pin.PULL_UP)
myGreenButton = Pin(greenButtonPin, Pin.IN, Pin.PULL_UP)
myBlueButton = Pin(blueButtonPin, Pin.IN, Pin.PULL_UP)

redButtonStateNow = 1
greenButtonStateNow = 1
blueButtonStateNow = 1

redButtonStateOld = 1
greenButtonStateOld = 1
blueButtonStateOld = 1

redLedState = False
greenLedState = False
BlueLedState = False

while True:
    redButtonStateNow = myRedButton.value()
    greenButtonStateNow = myGreenButton.value()
    blueButtonStateNow = myBlueButton.value()
    
    if redButtonStateOld == 0 and redButtonStateNow == 1:
        redLedState = not redLedState
        myRedLed.value(redLedState)
        print("Red Button: ", redButtonStateNow)
        
    redButtonStateOld = redButtonStateNow
    
    if greenButtonStateOld == 0 and greenButtonStateNow == 1:
        greenLedState = not greenLedState
        myGreenLed.value(greenLedState)
        print("Green Button: ", greenButtonStateNow)
        
    greenButtonStateOld = greenButtonStateNow
    
    if blueButtonStateOld == 0 and blueButtonStateNow == 1:
        BlueLedState = not BlueLedState
        myBlueLed.value(BlueLedState)
        print("Blue Button: ", blueButtonStateNow)
        
    blueButtonStateOld = blueButtonStateNow
    sleep(.1)
