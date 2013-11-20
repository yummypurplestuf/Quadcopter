"""
Continuously read packets
"""

from xbee import XBee
from serial import Serial
import time

alive = True
while alive == True:
	while True:
		try:
			# Xbee labeled "B"
			ser = Serial('/dev/tty.usbserial-A7025WZO', 9600)
			print ""
			print "Connected to Xbee: B"	
			xbee = XBee(ser)
			ser_init = True
			break
		except OSError:
				print "Please connect the correct Xbee"
				
	while ser_init == True:
	    try:
    		# Waits for a message to be recieved and prints it
			print xbee.wait_read_frame()
	    except NameError:
	    	pass
	    except IOError:
	    	ser_init = False
	    except KeyboardInterrupt:
	        alive = False
	        break

ser.close()