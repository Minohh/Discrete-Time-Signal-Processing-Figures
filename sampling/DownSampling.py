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
g2 = lambda x:g(x, 2)
g3 = lambda x:g(x, 3)
lowpass = lambda x: np.where(abs(x)>2, 0, 1)

x = np.arange(-10, 10, .1)
y = g2(x)

fig = plt.figure(figsize=(9,6), dpi=120)
(ax1, ax2),(ax3, ax4) = fig.subplots(2, 2)

axesCross(ax1)
ax1.set_ylim(-.2, 2)
ax1.set_xlim(-6, 6)
ax1.xaxis.set_ticks([-4, -2, 0, 2, 4])
ax1.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
ax1.yaxis.set_ticks([])
#ax1.yaxis.set_ticklabels([r"$\frac{1}{MT}$"])
x1, y1 = periodization(g2, 2*2, 10)
ax1.plot(x1, y1)
ax1.fill_between(x1, 0, y1, facecolor='#999999', alpha=.5)
ax1.annotate(r"$M=2$",xy=(0, 0), xytext=(-4, 1))
ax1.annotate(r"$X_d(e^{j\omega})$",xy=(0, 0), xytext=(-4, 1.3))
ax1.annotate(r"$\frac{1}{MT}$",xy=(0, 0), xytext=(-.7, 1.0/2+.05))

axesCross(ax2)
ax2.set_ylim(-.2, 2)
ax2.set_xlim(-6, 6)
ax2.xaxis.set_ticks([-4, -2, 0, 2, 4])
ax2.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
ax2.yaxis.set_ticks([])
#ax2.yaxis.set_ticklabels([r"$\frac{1}{MT}$"])
x2, y2 = periodization(g3, 2*2, 10, ax2)
ax2.plot(x2, y2)
ax2.annotate(r"$M=3$", xy=(0, 0), xytext=(-4, 1))
ax2.annotate(r"$X_d(e^{j\omega})$",xy=(0, 0), xytext=(-4, 1.3))
ax2.annotate(r"$\frac{1}{MT}$", xy=(0, 0), xytext=(-.7, 1.0/3+.05))
ax2.plot(x2, np.full(x2.shape, 0), color='w', linewidth=2)

axesCross(ax3)
l1 = 1.5*lowpass(x1)
y1_lowpass = y1*lowpass(x1)
ax3.set_ylim(-.2, 2.2)
ax3.set_xlim(-6, 6)
ax3.xaxis.set_ticks([])
ax3.yaxis.set_ticks([])
ax3.plot(x1, y1_lowpass)
ax3.plot(x1, l1, color='r')
ax3.fill_between(x1, 0, y1_lowpass, facecolor='#999999', alpha=.5)
ax3.annotate(r"$MT$", xy=(0, 0), xytext=(-.7, 1.55))
ax3.annotate(r"$\frac{1}{MT}$", xy=(0, 0), xytext=(-.7, 1.0/2+.05))
ax3.annotate(r"$M=2$", xy=(0, 0), xytext=(-4.5, 1))

axesCross(ax4)
l2 = 2*lowpass(x2)
y2_lowpass = y2*lowpass(x2)
ax4.set_ylim(-.2, 2.2)
ax4.set_xlim(-6, 6)
ax4.xaxis.set_ticks([])
ax4.yaxis.set_ticks([])
ax4.plot(x2, y2_lowpass)
ax4.plot(x2, l2, color='r')
ax4.fill_between(x2, 0, y2_lowpass, facecolor='#999999', alpha=.5)
ax4.annotate(r"$MT$", xy=(0, 0), xytext=(-.7, 1.85))
ax4.annotate(r"$\frac{1}{MT}$", xy=(0, 0), xytext=(-.7, 1.0/3+.05))
ax4.annotate(r"$M=3$", xy=(0, 0), xytext=(-4.5, 1))

plt.show()
fig.savefig("DownSampling.png", format='png')
