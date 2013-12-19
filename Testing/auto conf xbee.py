#! /usr/bin/python

# Import and init an XBee device

import time
from serial import Serial


# configure the serial connections
# (the parameters differ on the device you are connecting to)

# The name xbee below requires you to add a udev rule in /etc/udev/rules.d/


AT_COMMANDS = ['+++', 'atre', 
               # Serial Interfacing
               'atro', 'atnb', 'atbd', 'atap',
               # RF Interfacing
               'atpl','atca', 
               # Network and Security
               'atsl', 'atsh', 'atsd', 'atsc', 'atrr', 'atrn', 'atnt',
               'atno', 'atni', 'atmy', 'atmm', 'atky', 'atid', 'atee',
               'atdl', 'atdh', 'atch', 'atce', 'atai', 'ata2', 'ata1',
               # I/O Settings
               'atrp', 'atpt', 'atpr', 'atp1', 'atp0', 'atit', 'atir',
               'atic', 'atd8', 'atd7', 'atd6', 'atd5', 'atd4', 'atd3',
               'atd2', 'atd1'
               #'AT\%V'
               ]

LABELS = ['Serial Interfacing:', 'RF Interfacing', 'Network and Security',
          'I/O Settings', 'I/O Line Passing', 'Execution Commands', 
          'Diagnostics', 'AT Command Options']
def recieve_message(message):
  print ser.read()

def send_command(command):
    # send the command to the device
    # (note that I happend a \r\n carriage return and line feed to
    # the characters - this is requested by my device)
    if command == '+++':
        ser.write(command)
        time.sleep(1.125)  # Extra wait as connection is established
    else:
        ser.write(command + '\r\n')
    
    # let's wait before reading output to give device time to answer
    time.sleep(.125)

    out = ''
    while ser.inWaiting() > 0:
        out += ser.read()

    return out
    

with Serial('/dev/tty.usbserial-A7025WZ6') as ser:
    while ser.isOpen():
        # Prompt user for a command
        command = raw_input(">> ")

        # Special (Non-AT commands)
        if command == 'exit':
            ser.close()
            break
        elif command == 'status':
            for command in AT_COMMANDS:
                response = send_command(command)
                if response:
                    print response
            continue

        # Send general (AT) commands
        response = send_command(command)
        if response:
            print response
