# run script as super user (e.g. $ sudo python3 sendlora.py)
import serial

with serial.Serial('/dev/serial0', 115200, timeout=10) as ser:
    ser.write(b'send')

print("Data Sent")
