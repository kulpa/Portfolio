"""
This File Calculates the NPV of BulkPanamax
@author : Kodai Ito, 2015/10/24
"""

import csv
import Oil_expectation as oe
import settings as s

# input
deadweight =  s.BP_DEADWEIGHT
v = s.BP_VELOCITY
distance = s.BP_DISTANCE
year = s.YEAR
discount_rate = s.DISCOUNT_RATE
c_build = s.BP_BUILD

# coefficient to convert BPI to Timecharter average
multiplier = 8.00

def ReturnNPV():
	# set the Oil value
	f = open('../scenario/Oil_scenario.csv', 'rb')
	dataReader = csv.reader(f)
	Oil_Month_Prices = [] #US dollar / barrel  1 barrel = 143kg 
	for row in dataReader:
		Oil_Month_Prices.append(float(row[1]))
	f.close()

	# set the BPI
	BPI_Month = [] #income/ton
	for Oil_Month_Price in Oil_Month_Prices:
		BPI_estimated = 1 * Oil_Month_Price + 800 # This must be changed!!!
		BPI_Month.append(BPI_estimated)

	# NPV
	NPV = 0 
	for var in range(year):
		income_per_year = 0
		for num in range(12): # calculate per month
			income_per_year += multiplier * BPI_Month[12*var + num] * 30
		NPV += income_per_year / (1 + discount_rate)**var
	NPV = NPV - c_build

	return NPV  

print "Returned BPanamax NPV: " + str(ReturnNPV()) + " USD"