import serial, sys
import syslog
import time
from read_m5_sub import read_m5

port = sys.argv[1]
speed = sys.argv[2]
time.sleep(2)
for i in range(0,10):
  array=read_m5(port,speed)
  print(array)
exit()