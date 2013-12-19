#/usr/bin/python

from xbee import XBee
from serial import Serial

"""
serial_example.py
By Jared Luellen, 2013

Demonstrates reading the low-order address bits from an XBee Series 1
device over a serial port (USB) in API-mode.
"""
ser = Serial('/dev/tty.usbserial-A7025WZ6', 57600)
xbee = XBee(ser)

def main():
    """
    Sends an API AT command to read the lower-order address bits from 
    an XBee Series 1 and looks for a response
    """
    try:
        
        # Open serial port
        ser = Serial('/dev/tty.usbserial-A7025WZ6', 57600)
        
        # Create XBee Series 1 object
        
        
        dest = '\x00\x01'  
        text = 'send message'
        
        send(dest, text)
        print "Comp: ", convert(dest)
        # Wait for response
        #response = xbee.wait_read_frame()
        #print response
        
        # Send AT packet
        #xbee.send('at', frame_id='A', command='DH')
        #response = xbee.wait_read_frame()
        #print response
        
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()
    

def convert(self, text):
    conv = "".join("%02x" % ord(c) for c in text)
    #print conv
    return conv

def send(self, dest, text):
    self.xbee.tx(dest_addr=dest, data=text)
    # Need to figure out this section
    return


if __name__ == '__main__':
    main()