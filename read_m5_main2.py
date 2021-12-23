from read_m5_class import m5logger
import serial, sys
import syslog
import time

ser = serial.Serial(sys.argv[1],sys.argv[2])
shield=m5logger()
while True:
  data=shield.read_logger(ser)
  print(data)
  time.sleep(0.1)
exit()