"""
This File Calculates the NPV of VLCC
@author : Kodai Ito, 2015/10/24
"""
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

import csv
import settings as s

# input
year = s.YEAR
discount_rate = s.DISCOUNT_RATE
c_build = s.BS_BUILD
operation_cost = s.BS_OPE
other_cost = s.BS_OTHER

# coefficient to convert BSI to Timecharter average
multiplier = 10.45

def ReturnNPV():
	# set the Oil value
	f = open('../scenario/Oil_scenario.csv', 'rb')
	dataReader = csv.reader(f)
	Oil_Month_Prices = [] #US dollar / barrel  1 barrel = 143kg 
	for row in dataReader:
		Oil_Month_Prices.append(float(row[1]))
	f.close()

	# set the BSI
	f = open('../scenario/BSI.csv', 'rb')
	dataReader = csv.reader(f)
	BSI_Month = []  
	for row in dataReader:
		BSI_Month.append(float(row[1]))
	f.close()

	# NPV
	NPV = 0 
	for var in range(year):
		income_per_year = 0
		outcome_per_year = 0
		for num in range(12): # calculate per month
			income_per_year += multiplier * BSI_Month[12*var + num] * 30
			outcome_per_year += operation_cost + other_cost
		NPV += (income_per_year - outcome_per_year)/ (1 + discount_rate)**var
	NPV = NPV - c_build

	return NPV  

#print "Returned BSupramax NPV: " + str(ReturnNPV()) + " USD"