from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import csv
#import Ornstein_Uhlenbeck as orn
#import Geometric_Mean_Reversion as gmr
import Oil_expectation as oe
import datetime
import matplotlib
from datetime import datetime as dt

#f = open('../../data/CrudeOilPrice.csv', 'rb')
filepath='/Users/itokoudai/Documents/school_class/MyLabratory/GraduateThesis/code/data/CrudeOilPrice.csv'
kind="Oil"
if kind == "WS":
	f = open(filepath, 'rU')
else:
	f = open(filepath, 'rb')
#f = open('/Users/itokoudai/Documents/school_class/MyLabratory/GraduateThesis/code/data//ODA-PIORECR_USD.csv', 'rb')
monte_time=10

dataReader = csv.reader(f)

dates = []
data_prices = []
tdatetime = []

j = 0
for row in dataReader:
	if j != 0:
   		dates.append(row[0])
   		data_prices.append(float(row[1]))
   		try:
   			tdatetime.append(dt.strptime(row[0], '%Y-%m-%d'))
   		except:
   			tdatetime.append(dt.strptime(row[0], '%Y/%m/%d'))
   	else:
   		j = 1

graph_date = matplotlib.dates.date2num(tdatetime)

plt.plot_date(graph_date,data_prices,'-')

max_prices = []
max_price = 0
min_prices = []
min_price = 10000
d = []
for num in range(monte_time):
	
	print "Processed: " + str(float(num)/monte_time * 100) + "%"
 
	#orn.ornstein_uhlenbeck_model() # recalculate
	oe.binomial_lattice_model()
	#gmr.geometric_mean_reversion()

	#f = open('../../scenario/Oil_scenario_ornstein.csv', 'rb')
	f = open('/Users/itokoudai/Documents/school_class/MyLabratory/GraduateThesis/code/scenario/%s_scenario.csv'%kind, 'rb')


	dataReader = csv.reader(f)

	prices = []
	number = []
	datetime_reader = []

	i = len(dates)
	for row in dataReader:
		prices.append(float(row[1]))
		datetime_reader.append(dt.strptime(row[0], '%Y/%m'))
		i += 1

	# if prices[-1] > max_price:
	# 	max_price = prices[-1]
	# 	max_prices = prices
	# 	d = datetime_reader

	# if prices[-1] < min_price:
	# 	min_price = prices[-1]
	# 	min_prices = prices
	# 	d = datetime_reader

	graph_date2 = matplotlib.dates.date2num(datetime_reader)
	plt.plot_date(graph_date2,prices,'-')	

# graph_date2 = matplotlib.dates.date2num(d)
# plt.plot_date(graph_date2,max_prices,'-')
# plt.plot_date(graph_date2,min_prices,'-')
plt.title("Expectaion of %s"%kind)
plt.xlabel("[year]")
plt.ylabel(kind)
plt.savefig("../../image/binomial_%s%s"%(kind,monte_time))	
plt.show()