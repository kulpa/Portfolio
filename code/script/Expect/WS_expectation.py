"""
This File reads the oil price csv and writes the oil price expect scenario
@author : Kodai Ito, 2015/10/07
"""

import csv   
import math
import random
import numpy as np
import os
import logging
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import settings as s

year = s.YEAR

logging.info('Calculation about binomial_lattice_model start')
# read the csv file and calculate the parameter # 
#f = open('../data/CrudeOilPrice.csv', 'rb')
f = open('/Users/itokoudai/Documents/school_class/MyLabratory/GraduateThesis/code/data/WS.csv', 'rU')
#f = open('/Users/itokoudai/Documents/school_class/MyLabratory/GraduateThesis/code/data/Crtest.csv', 'rb')

dataReader = csv.reader(f)

dates = []
prices = []
i = 0

for row in dataReader:
	if i != 0:
		dates.append(row[0])
  		prices.append(float(row[1]))
  	i = 1

# calculate v
sum_lnprices = 0 
for i in range(len(prices)-1-12):
	if i % 12 == 0: 
		sum_lnprices += math.log(prices[i+12]/prices[i])

v = sum_lnprices/ (len(prices) - 1)

# calculate var
var_lnprices = 0
for i in range(len(prices)-1-12):
	if i % 12 == 0: 
		var_lnprices += (math.log(prices[i+12]/prices[i]) - v)**2

var = var_lnprices/ (len(prices) - 1)
sigma = var**0.5
dt = 1.0/12.0
dt_root = dt**0.5

# do montecalro simulation
probability = 0.5 * (1 + v/sigma*dt_root)
u = math.e**(sigma*dt_root)
d = math.e**(-sigma*dt_root)

print "-------------Oil binomial parameter--------------"
print "v          : " + str(v)
print "sigma      : " + str(sigma)
print "u          : " + str(u)
print "d          : " + str(d)
print "probability: " + str(probability)

logging.info('Calculation about binomial_lattice_model end')

Oil_price_scenario = []
# write the csv file # 
def binomial_lattice_model():
	# os.remove('../scenario/Oil_scenario.csv')
	# f = open('../scenario/Oil_scenario.csv', 'ab') 
	os.remove('/Users/itokoudai/Documents/school_class/MyLabratory/GraduateThesis/code/scenario/WS_scenario.csv')
	f = open('/Users/itokoudai/Documents/school_class/MyLabratory/GraduateThesis/code/scenario/WS_scenario.csv', 'ab')
	csvWriter = csv.writer(f)
	next_price = prices[-1]

	now_year = 2013
	now_month = 11

	for num in range(year * 12):
		now_month += 1
		if(random.random() <= probability):
			next_price = next_price * u
		else:
			next_price = next_price * d
		Oil_price_scenario.append(next_price)
		if now_month == 13:
			now_month = 1
			now_year += 1
		csvWriter.writerow([(str(now_year) + '/' + str(now_month)), next_price])
	f.close()
	return Oil_price_scenario

#binomial_lattice_model()
