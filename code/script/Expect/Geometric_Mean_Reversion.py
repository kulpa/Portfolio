"""
This File writes the oil price expect scenario by the geometric mean reversion
@author : Kodai Ito, 2015/12/7
"""
import csv   
import math
from numpy.random import *
import numpy as np
import os

year = 20
lamda = 1000
mean = 48.8476190476
sigma = 4.3488515538

# read the csv file and calculate the parameter # 
#f = open('../data/CrudeOilPrice.csv', 'rb')
f = open('/Users/itokoudai/Documents/school_class/MyLabratory/GraduateThesis/code/data/CrudeOilPrice.csv', 'rb')


dataReader = csv.reader(f)

dates = []
prices = []
i = 0

for row in dataReader:
	if i != 0:
		dates.append(row[0])
  		prices.append(float(row[1]))
  	i = 1


# write the csv file # 
def geometric_mean_reversion():
	#os.remove('../scenario/Oil_scenario.csv')
	#f = open('../scenario/Oil_scenario.csv', 'ab') 
	os.remove('/Users/itokoudai/Documents/school_class/MyLabratory/GraduateThesis/code/scenario/Oil_scenario.csv')
	f = open('/Users/itokoudai/Documents/school_class/MyLabratory/GraduateThesis/code/scenario/Oil_scenario.csv', 'ab')
	csvWriter = csv.writer(f)
	next_price = prices[-1]

	now_year = 2015
	now_month = 9

	for num in range(year * 12):
		now_month += 1
		print next_price
		next_price = math.e**(math.log(next_price)*(math.e**(-lamda)) + (mean-0.5*(sigma**2)/lamda)*(1.0-math.e**(-lamda)) + sigma*(((1.0-math.e**(-2.0*lamda))/(2.0*lamda))**0.5)*randn()) 
		if now_month == 13:
			now_month = 1
			now_year += 1
		csvWriter.writerow([(str(now_year) + '/' + str(now_month)), next_price])
	f.close()

#ornstein_uhlenbeck_model()