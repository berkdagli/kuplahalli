from ruuvitag_sensor.ruuvitag import RuuviTag
import sys
import time

class Sensors():
	ruuviSensors=[]

	def __init__(self):
		self.ruuviSensors.insert(0,RuuviTag('FB:9C:C6:4D:2C:46'))
		self.ruuviSensors.insert(1,RuuviTag('D1:82:DB:D5:46:1D'))
		self.ruuviSensors.insert(2,RuuviTag('C6:BD:CC:FA:58:1C'))
		self.ruuviSensors.insert(3,RuuviTag('DC:1F:FE:DA:57:36'))
		self.ruuviSensors.insert(4,RuuviTag('EC:E0:88:7D:3B:66'))
		self.ruuviSensors.insert(5,RuuviTag('EC:D4:41:5A:82:BC'))				
			
	def sensehatPrintData(self):
		while 1:
			h,t,p = self.getSensehatData();

			sys.stdout.write('Temp:'+str(t)+' Pressure:'+str(p)+' Humidity:'+str(h)+'\r')
			sys.stdout.flush()
			time.sleep(1)
	
	def getSensehatData(self):
		h=round(self.sensehat.get_humidity())
		t=round(self.sensehat.get_temperature())
		p=round(self.sensehat.get_pressure())
		
		return h,t,p
		
	def getRuuvitagData(self,ruuviSensor):
		data=ruuviSensor.update()
		temp=round(data["temperature"])
		pressure=data["pressure"]
		humidity=round(data["humidity"])
		voltage=data["battery"]
		return temp,pressure,humidity,voltage			
			
	def ruuvitagPrintData(self,ruuviSensor):
		while 1:
			t,p,h,v=self.getRuuvitagData(ruuviSensor)
			sys.stdout.write('Temp:'+str(t)+' Pressure:'+str(p)+' Humidity:'+str(h)+' Battery Voltage:'+str(v)+'\r')
			sys.stdout.flush()
			time.sleep(1)
			
	def numOfSensors(self):
		return len(self.ruuviSensors)		
			
#sensor=Sensors()
#sensor.sensehatPrintData()
#sensor.ruuvitagPrintData(sensor.ruuviSensors[0])				
