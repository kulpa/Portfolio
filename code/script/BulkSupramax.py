"""
This File Calculates the NPV of VLCC
@author : Kodai Ito, 2015/10/24
"""

import csv
import Oil_expectation as oe
import settings as s

# input
deadweight =  s.BS_DEADWEIGHT
v = s.BS_VELOCITY
distance = s.BS_DISTANCE
year = s.YEAR
discount_rate = s.DISCOUNT_RATE
c_build = s.BS_BUILD

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
	BSI_Month = [] #income/ton
	for Oil_Month_Price in Oil_Month_Prices:
		BSI_estimated = 0.5 * Oil_Month_Price + 800 # This must be changed!!!
		BSI_Month.append(BSI_estimated)

	# NPV
	NPV = 0 
	for var in range(year):
		income_per_year = 0
		for num in range(12): # calculate per month
			income_per_year += multiplier * BSI_Month[12*var + num] * 30
		NPV += income_per_year / (1 + discount_rate)**var
	NPV = NPV - c_build

	return NPV  

print "Returned BSupramax NPV: " + str(ReturnNPV()) + " USD"