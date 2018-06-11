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
ax1= fig.subplots(1, 1)

axesCross(ax1)
#ax1.spines['left'].set_color('none')
ax1.set_xlim(-np.pi, np.pi)
ax1.yaxis.set_ticks([])
ax1.xaxis.set_ticks([-np.pi, -4*np.pi/L, -2*np.pi/L, -np.pi/L, 0, np.pi/L, 2*np.pi/L, 4*np.pi/L, np.pi])
ax1.xaxis.set_ticklabels([r"$-\pi$", r"$-4\pi/L$", r"$-2\pi/L$", r"$-\pi/L$", 0, r"$\pi/L$", r"$2\pi/L$", r"$4\pi/L$", r"$\pi$"])
x_s1, y_s1 = dtft(x1, flin(x1))
ax1.plot(x_s1, np.abs(y_s1))
ax1.plot(x_s1, f(x_s1), color='C1')
ax1.annotate("L = 5", xy=(0, 0), xytext=(-3, 4.5))
ax1.annotate(r"$Upsampling\ Lowpass\ filter\ H_i(e^{j\omega})$", xy=(.65, 3.5), xytext=(1.2, 3.6), arrowprops=dict(arrowstyle='->', color='C1'), color='C1')
ax1.annotate(r"$linear\ interpolator\ H_{lin}(e^{j\omega})$", xy=(.8, 1.7), xytext=(1.4, 2.6), arrowprops=dict(arrowstyle='->', color='C0'), color='C0')
ax1.annotate("L", xy=(0, 0), xytext=(-.08, 5.15))

plt.show()
fig.savefig("simple_interpolation_lowpass.png", format='png')
