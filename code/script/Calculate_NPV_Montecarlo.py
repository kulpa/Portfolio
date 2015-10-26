import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/Bulk')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/LNG')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/Tanker')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/Expect')

import BulkCapesize as BC
import BulkPanamax as BP
import BulkSupramax as BS
import Oil_expectation as oe
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pylab as plt

NPV_BC = []
NPV_BP = []
NPV_BS = []
m_times = 1000 # montecalro times

# motecalro for m_times
for num in range(m_times):
	oe.binomial_lattice_model()
	NPV_BC.append(BC.ReturnNPV())
	NPV_BP.append(BP.ReturnNPV())
	NPV_BS.append(BS.ReturnNPV())

# Convert array to np.array
BCn = np.array(NPV_BC)
BPn = np.array(NPV_BP)
BSn = np.array(NPV_BS)

def WriteHistgram():
	plt.hist(BCn,facecolor='r', edgecolor='r',bins = 150)
	plt.hist(BPn,facecolor='b', edgecolor='b')
	plt.hist(BSn,color = 'k')

	plt.title("Bulk_Carrier")
	plt.xlabel("NPV[USD]")
	plt.ylabel("Frequency")
	plt.legend(['Capesize','Panamax','Supramax'])
	plt.show()

def CoefficientAnalysis():
	print "------------About average and varience----------------"
	print 'BulkCapesizeNPV: avg=' + str(np.average(BCn)) + " var=" + str(np.var(BCn))
	print 'BulkPanamaxNPV : avg=' + str(np.average(BPn)) + " var=" + str(np.var(BPn))
	print 'BulkSupramaxNPV: avg=' + str(np.average(BSn)) + " var=" + str(np.var(BSn))
	print "------------About correlation coefficient-------------"
	print "Capesize and Panamax : " + str(np.corrcoef(BCn, BPn)[0,1])
	print "Capesize and Supramax: " + str(np.corrcoef(BCn, BSn)[0,1])
	print "Panamax and Supramax : " + str(np.corrcoef(BPn, BSn)[0,1])

CoefficientAnalysis()
WriteHistgram()



