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

f = lambda x: np.where(x<=-1, 0, np.where(x<0, x+1, np.where(x<1, 1-x, 0)))
# g for downsampling, M is the down rate
g = lambda x,M: np.where(x<=-M, 0, np.where(x<0, 1.0/(M**2)*x+1.0/M, np.where(x<M, 1.0/M-1.0/(M**2)*x, 0)))
#g2 = lambda x:g(x, 2)
g3 = lambda x:g(x, 3)
lowpass = lambda x: np.where(abs(x)>2, 0, 1)
g_filter = lambda x: g3(x)*lowpass(x)

x = np.arange(-10, 10, .02)
y = g_filter(x)
y3 = g3(x)

fig = plt.figure(figsize=(9,3), dpi=120)
ax1, ax2 = fig.subplots(1, 2)

axesCross(ax1)
l1 = 1.5*lowpass(x)
ax1.set_ylim(-.2, 2.2)
ax1.set_xlim(-6, 6)
ax1.xaxis.set_ticks([-2, 0, 2])
ax1.xaxis.set_ticklabels([r"$-\frac{\pi}{MT}$", r"$0$", r"$\frac{\pi}{MT}$"])
ax1.yaxis.set_ticks([])
ax1.plot(x, y3, linestyle=':')
ax1.plot(x, l1, color='C1')
ax1.plot(x, y)
ax1.fill_between(x, 0, y, facecolor='r')
ax1.annotate(r"$MT$", xy=(0, 0), xytext=(-.7, 1.55))
ax1.annotate(r"$\frac{1}{MT}$", xy=(0, 0), xytext=(-.7, 1.0/3+.05))
ax1.annotate(r"$M=3$", xy=(0, 0), xytext=(-4.5, 1))

axesCross(ax2)
ax2.set_ylim(-.2, 2)
ax2.set_xlim(-6, 6)
ax2.xaxis.set_ticks([-4, -2, 0, 2, 4])
ax2.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
ax2.yaxis.set_ticks([])
#ax2.yaxis.set_ticklabels([r"$\frac{1}{MT}$"])
x1, y1 = periodization(g_filter, 2*2, 10)
ax2.plot(x1, y1)
ax2.fill_between(x1, 0, y1, facecolor='#999999', alpha=.5)
ax2.annotate(r"$M=3$",xy=(0, 0), xytext=(-4, 1))
ax2.annotate(r"$\tilde{X}_d(e^{j\omega})$",xy=(0, 0), xytext=(-4, 1.3))
ax2.annotate(r"$\frac{1}{MT}$",xy=(0, 0), xytext=(-.7, 1.0/3+.05))

plt.show()
fig.savefig("DownSampling_filter_M.png", format='png')
