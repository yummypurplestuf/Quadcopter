"""
Continuously read the serial port and process IO data received from a remote XBee.
"""

# This version is for the pi

import time
from xbee import XBee
from serial import Serial

ser = Serial('/dev/tty.usbserial-A7025WZ6', 57600)
#ser = Serial('/dev/xbee', 57600)

xbee = XBee(ser)

data = 1
# Continuously send
while data == 1:
    try:
        
        signal = ['up', 'down', 'right', 'left']
        #print signal
        #send = xbee.send("str(signal")
        xbee.send("at", frame="A", command='MY', parameter=None)
        ser.flush()
        #send = ser.writelines("testing API\n")
        time.sleep(.5)
        data += 1
    except KeyboardInterrupt:
        break
        
ser.close()