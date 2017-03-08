# LoPy-RaspberryPi
Use a Raspberry Pi to control a LoPy over UART

# Instructions

**Before you do anything** configure the LoRaWAN App_Key and App_EUI in the lopy/main.py file.

1. Connect the RPi (pins TX:14, RX:15) via UART to the LoPy using the expansion board (pins TX:G11, RX:G24)
  - Note, we are using the UART 1 interface on the LoPy, this refers to pins P3/P4 or G11/G24 on the expansion board
2. Ensure that the both the RPi and LoPy are powered.
3. Upload the lopy/main.py script to the LoPy and reboot it via the button on the device.
4. Run sendlora.py on the Raspberry Pi (ensure you have python and pyserial installed, $ pip instal pyserial)
  - Note, you should run sendlora.py as superuser ($ sudo python3 sendlora.py)
5. You can change the data in the sendlora.py script to send various payloads between the devices
