"""
This File Calculates the NPV of VLCC
@author : Kodai Ito, 2015/10/07
"""

import csv
import Oil_expectation as oe
import settings as s

# input
deadweight =  s.VLCC_DEADWEIGHT
v = s.VLCC_VELOCITY
distance = s.VLCC_DISTANCE
BCI_rate = s.BCI_RATE
year = s.YEAR
fc = s.VLCC_FC
discount_rate = s.DISCOUNT_RATE
c_build = s.VLCC_BUILD

def ReturnNPV():
	# set the Oil value
	f = open('../scenario/Oil_scenario.csv', 'rb')
	dataReader = csv.reader(f)
	Oil_Month_Prices = [] #US dollar / barrel  1 barrel = 143kg 
	for row in dataReader:
		Oil_Month_Prices.append(float(row[1]))
	f.close()

	# set the BCI
	BCI_Month_Prices = [] #income/ton
	for Oil_Month_Price in Oil_Month_Prices:
		BCI_Month_Prices.append(-1.01 * Oil_Month_Price + 152.9)

	# income calculation
	transportation_amount = deadweight * (year * 365 * 24) / (2.5 * distance / v)
	transportation_amount_per_month = transportation_amount / (year * 12)

	# NPV
	NPV = 0 
	for var in range(year):
		income_per_year = 0
		c_fuel_per_year = 0
		for num in range(12): # calculate per month
			income_per_year += BCI_Month_Prices[12*var + num] * BCI_rate * transportation_amount_per_month
			c_fuel_per_year += fc * 30 * (Oil_Month_Prices[12*var + num] / 0.143 )
		NPV += (income_per_year - c_fuel_per_year) / (1 + discount_rate)**var
	NPV = NPV - c_build

	return NPV  

print "Returned VLCC NPV: " + str(ReturnNPV())