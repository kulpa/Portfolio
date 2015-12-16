"""
This File Calculates the NPV of BulkPanamax
@author : Kodai Ito, 2015/11/4
"""
import csv
import random
import numpy as np
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../Expect')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

def WriteBalticCSV():
	# set the Oil value
	f = open('../scenario/Oil_scenario.csv', 'rb')
	dataReader = csv.reader(f)
	Oil_Month_Prices = [] #US dollar / barrel  1 barrel = 143kg 
	for row in dataReader:
		Oil_Month_Prices.append(float(row[1]))
	f.close()

	# set the BCI
	BCI = 1549

	# set the BPI
	BPI = 761

	# set the BSI
	BSI = 800

	os.remove('../scenario/BCI.csv')
	fC = open('../scenario/BCI.csv', 'ab')
	os.remove('../scenario/BPI.csv')
	fP = open('../scenario/BPI.csv', 'ab')
	os.remove('../scenario/BSI.csv')
	fS = open('../scenario/BSI.csv', 'ab') 

	csv_C_Writer = csv.writer(fC)
	csv_P_Writer = csv.writer(fP)
	csv_S_Writer = csv.writer(fS)

	now_year = 2015
	now_month = 10

	for Oil_Month_Price in Oil_Month_Prices:
		# BCI = -8.51 * Oil_Month_Price + 0.7 * BCI + 1425 + np.random.normal(0,1384) # This must be changed!!!
		# BPI = -3.54 * Oil_Month_Price + 0.90 * BPI + 447 + np.random.normal(0,957)# This must be changed!!!
		# BSI = -1 * Oil_Month_Price + 0.9 * BSI + np.random.normal(0,214) 		# Tekitoooooooooooooooooooooo

		# keep the correlation coefficient
		BCI = -8.51 * Oil_Month_Price + 0.7 * BCI + 1425 + np.random.normal(0,500) 
		BPI = -3.54 * Oil_Month_Price + 0.90 * BPI + 447 + np.random.normal(0,300)
		BSI = 0.31 * Oil_Month_Price + 0.7 * BSI + 170 + np.random.normal(0,200) 		

		if now_month == 13:
			now_month = 1
			now_year += 1
		else:
			now_month += 1

		csv_C_Writer.writerow([(str(now_year) + '/' + str(now_month)), BCI])
		csv_P_Writer.writerow([(str(now_year) + '/' + str(now_month)), BPI])
		csv_S_Writer.writerow([(str(now_year) + '/' + str(now_month)), BSI])
	fC.close()
	fP.close()
	fS.close()

