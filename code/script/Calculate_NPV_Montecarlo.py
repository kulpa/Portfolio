import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/Bulk')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/LNG')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/Tanker')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/Expect')

import BulkCapesize as BC
import BulkPanamax as BP
import BulkSupramax as BS
import VLCC as VL
import Oil_expectation as oe
#import Ornstein_Uhlenbeck as ou
import CalcBaltic as cb
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pylab as plt
import settings as s

NPV_BC = []
NPV_BP = []
NPV_BS = []
NPV_VL = []
m_times = 1000 # montecalro times

# motecalro for m_times
for num in range(m_times):
	oe.binomial_lattice_model()
	#ou.ornstein_uhlenbeck_model()
	cb.WriteBalticCSV()
	NPV_BC.append(BC.ReturnNPV())
	NPV_BP.append(BP.ReturnNPV())
	NPV_BS.append(BS.ReturnNPV())
	NPV_VL.append(VL.ReturnNPV())

# Convert array to np.array
BCn = np.array(NPV_BC)
BPn = np.array(NPV_BP)
BSn = np.array(NPV_BS)
VLn = np.array(NPV_VL)

BCn_return_rate = map(lambda n:n/s.BC_BUILD, BCn)
BPn_return_rate = map(lambda n:n/s.BP_BUILD, BPn)
BSn_return_rate = map(lambda n:n/s.BS_BUILD, BSn)
VLn_return_rate = map(lambda n:n/s.VLCC_BUILD, VLn)

def ReturnData():
	return (NPV_BC, NPV_BP, NPV_BS, NPV_VL)

def ReturnNPArrayData():
	return (BCn_return_rate,BPn_return_rate,BSn_return_rate,VLn_return_rate)
	#return (map(lambda n:n/s.BC_BUILD, BCn),map(lambda n:n/s.BP_BUILD, BPn),map(lambda n:n/s.BS_BUILD, BSn))

	#map(lambda n:n/s.BC_BUILD, BCn)

def WriteNPVHistgram():
	# plt.hist(VLn, range=(-1*10**8, 3*10**8),bins=1000,histtype='stepfilled')
	# plt.hist(BCn, range=(-1*10**8, 3*10**8),bins=1000,histtype='stepfilled')
	# plt.hist(BPn, range=(-1*10**8, 3*10**8),bins=1000,histtype='stepfilled')
	# plt.hist(BSn, range=(-1*10**8, 3*10**8),bins=1000,histtype='stepfilled')

	#multi=np.array(np.vstack((VLn, BCn, BPn, BSn)))
	# multi=[VLn,BCn,BPn,BSn]
	# print multi
	# plt.hist(multi,histtype='bar')

	plt.hist(VLn,histtype='bar')
	plt.hist(BCn,histtype='bar')
	plt.hist(BPn,histtype='bar')
	plt.hist(BSn,histtype='bar')

	plt.title("Histgram of NPV")
	plt.xlabel("NPV[USD]")
	plt.ylabel("Frequency")
	plt.legend(['VLCC','Capesize','Panamax','Supramax'])
	plt.savefig("../image/npv_hist")
	plt.show()

def WriteVLCCHistgram():
	plt.hist(VLn, color = "blue", range=(-1*10**8, 3*10**8),bins=50)

	plt.title("Histgram of VLCC NPV")
	plt.xlabel("NPV[USD]")
	plt.ylabel("Frequency")
	plt.legend(['VLCC'])
	plt.savefig("../image/npv_VLCC_hist")
	plt.show()

def WriteCapesizeHistgram():
	plt.hist(BCn, color = "green", range=(-1*10**8, 3*10**8),bins=50)

	plt.title("Histgram of Capesize NPV")
	plt.xlabel("NPV[USD]")
	plt.ylabel("Frequency")
	plt.legend(['Capesize'])
	plt.savefig("../image/npv_Capesize_hist")
	plt.show()

def WritePanamaxHistgram():
	plt.hist(BPn, color = "red", range=(-1*10**8, 3*10**8),bins=50)

	plt.title("Histgram of Panamax NPV")
	plt.xlabel("NPV[USD]")
	plt.ylabel("Frequency")
	plt.legend(['Panamax'])
	plt.savefig("../image/npv_Panamax_hist")
	plt.show()

def WriteSupramaxHistgram():
	plt.hist(BSn, color = "cyan", range=(-1*10**8, 3*10**8),bins=50)

	plt.title("Histgram of Supramax NPV")
	plt.xlabel("NPV[USD]")
	plt.ylabel("Frequency")
	plt.legend(['Supramax'])
	plt.savefig("../image/npv_Supramax_hist")
	plt.show()

def WriteReturnHistgram():
	plt.hist(VLn_return_rate)
	plt.hist(BCn_return_rate)
	plt.hist(BPn_return_rate)
	plt.hist(BSn_return_rate)

	plt.title("Histgram of Return rate")
	plt.xlabel("NPV_Return")
	plt.ylabel("Frequency")
	plt.legend(['VLCC','Capesize','Panamax','Supramax'])
	plt.savefig("../image/return_hist")
	plt.show()

def WriteReVLCCHistgram():
	plt.hist(VLn_return_rate, color = "blue", range=(-0.5, 2),bins=50)

	plt.title("Histgram of VLCC Return rate")
	plt.xlabel("NPV_Return")
	plt.ylabel("Frequency")
	plt.legend(['VLCC'])
	plt.savefig("../image/npv_Re_VLCC_hist")
	plt.show()

def WriteReCapesizeHistgram():
	plt.hist(BCn_return_rate, color = "green", range=(-0.5, 2),bins=50)

	plt.title("Histgram of Capesize Return rate")
	plt.xlabel("NPV_Return")
	plt.ylabel("Frequency")
	plt.legend(['Capesize'])
	plt.savefig("../image/npv_Re_Capesize_hist")
	plt.show()

def WriteRePanamaxHistgram():
	plt.hist(VLn_return_rate, color = "red", range=(-0.5, 2),bins=50)

	plt.title("Histgram of Panamax Return NPV")
	plt.xlabel("NPV_Return")
	plt.ylabel("Frequency")
	plt.legend(['Panamax'])
	plt.savefig("../image/npv_Re_Panamax_hist")
	plt.show()

def WriteReSupramaxHistgram():
	plt.hist(BSn_return_rate, color = "cyan", range=(-0.5, 2),bins=50)

	plt.title("Histgram of Supramax Return NPV")
	plt.xlabel("NPV_Return")
	plt.ylabel("Frequency")
	plt.legend(['Supramax'])
	plt.savefig("../image/npv_Re_Supramax_hist")
	plt.show()

def CoefficientAnalysis():
	print "------------About average and standard----------------"
	print 'BulkCapesizeNPV: avg=' + str(np.average(BCn)) + " standard=" + str(np.std(BCn))
	print 'BulkPanamaxNPV : avg=' + str(np.average(BPn)) + " standard=" + str(np.std(BPn))
	print 'BulkSupramaxNPV: avg=' + str(np.average(BSn)) + " standard=" + str(np.std(BSn))
	print 'VLCCNPV        : avg=' + str(np.average(VLn)) + " standard=" + str(np.std(VLn))
	print "------------Return rate-------------------------------"
	print 'BulkCapesizeReturn: avg=' + str(np.average(BCn_return_rate)) + " standard=" + str(np.std(BCn_return_rate))
	print 'BulkPanamaxReturn : avg=' + str(np.average(BPn_return_rate)) + " standard=" + str(np.std(BPn_return_rate))
	print 'BulkSupramaxReturn: avg=' + str(np.average(BSn_return_rate)) + " standard=" + str(np.std(BSn_return_rate))
	print 'VLCCReturn        : avg=' + str(np.average(VLn_return_rate)) + " standard=" + str(np.std(VLn_return_rate))
	print "------------About correlation coefficient-------------"
	print "Capesize and Panamax : " + str(np.corrcoef(BCn, BPn)[0,1])
	print "Capesize and Supramax: " + str(np.corrcoef(BCn, BSn)[0,1])
	print "Panamax and Supramax : " + str(np.corrcoef(BPn, BSn)[0,1])
	print "VLCC and Capesize    : " + str(np.corrcoef(VLn, BCn)[0,1])
	print "VLCC and Panamax     : " + str(np.corrcoef(VLn, BPn)[0,1])
	print "VLCC and Supramax    : " + str(np.corrcoef(VLn, BSn)[0,1])

CoefficientAnalysis()
WriteNPVHistgram()
WriteReturnHistgram()

WriteVLCCHistgram()
WriteCapesizeHistgram()
WritePanamaxHistgram()
WriteSupramaxHistgram()

WriteReVLCCHistgram()
WriteReCapesizeHistgram()
WriteRePanamaxHistgram()
WriteReSupramaxHistgram()




