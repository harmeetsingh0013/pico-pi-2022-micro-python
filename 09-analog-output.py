from machine import PWM,Pin
from time import sleep

outPin = 16
analogOut = PWM(Pin(outPin))
analogOut.freq(1000)
analogOut.duty_u16(0)

while True:
    myVoltage = float(input('What voltage would you like? : '))
    pwmValue = (65536 / 3.3) * myVoltage
    analogOut.duty_u16(int(pwnVal))
    sleep(.1)