#!/usr/bin/python

# This is a simple demo to remotely turn a LED on and off
# 2011-02-11 Harald Kubota

import serial
from xbee import ZigBee
import time

PORT='/dev/ttyUSB0'
BAUD_RATE=9600
ser = serial.Serial(PORT, BAUD_RATE)

# ZB XBee here. If you have Series 1 XBee, try XBee(ser) instead
xbee=ZigBee(ser)

#MAC, number written on the back of the XBee module
# CO3 = my coordinator
# EP1 = my endpoint with the LED on pin 11
device={
        "CO3":'\x00\x13\xa2\x00\x40\x52\x8d\x8a',
        "EP1":'\x00\x13\xa2\x00\x40\x4a\x61\x84'
}
#64 bit address
led=False

#change remote device function
xbee.remote_at(dest_addr_long=device["EP1"],command='D2',parameter='\x02')
xbee.remote_at(dest_addr_long=device["EP1"],command='D1',parameter='\x03')
xbee.remote_at(dest_addr_long=device["EP1"],command='IR',parameter='\x04\x00')
xbee.remote_at(dest_addr_long=device["EP1"],command='IC',parameter='\x02')

while 1:
        #set led status
        led=not led
        if led:
                xbee.remote_at(dest_addr_long=device["EP1"],command='D4',parameter='\x04')
        else:
                xbee.remote_at(dest_addr_long=device["EP1"],command='D4',parameter='\x05')
        # wait 1 second
        time.sleep(1)
        
ser.close()