from machine import Pin
import utime as time
from dht import DHT11

dataPin = 16

myPin = Pin(dataPin, Pin.OUT, Pin.PULL_DOWN)
time.sleep(3) #needs an delays because of DHT11 taking time for initialization
sensor = DHT11(myPin)

toggleButtonPin = 2
myToggleButton = Pin(toggleButtonPin, Pin.IN, Pin.PULL_UP)

toggleButtonStateOld = 1
toggleButtonStateNow = 1

print("Current Temprature")

tempUnitC = True

while True:

        toggleButtonStateNow = myToggleButton.value()
        
        if toggleButtonStateOld == 0 and toggleButtonStateNow == 1:
            try:
                sensor.measure()
            except:
                passb 
            sensor.measure()
            tempC = sensor.temperature()
            hum = sensor.humidity()
            
            if tempUnitC == True:
                print("\r", 'Temp = ', tempC, chr(176) + 'C', 'Humidity = ', hum, '%', end = '')
            if tempUnitC == False:
                tempFr = (tempC * 9/5) + 32
                print("\r", 'Temp = ', tempFr, chr(176) + 'F', 'Humidity = ', hum, '%', end = '')
                 
            tempUnitC = not tempUnitC
            
        toggleButtonStateOld = toggleButtonStateNow
        
        time.sleep(.1)