from machine import Pin
import utime as time
from dht import DHT11

dataPin = 16

myPin = Pin(dataPin, Pin.OUT, Pin.PULL_DOWN)
time.sleep(3)
sensor = DHT11(myPin)

print('My Sensor Data')
while True:
    sensor.measure()
    tempC = sensor.temperature()
    hum = sensor.humidity()
    print("\r", tempC, hum, end = '')
    time.sleep(1)