import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
from scipy.interpolate import spline

def axesCross(ax):
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

def dtft(x, y):
    if x.size!=y.size:
        print "array size not the same, x.size :"+x.size+" y.size :"+y.size
    xret = np.linspace(-np.pi, np.pi, 300)
    yret = np.full(xret.shape, 0+0j)
    n = 0
    m = 0
    for xn in xret:
        for xm in x:
            yret[n] += y[m]*(cm.exp(-1j*xn*xm))
            m += 1
        m = 0
        n += 1
    return xret, yret

a = -.5
L = 5

f = lambda x: np.where(np.abs(x)<=np.pi/L, L, 0)
g = lambda x: np.where(x%L==0, 1, 0)

flin = lambda x: np.where(np.abs(x)<=L, -1.0*np.abs(x)/L+1, 0)
fcu  = lambda x: np.where(np.abs(x)<=L, (a+2)*((1.0*np.abs(x)/L)**3) - (a+3)*((1.0*np.abs(x)/L)**2) + 1, \
                 np.where(np.abs(x)<=2*L, a*((1.0*np.abs(x)/L)**3) - 5*a*((1.0*np.abs(x)/L)**2) + 8*a*(1.0*np.abs(x)/L) - 4*a, \
       0))


x1 = np.arange(-30, 30, 1)

fig = plt.figure(figsize=(9, 3), dpi=120)
ax1, ax2= fig.subplots(1, 2)

#axesCross(ax1)
#ax1.spines['left'].set_color('none')
ax1.set_xlim(-np.pi, np.pi)
ax1.yaxis.set_ticks([L])
ax1.yaxis.set_ticklabels(["L"])
ax1.xaxis.set_ticks([-np.pi, -np.pi/L, 0, np.pi/L, np.pi])
ax1.xaxis.set_ticklabels([r"$-\pi$", r"$-\pi/L$", 0, r"$\pi/L$", r"$\pi$"])
x_s1, y_s1 = dtft(x1, flin(x1))
ax1.plot(x_s1, np.abs(y_s1))
#ax1.annotate("cubic spline interpolator", xy=(-3.1, 4.8), xytext=(-2, 4.8), arrowprops=dict(arrowstyle='-', color='r'), color='r')
#ax1.annotate("linear interpolator", xy=(-3.1, 3.8), xytext=(-2, 3.8), arrowprops=dict(arrowstyle='-', color='C0'), color='C0')
x_s2, y_s2 = dtft(x1, fcu(x1))
ax1.plot(x_s2, np.abs(y_s2), color='r', linestyle='--')
#ax1.plot(x_s1, f(x_s1), color='r')

#axesCross(ax2)
ax2.set_xlim(-np.pi, np.pi)
ax2.xaxis.set_ticks([-np.pi, -np.pi/L, 0, np.pi/L, np.pi])
ax2.xaxis.set_ticklabels([r"$-\pi$", r"$-\pi/L$", 0, r"$\pi/L$", r"$\pi$"])
x_s3, y_s3 = dtft(x1, flin(x1))
ax2.plot(x_s3, np.log(np.abs(y_s3)))
x_s4, y_s4 = dtft(x1, fcu(x1))
ax2.plot(x_s4, np.log(np.abs(y_s4)), color='r',linestyle='--')


plt.show()
fig.savefig("simple_interpolation_spectrum.png", format='png')
