import serial
import time
import math
import sys

ser = serial.Serial('/dev/ttyACM0',9600)
#read_serial=ser.readline()`1+
#time.sleep(5)
#ser.write("forward")
#time.sleep(2)

#ser.write("backward")
#time.sleep(2)
x=0
ser.write(str(x))
time.sleep(3)
#while True:
#	ser.write(str(math.sin(x)))
#	x=x+1
#	time.sleep(1)
ser.write(str(0.1))
while True:
	try:
		pass
	except KeyboardInterrupt:
		ser.write(str(0))
		break

