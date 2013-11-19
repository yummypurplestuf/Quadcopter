#! /usr/bin/python

# Import and init an XBee device

import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)

# The name xbee below requires you to add a udev rule in /etc/udev/rules.d/
ser = serial.Serial(
    port='/dev/tty.usbserial-A7025WZ6' or '/dev/xbee',
    baudrate=9600,
    timeout= 0,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

input=1
l = 0
while ser.isOpen() == True:
    # config commands for xbee modual 
    configure_xbee = [
                        
                        '+++', 'atre', 
                        # Serial Interfacing
                        'atro', 'atnb', 'atbd', 'atap',
                        # RF Interfacing
                        'atpl','atca', 
                        # Network and Security
                        'atsl', 'atsh', 'atsd', 'atsc', 'atrr', 'atrn', 'atnt', 'atno',
                        'atni', 'atmy', 'atmm', 'atky', 'atid', 'atee', 'atdl', 'atdh',
                        'atch', 'atce', 'atai', 'ata2', 'ata1',
                        # I/O Settings
                        'atrp', 'atpt', 'atpr', 'atp1', 'atp0', 'atit', 'atir', 'atic',
                        'atd8', 'atd7', 'atd6', 'atd5', 'atd4', 'atd3', 'atd2', 'atd1',

                        'AT%\V'
                        


                        
    ]
    labels = [
                'Serial Interfacing:', 'RF Interfacing', 'Network and Security',
                'I/O Settings', 'I/O Line Passing', 'Execution Commands', 
                'Diagnostics', 'AT Command Options'


    ]
    if l < len(configure_xbee):
        input = configure_xbee[l]

    if l >= len(configure_xbee):
        input = raw_input(">> ")

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
        l += 1