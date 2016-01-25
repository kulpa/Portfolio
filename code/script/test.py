import numpy as np
import matplotlib.pyplot as plt
#import scikits.statsmodels.api as sm
import statsmodels.api as sm
from statsmodels.tsa.api import VAR 

from scipy.signal import lfilter

mdata = sm.datasets.macrodata.load().data
mdata = mdata[['realgdp','realcons','realinv']]
names = mdata.dtype.names
data = mdata.view((float,3))
data = np.diff(np.log(data), axis=0)
model = VAR(data, names=names)
res = model.fit(2)

res.plot_sample_acorr()

irf = res.irf(10) # 10 periods
irf.plot()
plt.show()

res.plot_forecast(5)

res.fevd().plot()
plt.show()
