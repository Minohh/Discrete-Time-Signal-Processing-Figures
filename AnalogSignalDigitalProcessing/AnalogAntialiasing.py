from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

def axesCross(ax):
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.yaxis.set_ticks([])
    ax.set_xlim(-5, 5)
    ax.set_ylim(-.1, 2.2)
    ax.xaxis.set_ticks([-4, -2, 0, 2, 4])
    ax.xaxis.set_ticklabels([r"$-\frac{2\pi}{T}$", r"$-\frac{\pi}{T}$", r"$0$", r"$\frac{\pi}{T}$", r"$\frac{2\pi}{T}$"])

def periodization(f, T, times, ax=None, color='#999999'):
    limit = np.floor(T*times/2)
    x = np.arange(-limit, limit, .02)
    sumY = 0
    for n in np.arange(times):
        y1 = f(x-T*n)
        sumY = sumY + y1
        if ax is not None:
            ax.plot(x, y1, color='C0', linestyle=':')
            ax.fill_between(x, 0, y1, facecolor=color, alpha=.5)

        if n != 0:
            y2 = f(x+T*n)
            sumY = sumY + y2
            if ax is not None:
                ax.plot(x, y2, color='C0', linestyle=':')
                ax.fill_between(x, 0, y2, facecolor=color, alpha=.5)
    return x, sumY


# the tick 2 is pi
f = lambda x: np.where(np.abs(x)<2, .5*np.sqrt(4-x**2), 0)
f2 = lambda x:f(.5*x)
lowpass = lambda x: np.where(np.abs(x)<2, 1, 0)
highpass = lambda x: np.where(np.abs(x)<1, 0, np.where(np.abs(x)<2, 1, 0))
gaussian = lambda x, mu, sigma: 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-((x-mu)**2/2*sigma**2))
stdGaussian = lambda x: 2*gaussian(x, 0, .8)
lpStdGaussian = lambda x: lowpass(x)*stdGaussian(x)

fig = plt.figure(figsize=(9,6), dpi=120)
(ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)

x, y = periodization(stdGaussian, 4, 10, ax2, 'C0')
lx, ly = periodization(lowpass, 4, 10)
lpgx, lpgy = periodization(lpStdGaussian, 4, 10)
gx = np.arange(-10, 10, .02)
gy = stdGaussian(gx)
lgy = lowpass(gx)

axesCross(ax1)
ax1.plot(gx, gy)
ax1.fill_between(gx, 0, gy, color='C0', alpha=.3)
ax1.annotate(r"$X_c(j\Omega)$", xy=(0, 0), xytext=(-5, 2), color='C0')

axesCross(ax2)
ax2.plot(x, y)
ax2.fill_between(x, 0, y, color='C0', alpha=.3)
ax2.annotate(r"$X_s(j\Omega) = \frac{1}{T}\sum_{k=-\infty}^{\infty}X_c\left[j\left(\Omega-\frac{2\pi k}{T}\right)\right]$", xy=(0, 0), xytext=(-5, 2), color='C0')

axesCross(ax3)
ax3.plot(gx, gy)
ax3.fill_between(gx, 0, gy*lgy, color='C0', alpha=.3)
ax3.plot(gx, lgy, color='r')
ax3.annotate(r"$X_a(j\Omega) = X_c(j\Omega)H_{aa}(j\Omega)$", xy=(0, 0), xytext=(-5, 2), color='r')

axesCross(ax4)
ax4.plot(lpgx, lpgy)
ax4.fill_between(lpgx, 0, lpgy, color='C0', alpha=.3)
ax4.annotate(r"$X_{as}(j\Omega) = \frac{1}{T}\sum_{k=-\infty}^{\infty}X_a\left[j\left(\Omega-\frac{2\pi k}{T}\right)\right]$", xy=(0, 0), xytext=(-5, 2), color='r')

plt.show()
fig.savefig("AntiAliasing.png", format='png')
