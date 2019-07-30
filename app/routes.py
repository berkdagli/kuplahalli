from flask import Flask, render_template
from app import app
from app import database

DBPATH='/home/kuplahalli/app/sensordata.db'

@app.route("/")
def main():
	db=database.Database(DBPATH)
	return render_template('main.html')
	
@app.route("/ruuvi1/temperature")
def r1Temp():
	db=database.Database(DBPATH)
	return render_template('tempchart.html',labels=db.get_time_data(0),values=db.get_temperature_data(0))
	
@app.route("/ruuvi2/temperature")
def r2temp():
	db=database.Database(DBPATH)
	return render_template('tempchart.html',labels=db.get_time_data(1),values=db.get_temperature_data(1))

@app.route("/ruuvi3/temperature")	
def r3temp():
	db=database.Database(DBPATH)
	return render_template('tempchart.html',labels=db.get_time_data(2),values=db.get_temperature_data(2))
	
@app.route("/ruuvi4/temperature")
def r4temp():
	db=database.Database(DBPATH)
	return render_template('tempchart.html',labels=db.get_time_data(3),values=db.get_temperature_data(3))
	
@app.route("/ruuvi5/temperature")
def r5temp():
	db=database.Database(DBPATH)
	return render_template('tempchart.html',labels=db.get_time_data(4),values=db.get_temperature_data(4))
	
@app.route("/ruuvi6/temperature")
def r6temp():
	db=database.Database(DBPATH)
	return render_template('tempchart.html',labels=db.get_time_data(5),values=db.get_temperature_data(5))
	
@app.route("/ruuvi1/pressure")
def r1pressure():
	db=database.Database(DBPATH)
	return render_template('pressurechart.html',labels=db.get_time_data(0),values=db.get_pressure_data(0))

@app.route("/ruuvi2/pressure")
def r2pressure():
	db=database.Database(DBPATH)
	return render_template('pressurechart.html',labels=db.get_time_data(1),values=db.get_pressure_data(1))
	
@app.route("/ruuvi3/pressure")
def r3pressure():
	db=database.Database(DBPATH)
	return render_template('pressurechart.html',labels=db.get_time_data(2),values=db.get_pressure_data(2))
	
@app.route("/ruuvi4/pressure")
def r4pressure():
	db=database.Database(DBPATH)
	return render_template('pressurechart.html',labels=db.get_time_data(3),values=db.get_pressure_data(3))			
	
@app.route("/ruuvi5/pressure")
def r5pressure():
	db=database.Database(DBPATH)
	return render_template('pressurechart.html',labels=db.get_time_data(4),values=db.get_pressure_data(4))	
	
@app.route("/ruuvi6/pressure")
def r6pressure():
	db=database.Database(DBPATH)
	return render_template('pressurechart.html',labels=db.get_time_data(5),values=db.get_pressure_data(5))	
	
@app.route("/ruuvi1/humidity")
def r1humidity():
	db=database.Database(DBPATH)
	return render_template('humiditychart.html',labels=db.get_time_data(0),values=db.get_humidity_data(0))	
	
@app.route("/ruuvi2/humidity")
def r2humidity():
	db=database.Database(DBPATH)
	return render_template('humiditychart.html',labels=db.get_time_data(1),values=db.get_humidity_data(1))
	
@app.route("/ruuvi3/humidity")
def r3humidity():
	db=database.Database(DBPATH)
	return render_template('humiditychart.html',labels=db.get_time_data(2),values=db.get_humidity_data(2))
	
@app.route("/ruuvi4/humidity")
def r4humidity():
	db=database.Database(DBPATH)
	return render_template('humiditychart.html',labels=db.get_time_data(3),values=db.get_humidity_data(3))	
	
@app.route("/ruuvi5/humidity")
def r5humidity():
	db=database.Database(DBPATH)
	return render_template('humiditychart.html',labels=db.get_time_data(4),values=db.get_humidity_data(4))	
	
@app.route("/ruuvi6/humidity")
def r6humidity():
	db=database.Database(DBPATH)
	return render_template('humiditychart.html',labels=db.get_time_data(5),values=db.get_humidity_data(5))	
	
@app.route("/ruuvi1/voltage")
def r1voltage():
	db=database.Database(DBPATH)
	return render_template('voltagechart.html',labels=db.get_time_data(0),values=db.get_voltage_data(0))
	
@app.route("/ruuvi2/voltage")
def r2voltage():
	db=database.Database(DBPATH)
	return render_template('voltagechart.html',labels=db.get_time_data(1),values=db.get_voltage_data(1))	
	
@app.route("/ruuvi3/voltage")
def r3voltage():
	db=database.Database(DBPATH)
	return render_template('voltagechart.html',labels=db.get_time_data(2),values=db.get_voltage_data(2))
	
@app.route("/ruuvi4/voltage")
def r4voltage():
	db=database.Database(DBPATH)
	return render_template('voltagechart.html',labels=db.get_time_data(3),values=db.get_voltage_data(3))

@app.route("/ruuvi5/voltage")
def r5voltage():
	db=database.Database(DBPATH)
	return render_template('voltagechart.html',labels=db.get_time_data(4),values=db.get_voltage_data(4))	
		
@app.route("/ruuvi6/voltage")
def r6voltage():
	db=database.Database(DBPATH)
	return render_template('voltagechart.html',labels=db.get_time_data(5),values=db.get_voltage_data(5))	
	
	
	
	
	
	
		
	
								
