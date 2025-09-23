from machine import Pin
from time import sleep

buttonPin = 13
ledPin = 15

ledState = False;
oldButtonState = 1
currentButtonState = 1

myButton = Pin(buttonPin, Pin.IN, Pin.PULL_UP)
myLed = Pin(ledPin, Pin.OUT)

while True:
    buttonStateNew = myButton.value()
    
    
    if( buttonStateNew == 1 and oldButtonState == 0):
        ledState = not ledState
        myLed.value(ledState)
        
    print(ledState, buttonStateNew)
    oldButtonState = buttonStateNew
    sleep(.1)
