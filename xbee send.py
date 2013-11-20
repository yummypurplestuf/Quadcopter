"""
Continuously send data.
"""

"""
Todo:
learn about ser.isOpen()
learn to program xbee using pyserial




"""


from xbee import XBee
from serial import Serial
import time

alive = True
while alive == True:
	while True:
		try:
			# Xbee labeled "A"
			ser = Serial('/dev/tty.usbserial-A7025WZ6', 9600)
			print ""
			print "Connected to Xbee: A"	
			xbee = XBee(ser)
			ser_init = True
			break
		except OSError:
				print "Please connect the correct Xbee"
				

	# Continuously send "Hello, World!"
	while ser_init == True:
	    try:
	    	# Send the string 'Hello World' to the module with MY set to 1
			xbee.tx(dest_addr= '\x00\x01', data='Hello, World')
			# Delays the message from sending
			time.sleep(3)
	    except NameError:
	    	pass
	    except IOError:
	    	ser_init = False
	    except KeyboardInterrupt:
	        alive = False
	        break

ser.close()