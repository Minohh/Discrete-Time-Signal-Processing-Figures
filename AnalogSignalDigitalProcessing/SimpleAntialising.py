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

def periodization(f, T, times, ax=None, color='#999999', lstyle=':'):
    limit = np.floor(T*times/2)
    x = np.arange(-limit, limit, .02)
    sumY = 0
    for n in np.arange(times):
        y1 = f(x-T*n)
        sumY = sumY + y1
        if ax is not None:
            ax.plot(x, y1, color=color, linestyle=lstyle)
            ax.fill_between(x, 0, y1, facecolor=color, alpha=.3)

        if n != 0:
            y2 = f(x+T*n)
            sumY = sumY + y2
            if ax is not None:
                ax.plot(x, y2, color=color, linestyle=lstyle)
                ax.fill_between(x, 0, y2, facecolor=color, alpha=.3)
    return x, sumY


# the tick 2 is pi
f = lambda x: np.where(np.abs(x)<1, -np.abs(x)+1, 0)
f2 = lambda x: np.where(np.abs(x)<2, -.5*np.abs(x)+1, 0)
noise = lambda x: np.where(np.abs(x)<1, 0, np.where(np.abs(x)<4.2, .2, 0))
f2 = lambda x: .4*f(.5*x)
lowpass = lambda x: np.where(np.abs(x)<1, 1, 0)
prefilter = lambda x: np.where(np.abs(x)<1, 1, np.where(np.abs(x)<3, -.5*np.abs(x)+1.5, 0))
prefilterf = lambda x: .7*f(x)*prefilter(x)
prefilternoise = lambda x: .7*noise(x)*prefilter(x)

fig = plt.figure(figsize=(9,10), dpi=120)
ax1, ax2, ax3, ax4, ax5 = fig.subplots(5, 1)

x, y = periodization(f, 4, 10)
fx = np.arange(-10, 10, .02)
fy = f(fx)
ny = noise(fx)
py = prefilter(fx)


axesCross(ax1)
ax1.plot(fx, fy)
ax1.plot(fx, ny)
ax1.plot(fx, py, color='r', linestyle='--')
ax1.fill_between(fx, 0, fy, color='C0', alpha=.3)
ax1.fill_between(fx, 0, ny, color='C1', alpha=.3)
ax1.xaxis.set_ticks([-3, -1, 0, 1, 3])
ax1.xaxis.set_ticklabels([r"$-\Omega_c$", r"$-\Omega_N$", r"$0$", r"$\Omega_N$", r"$\Omega_c$"])
ax1.annotate("Simple antialiasing filter", xy=(1.2, .9), xytext=(2, 2), color='r', arrowprops=dict(arrowstyle='->', color='r'))
ax1.annotate("High-frequency noise", xy=(2, .2), xytext=(2, 1), color='C1', arrowprops=dict(arrowstyle='->', color='C1'))
ax1.annotate("Signal", xy=(-.5, .5), xytext=(-2.5, 1), color='C0', arrowprops=dict(arrowstyle='->',color='C0'))
ax1.annotate(r"$X_c(j\Omega)$", xy=(0, 0), xytext=(-5, 1.7), color='k')
ax1.annotate(r"$1$", xy=(0, 0), xytext=(-.2, 1.1), color='k')

axesCross(ax2)
ax2.plot(fx, fy)
ax2.plot(fx, ny*py)
ax2.fill_between(fx, 0, fy, color='C0', alpha=.3)
ax2.fill_between(fx, 0, ny*py, color='C1', alpha=.3)
ax2.xaxis.set_ticks([-3, -1, 0, 1, 3])
ax2.xaxis.set_ticklabels([r"$-\Omega_c$", r"$-\Omega_N$", r"$0$", r"$\Omega_N$", r"$\Omega_c$"])
ax2.annotate(r"$X_a(j\Omega) = X_c(j\Omega)H_{aa}(j\Omega)$", xy=(0, 0), xytext=(-5, 1.7), color='k')
ax2.annotate("Signal", xy=(-.5, .5), xytext=(-2.5, 1), color='C0', arrowprops=dict(arrowstyle='->',color='C0'))
ax2.annotate("Filtered noise", xy=(2, .1), xytext=(2, 1), color='C1', arrowprops=dict(arrowstyle='->', color='C1'))
ax2.annotate(r"$1$", xy=(0, 0), xytext=(-.2, 1.1), color='k')

axesCross(ax3)
lpfx, lpfy = periodization(prefilterf, 4, 10, ax3, 'C0', '-')
lpnx, lpny = periodization(prefilternoise, 4, 10, ax3, 'C1', '-')
#ax3.plot(lpfx, lpfy)
#ax3.fill_between(lpfx, 0, lpfy, color='C0', alpha=.3)
ax3.annotate(r"$X_{as}(j\Omega) = \frac{1}{T}\sum_{k=-\infty}^{\infty}X_a\left[j\left(\Omega-\frac{2\pi k}{T}\right)\right]$", xy=(0, 0), xytext=(-5, 1.7), color='k')
ax3.annotate(r"$T =\frac{\pi}{M\Omega_N}\qquad M\Omega_N\geqslant \frac{\Omega_N+\Omega_c}{2}$", xy=(0, 0), xytext=(1, 1.3), color='k')
ax3.annotate(r"$\frac{1}{T}$", xy=(0, 0), xytext=(-.2, .8), color='k')

axesCross(ax4)
ax4.xaxis.set_ticks([-4, -2, 0, 2, 4])
ax4.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
lpfx, lpfy = periodization(prefilterf, 4, 10, ax4, 'C0', '-')
lpnx, lpny = periodization(prefilternoise, 4, 10, ax4, 'C1', '-')
lx, ly = periodization(lowpass, 4, 10)
ax4.plot(lx, ly, color='r', linestyle='--')
ax4.annotate(r"$\hat{X}(e^{j\omega}) = X_{as}(j\Omega)|_{\omega=T\Omega}$", xy=(0, 0), xytext=(-5, 1.7), color='k')
ax4.annotate("Sharp cutoff decimation filter", xy=(-1, .9), xytext=(-3, 1.3), color='r', arrowprops=dict(arrowstyle='->', color='r'))
ax4.annotate(r"$1$", xy=(0, 0), xytext=(-.2, 1.1), color='k')
ax4.annotate(r"$\frac{1}{T}$", xy=(0, 0), xytext=(-.2, .7), color='k')


axesCross(ax5)
ax5.xaxis.set_ticks([-4, -2, 0, 2, 4])
ax5.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
f2x, f2y = periodization(f2, 4, 10)
ax5.plot(f2x, f2y)
ax5.fill_between(f2x, 0, f2y, color='C0', alpha=.3)
ax5.annotate(r"$X_d(e^{j\omega}) = Downsampling\ \hat{X}(e^{j\omega})\ with\ M$", xy=(0, 0), xytext=(-5, 1.7), color='k')
ax5.annotate(r"$T_d = MT$", xy=(0, 0), xytext=(1, 1), color='k')
ax5.annotate(r"$\frac{1}{T_d}$", xy=(0, 0), xytext=(-.2, .6), color='k')


plt.show()
fig.savefig("SimpleAntiAliasing.png", format='png')
