import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/Bulk')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/LNG')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/Tanker')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/Expect')

import BulkCapesize as BC
import BulkPanamax as BP
import BulkSupramax as BS
import VLCC as VL
#import Oil_expectation as oe
import Ornstein_Uhlenbeck as ou
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pylab as plt

NPV_BC = []
NPV_BP = []
NPV_BS = []
NPV_VL = []
m_times = 1000 # montecalro times

# motecalro for m_times
for num in range(m_times):
	#oe.binomial_lattice_model()
	ou.ornstein_uhlenbeck_model()
	NPV_BC.append(BC.ReturnNPV())
	NPV_BP.append(BP.ReturnNPV())
	NPV_BS.append(BS.ReturnNPV())
	NPV_VL.append(VL.ReturnNPV())

# Convert array to np.array
BCn = np.array(NPV_BC)
BPn = np.array(NPV_BP)
BSn = np.array(NPV_BS)
VLn = np.array(NPV_VL)

def ReturnData():
	return (NPV_BC, NPV_BP, NPV_BS, NPV_VL)

def ReturnNPArrayData():
	return (BCn,BPn,BSn,VLn)

def WriteHistgram():
	plt.hist(BCn)
	plt.hist(BPn)
	plt.hist(BSn)
	plt.hist(VLn)


	plt.title("Histgram")
	plt.xlabel("NPV[USD]")
	plt.ylabel("Frequency")
	plt.legend(['Capesize','Panamax','Supramax','VLCC'])
	plt.show()

def CoefficientAnalysis():
	print "------------About average and standard----------------"
	print 'BulkCapesizeNPV: avg=' + str(np.average(BCn)) + " standard=" + str(np.std(BCn))
	print 'BulkPanamaxNPV : avg=' + str(np.average(BPn)) + " standard=" + str(np.std(BPn))
	print 'BulkSupramaxNPV: avg=' + str(np.average(BSn)) + " standard=" + str(np.std(BSn))
	print 'VLCCNPV        : avg=' + str(np.average(VLn)) + " standard=" + str(np.std(VLn))
	print "------------About correlation coefficient-------------"
	print "Capesize and Panamax : " + str(np.corrcoef(BCn, BPn)[0,1])
	print "Capesize and Supramax: " + str(np.corrcoef(BCn, BSn)[0,1])
	print "Panamax and Supramax : " + str(np.corrcoef(BPn, BSn)[0,1])
	print "VLCC and Capesize    : " + str(np.corrcoef(VLn, BCn)[0,1])
	print "VLCC and Panamax     : " + str(np.corrcoef(VLn, BPn)[0,1])
	print "VLCC and Supramax    : " + str(np.corrcoef(VLn, BSn)[0,1])

CoefficientAnalysis()
# WriteHistgram()



