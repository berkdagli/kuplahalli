import sqlite3
from datetime import datetime
import time

class Database:

	con=None
	c=None
	
	def __init__(self,path):
		self.con=sqlite3.connect(path,check_same_thread=False)
		self.con.row_factory=lambda cursor, row: row[0]
		self.c=self.con.cursor()

	def initializeDB(self,numOfSensors):
		self.c.execute('CREATE TABLE IF NOT EXISTS sensordata(datetime text not null,sensor_id int not null,temp int,pressure int,humidity int,voltage int,constraint cnstrnt unique(datetime,sensor_id))')
		self.con.commit()

	def writeDB(self,sensor_id,temp,pressure,humidity,voltage):
		time=str(datetime.now().isoformat(timespec='minutes'))
		time=time.replace('T',' ')
		self.c.execute('INSERT OR IGNORE INTO sensordata(datetime,sensor_id,temp,pressure,humidity,voltage) VALUES(?,?,?,?,?,?)',(time,int(sensor_id),int(temp),float(pressure),int(humidity),int(voltage)))
		self.con.commit()
	
	def readDB(self):
		self.c.execute('SELECT * FROM sensordata')
		rows=array(self.c.fetchall())
		count=0
		for row in rows:
			print(f'{row[0]}\t {row[1]}\t {row[2]}\t {row[3]}')
			count=count+1
		print(f'{count} items')
		
	def get_time_data(self,sensor_id):
		self.c.execute(f'SELECT sensordata.datetime FROM sensordata WHERE sensor_id={sensor_id}')
		return self.c.fetchall()
		
	def get_temperature_data(self,sensor_id):
		self.c.execute(f'SELECT sensordata.temp FROM sensordata WHERE sensor_id={sensor_id}')
		return self.c.fetchall()
	
	def get_pressure_data(self,sensor_id):
		self.c.execute(f'SELECT sensordata.pressure FROM sensordata WHERE sensor_id={sensor_id}')
		return self.c.fetchall()
		
	def get_humidity_data(self,sensor_id):
		self.c.execute(f'SELECT sensordata.humidity FROM sensordata WHERE sensor_id={sensor_id}')
		return self.c.fetchall()
		
	def get_voltage_data(self,sensor_id):
		self.c.execute(f'SELECT sensordata.voltage FROM sensordata WHERE sensor_id={sensor_id}')		
		return self.c.fetchall()
		
