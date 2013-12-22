"""
Continuously read the serial port and process IO data received from a remote XBee.
"""

from xbee import XBee
from serial import Serial

ser = Serial('/dev/tty.usbserial-A7025WZO', 57600)

xbee = XBee(ser)
# Continuously read and print packets
while ser.isOpen():
    try:
        # message = ser.read()
        # ser.flush()
        # print message
 		print xbee.wait_read_frame()
 		
        #print message
        #flush('/dev/tty.usbserial-A7025WZO')
    except KeyboardInterrupt:
        break
    finally:
        break
ser.close()
