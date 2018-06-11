import numpy as np
import matplotlib.pyplot as plt

def axesCross(ax):
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

def periodization(f, T, times, ax=None):
    limit = np.floor(T*times/2)
    x = np.arange(-limit, limit, .1)
    sumY = 0
    for n in np.arange(times):
        y1 = f(x-T*n)
        sumY = sumY + y1
        if ax is not None:
            ax.plot(x, y1, color='C0', linestyle=':')
            ax.fill_between(x, 0, y1, facecolor='#999999', alpha=.5)

        if n != 0:
            y2 = f(x+T*n)
            sumY = sumY + y2
            if ax is not None:
                ax.plot(x, y2, color='C0', linestyle=':')
                ax.fill_between(x, 0, y2, facecolor='#999999', alpha=.5)
    return x, sumY

fig = plt.figure(figsize=(9, 6), dpi=120)
(ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)


a = -.5
L = 5

f = lambda x: np.sin(x+1)+.6*np.sin(.1*(x+1))+2
g = lambda x: np.where(x%L==0, 1, 0)

flin = lambda x: np.where(np.abs(x)<=L, -1.0*np.abs(x)/L+1, 0)
fcu  = lambda x: np.where(np.abs(x)<=L, (a+2)*((1.0*np.abs(x)/L)**3) - (a+3)*((1.0*np.abs(x)/L)**2) + 1, \
                 np.where(np.abs(x)<=2*L, a*((1.0*np.abs(x)/L)**3) - 5*a*((1.0*np.abs(x)/L)**2) + 8*a*(1.0*np.abs(x)/L) - 4*a, \
       0))


x1 = np.arange(-30, 30, 1)
x2 = np.arange(-30, 30, 3)

x3 = np.arange(-6, 7, 1)

axesCross(ax1)
ax1.spines['left'].set_color('none')
ax1.set_xlim(-10, 10)
ax1.set_ylim(-.3, 1.5)
ax1.yaxis.set_ticks([])
markers1, stemlines1, baseline1 = ax1.stem(x1, flin(x1))
plt.setp(markers1, 'markersize', 3)
plt.setp(stemlines1, 'linewidth', 1)
plt.setp(baseline1, 'color', 'k', 'linewidth', 1)
ax1.annotate(r"$linear\ interpolator\ h_{lin}$", xy=(0, 0), xytext=(-8, 1.2))

axesCross(ax2)
ax2.spines['left'].set_color('none')
ax2.set_xlim(-10, 10)
ax2.set_ylim(-.3, 1.5)
ax2.yaxis.set_ticks([])
markers2, stemlines2, baseline2 = ax2.stem(x1, fcu(x1))
plt.setp(markers2, 'markersize', 3)
plt.setp(stemlines2, 'linewidth', 1)
plt.setp(baseline2, 'color', 'k', 'linewidth', 1)
ax2.annotate(r"$cubic\ spline\ interpolator\ h_{cu}$", xy=(0, 0), xytext=(-8, 1.2))

axesCross(ax3)
ax3.spines['left'].set_color('none')
ax3.set_xlim(-20, 20)
ax3.set_ylim(-.3, 4)
ax3.yaxis.set_ticks([])
markers3a, stemlines3a, baseline3a = ax3.stem(x1-1, np.convolve(f(x1)*g(x1), flin(x1), mode='same'))
plt.setp(markers3a, 'markersize', 3)
plt.setp(stemlines3a, 'linewidth', 1)
plt.setp(baseline3a, 'color', 'k', 'linewidth', 1)
markers3b, stemlines3b, baseline3b = ax3.stem(x1, f(x1)*g(x1))
plt.setp(markers3b, 'color', 'r', 'markersize', 3)
plt.setp(stemlines3b, 'color', 'r', 'linewidth', 1)
plt.setp(baseline3b, 'color', 'k', 'linewidth', 1)
ax3.annotate(r"$x_e[n]$", xy=(-5, 2.5), xytext=(-14, 3.1), arrowprops=dict(arrowstyle='->', color='r'), color='r')
ax3.annotate(r"$x_i[n]$", xy=(-8, 1.7), xytext=(-15, 2.2), arrowprops=dict(arrowstyle='->', color='C0'), color='C0')

axesCross(ax4)
ax4.spines['left'].set_color('none')
ax4.set_xlim(-20, 20)
ax4.set_ylim(-.3, 4)
ax4.yaxis.set_ticks([])
markers4a, stemlines4a, baseline4a = ax4.stem(x1-1, np.convolve(f(x1)*g(x1), fcu(x1), mode='same'))
plt.setp(markers4a, 'markersize', 3)
plt.setp(stemlines4a, 'linewidth', 1)
plt.setp(baseline4a, 'color', 'k', 'linewidth', 1)
markers4b, stemlines4b, baseline4b = ax4.stem(x1, f(x1)*g(x1))
plt.setp(markers4b, 'color', 'r', 'markersize', 3)
plt.setp(stemlines4b, 'color', 'r', 'linewidth', 1)
plt.setp(baseline4b, 'color', 'k', 'linewidth', 1)
ax4.annotate(r"$x_e[n]$", xy=(-5, 2.5), xytext=(-14, 3.1), arrowprops=dict(arrowstyle='->', color='r'), color='r')
ax4.annotate(r"$x_i[n]$", xy=(-8, 1.7), xytext=(-15, 2.2), arrowprops=dict(arrowstyle='->', color='C0'), color='C0')

plt.show()
fig.savefig("simple_interpolation.png", format='png')
