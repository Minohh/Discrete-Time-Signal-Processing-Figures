import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

def GenRandomProcess(y) :
    y[0] = mu+(random.random()-.5)*sigma
    n = 1
    while n<Len :
        delta = (1.0-rho**2)*(random.random()-.5)*sigma
        y[n] = rho*(y[n-1]-mu) + mu + delta
        if y[n]> (mu+sigma):
            y[n] = y[n]-sigma
        elif y[n]< (mu-sigma):
            y[n] = y[n]+sigma
        n=n+1
    return y

def AxesCross(ax):
#    ax.spines['left'].set_position('center')
    ax.set_ylim(-.5, .5)
    ax.set_xlim(0, 100)
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('center')

fig = plt.figure(figsize=(9,6), dpi=120)
ax1, ax2, ax3, ax4 = fig.subplots(4,1)

mu = 0
sigma = 1
rho = .8
Len = 150
x = np.arange(Len)
y = np.full(x.shape, 0.0)

xnew = np.linspace(0, Len-1, 2*Len)

AxesCross(ax1)
AxesCross(ax2)
AxesCross(ax3)
AxesCross(ax4)

y = GenRandomProcess(y)
ynew = spline(x, y, xnew)
ax1.plot(xnew, ynew, linewidth=1)

y = GenRandomProcess(y)
ynew = spline(x, y, xnew)
ax2.plot(xnew, ynew, linewidth=1)

y = GenRandomProcess(y)
ynew = spline(x, y, xnew)
ax3.plot(xnew, ynew, linewidth=1)

y = GenRandomProcess(y)
ynew = spline(x, y, xnew)
ax4.plot(xnew, ynew, linewidth=1)

plt.show()
fig.savefig("GenRandomProcess.png", format='png')
