"""
Continuously read the serial port and process IO data received from a remote XBee.
"""

# This version is for the pi

import time
from xbee import XBee
from serial import Serial

ser = Serial('/dev/xbee', 9600)

xbee = XBee(ser)

# Continuously send
i = 0
while True:
    try:
        for i in range(1):
	        ser.write(str(i))
	        print i
	        time.sleep(.125)

    except KeyboardInterrupt:
        break
        
ser.close()