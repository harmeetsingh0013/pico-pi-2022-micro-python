import machine
from time import sleep

potPin = 28
myPot = machine.ADC(potPin)

while True:
    potVal = myPot.read_u16()
    voltage = (3.3/65106) * potVal - (192 * 3.3 / 65106)
    print(voltage)
    sleep(.5) 