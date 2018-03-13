#!/usr/bin/env python

import time
import serial
ser = serial.Serial(
	port='/dev/ttyAMA0',
	baudrate = 9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)
counter=0

with open('somefile.txt', 'a') as the_file:
	while 1:
		x=ser.readline()
		the_file.write('x')
		print x