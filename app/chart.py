import matplotlib.pyplot as plt
import matplotlib.dates as pltdate
import database as db
import datetime as d

def construct_chart():
	data=db.Database()
	x_axis=data.get_time_data()
	y_temperature=data.get_temperature_data()
	y_pressure=data.get_pressure_data()
	y_humidity=data.get_humidity_data()
	
	plt.subplot(3,1,1)
	plt.plot(x_axis,y_temperature)
	plt.xlabel('Date')
	plt.ylabel('Temperature (°C)')
	plt.ylim([25,75])
	
	plt.subplot(3,1,2)
	plt.plot(x_axis,y_pressure)
	plt.xlabel('Date')
	plt.ylabel('Pressure')
	plt.ylim([880,1120])
	
	plt.subplot(3,1,3)
	plt.plot(x_axis,y_humidity)
	plt.xlabel('Date')
	plt.ylabel('Humidity (%)')
	plt.ylim([15,95])
	
	plt.gcf().autofmt_xdate()
	plt.show()
	
construct_chart()	
