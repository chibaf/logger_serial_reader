def read_m5(port,speed):
	import serial, sys
	import syslog
	import time
	
	#The following line is for serial over GPIO	
	ser = serial.Serial(port,speed)
	
	# Serial read section
	line = ser.readline()
	line2=line.strip().decode('utf-8')
	data = [str(val) for val in line2.split(",")]
	return data