from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv
import Ornstein_Uhlenbeck as orn
import datetime
import matplotlib
from datetime import datetime as dt

f = open('../data/CrudeOilPrice.csv', 'rb')

dataReader = csv.reader(f)

dates = []
data_prices = []
tdatetime = []

j = 0
for row in dataReader:
	if j != 0:
   		dates.append(row[0])
   		data_prices.append(float(row[1]))
   		tdatetime.append(dt.strptime(row[0], '%Y-%m-%d'))
   	else:
   		j = 1

graph_date = matplotlib.dates.date2num(tdatetime)

plt.plot_date(graph_date,data_prices,'-')

for num in range(1000):
	
	print "Processed: " + str(float(num)/1000.0 * 100) + "%"
 
	orn.ornstein_uhlenbeck_model() # recalculate

	f = open('../scenario/Oil_scenario_ornstein.csv', 'rb')

	dataReader = csv.reader(f)

	prices = []
	number = []
	datetime_reader = []

	i = len(dates)
	for row in dataReader:
		prices.append(float(row[1]))
		datetime_reader.append(dt.strptime(row[0], '%Y/%m'))
		i += 1

	graph_date2 = matplotlib.dates.date2num(datetime_reader)
	plt.plot_date(graph_date2,prices,'-')	

plt.xlabel("[year]")
plt.ylabel("Oil[USD/h]")	
plt.show()