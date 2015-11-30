"""
This File Calculates the NPV of BulkCapesize
@author : Kodai Ito, 2015/10/26
"""
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../Expect')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

import csv
import settings as s

# input
year = s.YEAR
discount_rate = s.DISCOUNT_RATE
c_build = s.BC_BUILD
operation_cost = s.BC_OPE
other_cost = s.BC_OTHER

# coefficient to convert BCI to Timecharter average
multiplier = 8.147

def ReturnNPV():
	# set the Oil value
	f = open('../scenario/Oil_scenario.csv', 'rb')
	dataReader = csv.reader(f)
	Oil_Month_Prices = [] #US dollar / barrel  1 barrel = 143kg 
	for row in dataReader:
		Oil_Month_Prices.append(float(row[1]))
	f.close()

	# set the BCI
	f = open('../scenario/BCI.csv', 'rb')
	dataReader = csv.reader(f)
	BCI_Month = []  
	for row in dataReader:
		BCI_Month.append(float(row[1]))
	f.close()

	# NPV
	NPV = 0 
	for var in range(year):
		income_per_year = 0
		outcome_per_year = 0
		for num in range(12): # calculate per month
			income_per_year += multiplier * BCI_Month[12*var + num] * 30
			outcome_per_year += operation_cost + other_cost
		NPV += (income_per_year - outcome_per_year)/ (1 + discount_rate)**var
	NPV = NPV - c_build

	return NPV  

#print "Returned BCapesize NPV: " + str(ReturnNPV()) + " USD"