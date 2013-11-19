#! /usr/bin/python

# Import and init an XBee device

import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/tty.usbserial-A7025WZ6',
    baudrate=9600,
    timeout= 0,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

input=1
while 1 :
    # get keyboard input
    input = raw_input(">> ") # This is where the dictionary for the command list will go 
    
    if input == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        if input == '+++':
        	ser.write(input) # ser.write(input + '\r\n')
        	out = ''
        	time.sleep(1.125)
        else:
        	ser.write(input + '\r\n')
        	out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(.125)
    
        while ser.inWaiting() > 0:
            out += ser.read()

        if out != '':
        	print out