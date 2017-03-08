from machine import UART
import pycom
import time
from network import LoRa
import socket
import binascii
import struct

pycom.heartbeat(False) # turn off heartbeat

uart = UART(1, 115200, bits=8, parity=None, stop=1)
uart.write("Connected...")

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)
app_eui = binascii.unhexlify('AD A4 DA E3 AC 12 67 6B'.replace(' ',''))
app_key = binascii.unhexlify('11 B0 28 2A 18 9B 75 B0 B4 D2 D8 C7 FA 38 54 8B'.replace(' ',''))
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

while not lora.has_joined():
    time.sleep(2.5)
    print('Searching for network...')

print("Connected to the network.")

def send_lora(data):
    print("Sending " + data)
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(True)
    s.send(str(data))
    s.setblocking(False)
    uart.write(b'Success')

while True:
    if uart.any():
        data = uart.readall()
        pycom.rgbled(0xFF0000) # set LED to RED on if data received
        if data == b'send':
            send_lora("data")
            pycom.rgbled(0x00FF00) # set LED to GREEN if data is b'send'
        time.sleep(1)
        pycom.rgbled(0x000000)