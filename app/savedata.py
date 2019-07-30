import sys
import database
import sensors

sensor=sensors.Sensors()

db=database.Database('/home/pi/Desktop/kuplahalli/app/sensordata.db')
db.initializeDB(len(sensor.ruuviSensors))

r1Temp,r1Pressure,r1Humidity,r1Voltage=sensor.getRuuvitagData(sensor.ruuviSensors[0])
r2Temp,r2Pressure,r2Humidity,r2Voltage=sensor.getRuuvitagData(sensor.ruuviSensors[1])
r3Temp,r3Pressure,r3Humidity,r3Voltage=sensor.getRuuvitagData(sensor.ruuviSensors[2])
r4Temp,r4Pressure,r4Humidity,r4Voltage=sensor.getRuuvitagData(sensor.ruuviSensors[3])
r5Temp,r5Pressure,r5Humidity,r5Voltage=sensor.getRuuvitagData(sensor.ruuviSensors[4])
r6Temp,r6Pressure,r6Humidity,r6Voltage=sensor.getRuuvitagData(sensor.ruuviSensors[5])

db.writeDB(0,r1Temp,r1Pressure,r1Humidity,r1Voltage)
db.writeDB(1,r2Temp,r2Pressure,r2Humidity,r2Voltage)
db.writeDB(2,r3Temp,r3Pressure,r3Humidity,r3Voltage)
db.writeDB(3,r4Temp,r4Pressure,r4Humidity,r4Voltage)
db.writeDB(4,r5Temp,r5Pressure,r5Humidity,r5Voltage)
db.writeDB(5,r6Temp,r6Pressure,r6Humidity,r6Voltage)
