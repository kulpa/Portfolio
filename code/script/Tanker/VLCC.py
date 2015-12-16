"""
This File Calculates the NPV of VLCC
@author : Kodai Ito, 2015/10/07
"""
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

import csv
import settings as s
import random

# input
deadweight =  s.VLCC_DEADWEIGHT
v = s.VLCC_VELOCITY
distance = s.VLCC_DISTANCE
WS_rate = s.WS_RATE
year = s.YEAR
fc = s.VLCC_FC
discount_rate = s.DISCOUNT_RATE
c_build = s.VLCC_BUILD
operation_cost = s.VLCC_OPE
other_cost = s.VLCC_OTHER

def ReturnNPV():
	# set the value
	f = open('../scenario/Oil_scenario.csv', 'rb')
	dataReader = csv.reader(f)
	Oil_Month_Price = [] #US dollar / barrel  1 barrel = 143kg 
	for row in dataReader:
		Oil_Month_Price.append(float(row[1]))
	f.close()

	# income calculation
	transportation_amount = deadweight * (year * 365 * 24) * 0.7 / (2 * distance / v)
	transportation_amount_per_month = transportation_amount / (year * 12)

	# NPV
	NPV = 0 
	for var in range(year):
		income_per_year = 0
		c_fuel_per_year = 0
		for num in range(12): # calculate per month
			# print "Year:" +str(12*var) + " | " + str(Oil_Month_Price[12*var])
			# print "Month:" +str(12*var + num) +  " | " + str(Oil_Month_Price[12*var + num])

			# with this method, I can caluculte just one year income!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			# must be chabged!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			income_per_year += (0.1932 * Oil_Month_Price[12*var] + 6.713) * WS_rate * transportation_amount_per_month
			c_fuel_per_year += fc * 30 * (Oil_Month_Price[num] / 0.143 )
		outcome_per_year = c_fuel_per_year + 12*operation_cost + 12*other_cost
		NPV += ((income_per_year - outcome_per_year)) / (1 + discount_rate)**var
	NPV = NPV - c_build

	return NPV 

# print "Returned VLCC NPV: " + str(ReturnNPV())