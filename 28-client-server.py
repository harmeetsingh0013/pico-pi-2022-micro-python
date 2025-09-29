import socket
import time
import network

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
    print('Message Received: ', messageDecoded, 'From: ', address[0])
    dataString = 'Received your command: ' + messageDecoded
    dataStringEncoded = dataString.encode('utf-8')
    print(dataStringEncoded)
    UDPServer.sendto(dataStringEncoded, address)