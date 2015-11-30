from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv
#import Ornstein_Uhlenbeck as orn
import Oil_expectation as oe
import datetime
import matplotlib
from datetime import datetime as dt

#f = open('../../data/CrudeOilPrice.csv', 'rb')
f = open('/Users/itokoudai/Documents/school_class/MyLabratory/GraduateThesis/code/data/CrudeOilPrice.csv', 'rb')

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

max_prices = []
max_price = 0
min_prices = []
min_price = 10000
d = []
for num in range(1000):
	
	print "Processed: " + str(float(num)/1000.0 * 100) + "%"
 
	#orn.ornstein_uhlenbeck_model() # recalculate
	oe.binomial_lattice_model()

	#f = open('../../scenario/Oil_scenario_ornstein.csv', 'rb')
	f = open('/Users/itokoudai/Documents/school_class/MyLabratory/GraduateThesis/code/scenario/Oil_scenario.csv', 'rb')


	dataReader = csv.reader(f)

	prices = []
	number = []
	datetime_reader = []

	i = len(dates)
	for row in dataReader:
		prices.append(float(row[1]))
		datetime_reader.append(dt.strptime(row[0], '%Y/%m'))
		i += 1

	if prices[-1] > max_price:
		max_price = prices[-1]
		max_prices = prices
		d = datetime_reader

	if prices[-1] < min_price:
		min_price = prices[-1]
		min_prices = prices
		d = datetime_reader

	# graph_date2 = matplotlib.dates.date2num(datetime_reader)
	# plt.plot_date(graph_date2,prices,'-')	

graph_date2 = matplotlib.dates.date2num(d)
plt.plot_date(graph_date2,max_prices,'-')
plt.plot_date(graph_date2,min_prices,'-')
plt.xlabel("[year]")
plt.ylabel("Oil[USD/h]")	
plt.show()