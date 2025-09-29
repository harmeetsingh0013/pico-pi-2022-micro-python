import socket
import time
import network

import machine

from machine import Pin

redLEDPin = 13
greenLEDPin = 14
blueLEDPin = 15

redLed = Pin(redLEDPin, Pin.OUT)
greenLed = Pin(greenLEDPin, Pin.OUT)
blueLed = Pin(blueLEDPin, Pin.OUT)

redLed.value(0)
greenLed.value(0)
blueLed.value(0)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect('wifiname', 'wifipassword')

while wifi.isconnected == False:
    print('Waitng for connection...')
    time.sleep(1)
    
wifiInfo = wifi.ifconfig()
print(wifiInfo)

rssi_value = wifi.status('rssi')
print(f'Wi-Fi RSSI: {rssi_value} dBm')
print("------------------------------")

ServerIP = wifiInfo[0]
ServerPort = 2222

bufferSize = 1024 # bytes
UDPServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServer.bind((ServerIP, ServerPort))
print('UDPServer is up and waiting ...')

while True:
    message, address = UDPServer.recvfrom(bufferSize)
    messageDecoded = message.decode('utf-8')
    
    if messageDecoded == 'RED':
        redLed.value(1)
        greenLed.value(0)
        blueLed.value(0)
    elif messageDecoded == 'GREEN':
        redLed.value(0)
        greenLed.value(1)
        blueLed.value(0)
    elif messageDecoded == 'BLUE':
        redLed.value(0)
        greenLed.value(0)
        blueLed.value(1)
    else:
        redLed.value(0)
        greenLed.value(0)
        blueLed.value(0)
    dataString = 'Your ' + messageDecoded + ' light is on'
    dataStringEncoded = dataString.encode('utf-8')
    print(dataStringEncoded)
    UDPServer.sendto(dataStringEncoded, address)


