"""
Continuously read the serial port and process IO data received from a remote XBee.
"""

# This version is for the pi

import time
from xbee import XBee
from serial import Serial

ser = Serial('/dev/xbee', 57600)

xbee = XBee(ser)

# Continuously send
while True:
    try:
        ser.write("testing API")
        time.sleep(.125)

    except KeyboardInterrupt:
        break
        
ser.close()