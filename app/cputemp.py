import io
import time
import subprocess
import sys

while 1:
#    f=open("/sys/class/thermal/thermal_zone0/temp","r")
#    temp=int(f.readline())//1000
	temp=subprocess.run(["vcgencmd","measure_temp"],stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip()
	temp=str(round(float(temp[5:-2])))
	sys.stdout.write("CPU temp:" + temp + '\r')
	sys.stdout.flush()
	time.sleep(1)
