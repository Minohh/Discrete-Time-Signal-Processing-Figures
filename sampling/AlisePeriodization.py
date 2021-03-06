import numpy as np
import matplotlib.pyplot as plt


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
x = np.arange(-10, 10, .1)
y = f(x)

fig = plt.figure(figsize=(9,3), dpi=120)
ax1, ax2 = fig.subplots(1, 2)

ax1.set_ylim(-.2, 3)
ax1.set_xlim(-6, 6)
ax1.xaxis.set_ticks([-7.5, -5, -2.5, 0, 2.5, 5, 7.5])
ax1.xaxis.set_ticklabels([r"$-3\Omega_s$", r"$-2\Omega_s$", r"$-\Omega_s$", r"$0$", r"$\Omega_s$", r"$2\Omega_s$", r"$3\Omega_s$"])
ax1.yaxis.set_ticks([1])
ax1.yaxis.set_ticklabels([r"$\frac{1}{T}$"])
x1, y1 = periodization(f, 2.5, 10)
ax1.plot(x1, y1)
ax1.fill_between(x1, 0, y1, facecolor='#999999', alpha=.5)
ax1.annotate(r"$\Omega_s > 2\Omega_N$",xy=(0, 0), xytext=(-1, 2))

ax2.set_ylim(-.2, 3)
ax2.set_xlim(-6, 6)
ax2.xaxis.set_ticks([0, 1.5, 3, 4.5])
ax2.xaxis.set_ticklabels([r"$0$", r"$\Omega_s$", r"$2\Omega_s$", r"$3\Omega_s$"])
ax2.yaxis.set_ticks([1])
ax2.yaxis.set_ticklabels([r"$\frac{1}{T}$"])
ax2.annotate(r"$\Omega_s - \Omega_N$", xy=(.5, 0), xytext=(-2.6, -.5), arrowprops=dict(arrowstyle='->'))
x2, y2 = periodization(f, 1.5, 10, ax2)
ax2.plot(x2, y2)
ax2.annotate(r"$\Omega_s < 2\Omega_N$", xy=(0, 0), xytext=(-1, 2))
ax2.plot(x2, np.full(x2.shape, 0), color='w', linewidth=2.5)

plt.show()
fig.savefig("Alise.png", format='png')
