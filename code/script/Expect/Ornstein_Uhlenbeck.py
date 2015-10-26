"""
This File writes the oil price expect scenario by the ornstein-uhlenbeck model
@author : Kodai Ito, 2015/10/12
"""
import csv   
import math
from numpy.random import *
import numpy as np
import os

year = 20
lamda = 0.0105555139395
mean = 48.8476190476
sigma = 4.3488515538

# read the csv file and calculate the parameter # 
f = open('../../data/CrudeOilPrice.csv', 'rb')

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
def ornstein_uhlenbeck_model():
	os.remove('../../scenario/Oil_scenario_ornstein.csv')
	f = open('../../scenario/Oil_scenario_ornstein.csv', 'ab') 
	csvWriter = csv.writer(f)
	next_price = prices[-1]

	now_year = 2015
	now_month = 9

	for num in range(year * 12):
		now_month += 1
		next_price = next_price*(math.e**(-lamda)) + mean*(1.0-math.e**(-lamda)) + sigma*(((1.0-math.e**(-2.0*lamda))/(2.0*lamda))**0.5)*randn() 
		if now_month == 13:
			now_month = 1
			now_year += 1
		csvWriter.writerow([(str(now_year) + '/' + str(now_month)), next_price])
	f.close()

ornstein_uhlenbeck_model()