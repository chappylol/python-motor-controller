#!/usr/bin/python

import time
import serial
import sys
import random
from lib import motorFunctions
from inspect import getmembers,isfunction

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 115200,
    bytesize = serial.EIGHTBITS,
    stopbits = serial.STOPBITS_ONE,
    parity = serial.PARITY_NONE
)

#ser.open()
if ser.isOpen():
  print "Serial socket opened." 

count = 0
output = 1

while True:
    packet = motorFunctions.printAndRunOptions()

    ser.write(packet)
    out = ''
    #time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1)

    if out != '':
        print "Output: \'" + out + '\''
