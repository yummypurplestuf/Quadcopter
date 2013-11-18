"""
Continuously read the serial port and process IO data received from a remote XBee.
"""

from xbee import XBee
from serial import Serial

ser = Serial('/dev/tty.usbserial-A7025WZO', 9600)				# Xbee labeled "B"

xbee = XBee(ser)

print ""
print "Connected to Xbee: B"

# Continuously send "Hello, World!"
while True:
    try:
    	# Send the string 'Hello World' to the module with MY set to 1
		xbee.tx(dest_addr= '\x00\x01', data='Hello, World')   
    except KeyboardInterrupt:
        break

print "break"
ser.close()