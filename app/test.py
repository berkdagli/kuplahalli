'''
from ruuvitag_sensor.ruuvi import RuuviTagSensor
import ruuvitag_sensor.log

ruuvitag_sensor.log.enable_console()

RuuviTagSensor.find_ruuvitags()
'''

import database
from numpy import array

db=database.Database("sensordata.db")
'''
db.c.execute(f'SELECT data_id FROM sensordata WHERE datetime="2018-08-10 09:30"')
row=db.c.fetchall()
print(row)

db.c.execute(f'DELETE FROM sensordata WHERE data_id=7963 OR data_id=7964 OR data_id=7965 OR data_id=7966 OR data_id=7967 OR data_id=7968')
db.con.commit()
'''
db.c.execute(f'SELECT temp FROM sensordata WHERE sensor_id=1')
row=db.c.fetchall()
print(row)