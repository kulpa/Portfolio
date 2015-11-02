import numpy as np
import matplotlib.pyplot as plt
import cvxopt as opt
from cvxopt import blas, solvers
import pandas as pd
import Calculate_NPV_Montecarlo as cm
import math

## NUMBER OF ASSETS
n_assets = 4

return_vec = np.array(cm.ReturnNPArrayData())

def WriteGraph():
	plt.plot(return_vec.T, alpha=.4);
	plt.xlabel('time')
	plt.ylabel('returns')

	plt.show()

def rand_weights(n):
    ''' Produces n random weights that sum to 1 '''
    k = np.random.rand(n)
    return k / sum(k)

weight_list=[]
mean_list=[]
sigma_list=[]

def random_portfolio(returns):
    ''' 
    Returns the mean and standard deviation of returns for a random portfolio
    '''

    p = np.asmatrix(np.mean(returns, axis=1))
    w = np.asmatrix(rand_weights(returns.shape[0]))
    C = np.asmatrix(np.cov(returns))
    
    mu = w * p.T
    sigma = np.sqrt(w * C * w.T)
    
    # This recursion reduces outliers to keep plots pretty
    # if sigma > 2:
    #     return random_portfolio(returns)
    weight_list.append([round(w[0,0],3), round(w[0,1],3), round(w[0,2],3), round(w[0,3],3)])
    mean_list.append(int(mu[0,0]))
    sigma_list.append(int(sigma[0,0]))
    return mu, sigma

def optimal_portfolio(returns):
    n = len(returns)
    returns = np.asmatrix(returns)
    
    N = 100
    mus = [10**(5.0 * t/N - 1.0) for t in range(N)]
    
    # Convert to cvxopt matrices
    S = opt.matrix(np.cov(returns))
    pbar = opt.matrix(np.mean(returns, axis=1))
    
    # Create constraint matrices
    G = -opt.matrix(np.eye(n))   # negative n x n identity matrix
    h = opt.matrix(0.0, (n ,1))
    A = opt.matrix(1.0, (1, n))
    b = opt.matrix(1.0)
    
    # Calculate efficient frontier weights using quadratic programming
    portfolios = [solvers.qp(mu*S, -pbar, G, h, A, b)['x'] 
                  for mu in mus]
    ## CALCULATE RISKS AND RETURNS FOR FRONTIER
    returns = [blas.dot(pbar, x) for x in portfolios]
    risks = [np.sqrt(blas.dot(x, S*x)) for x in portfolios]
    ## CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
    m1 = np.polyfit(returns, risks, 2)
    x1 = np.sqrt(m1[2] / m1[0])
    # CALCULATE THE OPTIMAL PORTFOLIO
    wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']
    return np.asarray(wt), returns, risks

n_portfolios = 500
means, stds = np.column_stack([
    random_portfolio(return_vec) 
    for _ in xrange(n_portfolios)
])

class PointBrowser:
    """
    pass a subplot to __init__
    overwrite the yellow circle on the clicked data
    """
    def __init__(self, fig, ax):
        self.fig = fig
        self.text = ax.text(0.05, 0.95, 'selected: none',
                            transform=ax.transAxes, va='top')


        self.selected,  = ax.plot([], [], 'o', ms=12, alpha=0.4,
                                  color='yellow', visible=False)

    def onpick(self, event):
        """
        it picks up the index of clicked data

        """
        if not len(event.ind):
            return True

        ind = event.ind[0]
        x = int(event.artist.get_xdata()[ind])
        y = int(event.artist.get_ydata()[ind])
        si = sigma_list.index(int(x))
        mi = mean_list.index(int(y))
        weight = weight_list[mi]
        clicked = (x, y)
        
        self.selected.set_visible(True)
        self.selected.set_data(clicked)
        self.text.set_text(' std: %d USD \n mean: %d USD \n'%(clicked) + "kind: BC,BP,BS,VL\nweight: " + str(weight))
        self.fig.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Portfolios')
ax.plot(stds, means, 'o', markersize=5, picker=5)  # 5 points tolerance
plt.xlabel('std')
plt.ylabel('mean')

# plt.plot(stds, means, 'o', markersize=5, picker=5)
# plt.title('Portfolios')

# weights, returns, risks = optimal_portfolio(return_vec)

# plt.plot(stds, means, 'o')
# plt.ylabel('mean')
# plt.xlabel('std')
# plt.plot(risks, returns, 'y-o')
# plt.title('Portfolios')

browser = PointBrowser(fig, ax)
fig.canvas.mpl_connect('pick_event', browser.onpick)


plt.show()

# fig = plt.figure()