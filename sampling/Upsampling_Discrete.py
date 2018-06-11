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

f = lambda x: np.where(np.abs(x)<=1, 1, 0)
#T and L tipical value is (2, 1) or (4, 2)
# T is period in spectrum
T = 4
# g for upsampling, L is the down rate
g = lambda x: np.where(x<=-1, 0, np.where(x<0, x+1, np.where(x<1, 1-x, 0)))
L = 2
g2 = lambda x:g(.5*x)
lowpass = lambda x: np.where(abs(x)>2, 0, 1)

fig = plt.figure(figsize=(9,6), dpi=120)
(ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)

axesCross(ax1)
ax1.set_ylim(-.2, 4)
ax1.set_xlim(-5, 5)
ax1.xaxis.set_ticks([-1, 0, 1])
ax1.xaxis.set_ticklabels([r"$-\Omega_N$", 0, r"$\Omega_N$"])
ax1.yaxis.set_ticks([])
ax1.xaxis.set_ticks([-4, -2, 0, 2, 4])
ax1.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
x, y = periodization(g2, 4, 10)
ax1.plot(x, y)
ax1.fill_between(x, 0, y, facecolor='#999999', alpha=.5)
ax1.annotate(r"$\frac{1}{T}$", xy=(0, 0), xytext=(-.3, 1.05))
ax1.annotate(r"$X(e^{j\omega})$", xy=(0, 0), xytext=(-5, 3))

axesCross(ax2)
ax2.set_ylim(-.2, 4)
ax2.set_xlim(-5, 5)
ax2.yaxis.set_ticks([])
ax2.xaxis.set_ticks([-4, -2, 0, 2, 4])
ax2.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
x2, y2 = periodization(g, 2, 10)
ax2.plot(x2, y2)
ax2.fill_between(x2, 0, y2, facecolor='#999999', alpha=.5)
ax2.annotate(r"$\frac{1}{T}$", xy=(0, 0), xytext=(-.3, 1.05))
ax2.annotate(r"$X_e(e^{j\omega}) = X(e^{j\omega L})$", xy=(0, 0), xytext=(-5, 3))

axesCross(ax3)
ax3.set_ylim(-.2, 4)
ax3.set_xlim(-5, 5)
ax3.yaxis.set_ticks([])
ax3.xaxis.set_ticks([-4,  -1, 0, 1, 4])
ax3.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi/L$", r"$0$", r"$\pi/L$", r"$2\pi$"])
ax3.plot(x2, y2)
ax3.fill_between(x2, 0, y2, facecolor='#999999', alpha=.5)
x3, y3 = periodization(f, 4, 10)
ax3.plot(x3, L*y3, color='r')
ax3.annotate(r"$\frac{1}{T}$", xy=(0, 0), xytext=(-.3, 1.05))
ax3.annotate(r"$L$", xy=(0, 0), xytext=(-.3, 2.05))
ax3.annotate(r"$H(e^{j\omega})$", xy=(0, 0), xytext=(-5, 3))

axesCross(ax4)
ax4.set_ylim(-.2, 4)
ax4.set_xlim(-5, 5)
ax4.yaxis.set_ticks([])
ax4.xaxis.set_ticks([-4,  -1, 0, 1, 4])
ax4.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi/L$", r"$0$", r"$\pi/L$", r"$2\pi$"])
x4, y4 = periodization(g, 4, 10)
ax4.plot(x4, L*y4)
ax4.fill_between(x4, 0, L*y4, facecolor='#999999', alpha=.5)
ax4.annotate(r"$\frac{L}{T}$", xy=(0, 0), xytext=(-.3, 2.05))
ax4.annotate(r"$X_I(e^{j\omega}) = X_e(e^{j\omega})H(e^{j\omega})$", xy=(0, 0), xytext=(-5, 3))

plt.show()
fig.savefig("UpSampling_Discrete.png", format='png')
