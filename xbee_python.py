"""
Continuously read the serial port and process IO data received from a remote XBee.
"""

import time
from xbee import XBee
from serial import Serial

ser = Serial('/dev/tty.usbserial-A7025WZO', 57600)

xbee = XBee(ser)

# Continuously read and print packets
while ser.isOpen():
    try:
        #message = str(ser.readline().strip())
        #print bool(message)
        print ser.read()
        #print message
    except KeyboardInterrupt:
        break
        
ser.close()