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

BCn = np.array(NPV_BC)
print 'BulkCapesize var = ' + str(np.var(BCn))

BPn = np.array(NPV_BP)
print 'BulkPanamax var = ' + str(np.var(BPn))

BSn = np.array(NPV_BS)
print 'BulkSupramax var = ' + str(np.var(BSn))

plt.hist(BCn,facecolor='r', edgecolor='r',bins = 150)
plt.hist(BPn,facecolor='b', edgecolor='b')
plt.hist(BSn,color = 'k')

plt.title("Bulk_Carrier")
plt.xlabel("NPV[USD]")
plt.ylabel("Frequency")
plt.legend(['Capesize','Panamax','Supramax'])
plt.show()



