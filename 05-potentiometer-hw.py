import machine
from time import sleep

potPin = 28
myPot = machine.ADC(potPin)

while True:
    potVal = myPot.read_u16()
    voltage = (3.3/65376) * potVal - (160 * 3.3 / 65376)
    print(voltage)
    sleep(.5) 
