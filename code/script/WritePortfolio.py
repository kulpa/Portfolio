# http://blog.quantopian.com/markowitz-portfolio-optimization-2/
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

#return_vec = np.random.randn(n_assets, 1000)

def WriteGraph():
	plt.plot(return_vec.T, alpha=.4);
	plt.xlabel('time')
	plt.ylabel('returns')

	plt.show()

# def rand_weights(n):
#     ''' Produces n random weights that sum to 1 '''
#     k = np.random.randint(10,size=n)
#     k = map(float,k)
#     k = np.array(k)
#     return k / sum(k)

def rand_weights(n):
    ''' Produces n random weights that sum to 1 '''
    k = np.random.rand(n)
    return k / sum(k)


weight_list=[]
weight_random_list=[]
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
    if sigma > 2:
        return random_portfolio(returns)
    weight_list.append([round(w[0,0],3), round(w[0,1],3), round(w[0,2],3), round(w[0,3],3)])
    weight_random_list.append([round(w[0,0],3), round(w[0,1],3), round(w[0,2],3), round(w[0,3],3)])
    #weight_list.append([round(w[0,0],3), round(w[0,1],3), round(w[0,2],3)])
    mean_list.append(mu[0,0])
    sigma_list.append(sigma[0,0])
    return mu, sigma

opt_weight_list = []
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

    for x in portfolios:
        weight_list.append([round(x[0],3), round(x[1],3), round(x[2],3), round(x[3],3)])
        opt_weight_list.append([round(x[0],3), round(x[1],3), round(x[2],3), round(x[3],3)])
        #weight_list.append([round(x[0],3), round(x[1],3), round(x[2],3)]) 
    ## CALCULATE RISKS AND RETURNS FOR FRONTIER
    returns = [blas.dot(pbar, x) for x in portfolios]
    risks = [np.sqrt(blas.dot(x, S*x)) for x in portfolios]

    for re in returns:
        mean_list.append(re)

    for ri in risks:
        sigma_list.append(ri)

    ## CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
    m1 = np.polyfit(returns, risks, 2)
    x1 = np.sqrt(m1[2] / m1[0])
    # CALCULATE THE OPTIMAL PORTFOLIO
    wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']
    print "-------------------debug-------------------"
    print x1
    return np.asarray(wt), returns, risks
    #return returns, risks

n_portfolios = 2000
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
        x = event.artist.get_xdata()[ind]
        y = event.artist.get_ydata()[ind]
        si = sigma_list.index(x)
        mi = mean_list.index(y)
        weight = weight_list[mi]
        clicked = (x, y)
        
        self.selected.set_visible(True)
        self.selected.set_data(clicked)
        self.text.set_text(' std: %f\n mean: %f\n'%(clicked) + "kind: BC,BP,BS,VL\nweight: " + str(weight))
        print ' std: %f\n mean: %f\n'%(clicked) + "kind: BC,BP,BS,VL\nweight: " + str(weight)
        self.fig.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Portfolios')
ax.plot(stds, means, 'o', markersize=5, picker=5)  # 5 points tolerance
plt.xlabel('std')
plt.ylabel('mean')

# plt.plot(stds, means, 'o', markersize=5, picker=5)
# plt.title('Portfolios')

weights, returns, risks = optimal_portfolio(return_vec)
#returns, risks = optimal_portfolio(return_vec)
print "---------best portfolio-----------"
print weights
print "----------------------------------"

ax.plot(risks, returns, 'y-o', markersize=5, picker=5)
# plt.title('Portfolios')

browser = PointBrowser(fig, ax)
fig.canvas.mpl_connect('pick_event', browser.onpick)

plt.savefig("../image/portfolio")
plt.show()

def WriteOptPortfolioHistgram():
    np_opt_array = np.asarray(opt_weight_list)
    # plt.hist(np_opt_array.T[0],normed=True,bins=10)
    # plt.hist(np_opt_array.T[1],normed=True,bins=20,alpha=0.7)
    # plt.hist(np_opt_array.T[2],normed=True,bins=3)
    # plt.hist(np_opt_array.T[3],normed=True,bins=20,alpha=0.7)
    plt.hist(np.array(np_opt_array),normed=True)

    plt.title("Histgram of Optimal Portfolio")
    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.legend(['Capesize','Panamax','Supramax','VLCC'])
    plt.savefig("../image/opt_portfolio_hist")
    plt.show()

def WriteRandomPortfolioHistgram():
    np_random_array = np.asarray(weight_random_list)
    plt.hist(np_random_array.T[0])

    plt.title("Histgram of Blue dot Portfolio")
    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.legend(['Capesize'])
    plt.show()

WriteOptPortfolioHistgram()
# WriteRandomPortfolioHistgram()
# fig = plt.figure()
