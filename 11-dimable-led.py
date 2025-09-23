import machine
from machine import Pin, PWM
from time import sleep

potPin = 28
myPot = machine.ADC(potPin)

outPin = 16
analogOut = PWM(Pin(outPin))
analogOut.freq(1000)
analogOut.duty_u16(0)

while True:
    potVal = myPot.read_u16()
    expVal = (50 / 65520) * potVal
    brightness = (1.248336) ** expVal
    #myVoltage = (3.3/65376) * potVal - (160 * 3.3 / 65376)
    print('My expVal: ', potVal, expVal, brightness)
   # pwmValue = (65536 / 3.3) * myVoltage
    analogOut.duty_u16(int(brightness))
    sleep(.1)