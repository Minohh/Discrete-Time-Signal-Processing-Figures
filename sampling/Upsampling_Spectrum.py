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
#T and L tipical value is (2, 1) or (4, 2)
# T is period in spectrum
T = 4
# g for upsampling, L is the down rate
g = lambda x: np.where(x<=-1, 0, np.where(x<0, x+1, np.where(x<1, 1-x, 0)))
L = 2
g2 = lambda x:g(.5*L*x)
lowpass = lambda x: np.where(abs(x)>2, 0, 1)

x = np.arange(-10, 10, .1)
y = g(x)

fig = plt.figure(figsize=(9,6), dpi=120)
(ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)

axesCross(ax1)
ax1.set_ylim(-.2, 4)
ax1.set_xlim(-5, 5)
ax1.xaxis.set_ticks([-1, 0, 1])
ax1.xaxis.set_ticklabels([r"$-\Omega_N$", 0, r"$\Omega_N$"])
ax1.yaxis.set_ticks([])
ax1.plot(x, y)
ax1.fill_between(x, 0, y, facecolor='#999999', alpha=.5)
ax1.annotate(r"$\Omega_N = \pi/T$", xy=(0, 0), xytext=(1, 2))
ax1.annotate("1", xy=(0, 0), xytext=(-.3, 1.05))
ax1.annotate(r"$X_c(j\Omega)$", xy=(0, 0), xytext=(-5, 3))

axesCross(ax2)
ax2.set_ylim(-.2, 4)
ax2.set_xlim(-5, 5)
if 2*T>5:
    ax2.xaxis.set_ticks([-T, 0, T])
    ax2.xaxis.set_ticklabels([r"$-2L\pi/T$", 0, r"$2L\pi/T$"])
else:
    ax2.xaxis.set_ticks([-2*T, -T, 0, T, 2*T])
    ax2.xaxis.set_ticklabels([r"$-4\pi/T$", r"$-2\pi/T$", 0, r"$2\pi/T$", r"$4\pi/T$"])
ax2.yaxis.set_ticks([])
xS = np.arange(-20, 20, T)
markers, stemlines, baseline = ax2.stem(xS, L*np.full(xS.shape, 1), markerfmt='^')
plt.setp(markers, 'color', 'r', 'linewidth', 1)
plt.setp(baseline, 'color', 'k', 'linewidth', 1)
plt.setp(stemlines, 'color', 'r')
if L!=1:
    ax2.annotate(r"$S_i(j\Omega) = \frac{L}{T}\sum_{k=-\infty}^{\infty}\delta\left[j\left(\Omega-\frac{2\pi k}{T/L}\right)\right]$", xy=(0, 0), xytext=(-5, 3))
    ax2.annotate(r"$T_i = T/L$", xy=(0, 0), xytext=(-5, 3.7))
    ax2.annotate(r"$\frac{L}{T}$",xy=(0, 0), xytext=(-.4, L+.05))
else:
    ax2.annotate(r"$S(j\Omega) = \frac{1}{T}\sum_{k=-\infty}^{\infty}\delta\left[j\left(\Omega-\frac{2\pi k}{T}\right)\right]$", xy=(0, 0), xytext=(-5, 3))
    ax2.annotate(r"$\frac{1}{T}$",xy=(0, 0), xytext=(-.4, L+.05))

axesCross(ax3)
ax3.set_ylim(-.2, 4)
ax3.set_xlim(-5, 5)
if 2*T>5:
    ax3.xaxis.set_ticks([-T, -1, 0, 1, T])
    ax3.xaxis.set_ticklabels([r"$-2L\pi/T$", r"$-\pi/T$", 0, r"$\pi/T$", r"$2L\pi/T$"])
else:
    ax3.xaxis.set_ticks([-2*T, -T, 0, T/2.0, T, 2*T])
    ax3.xaxis.set_ticklabels([r"$-4\pi/T$", r"$-2\pi/T$", r"$0$", r"$\pi/T$", r"$2\pi/T$", r"$4\pi/T$"])
ax3.yaxis.set_ticks([])
#ax3.yaxis.set_ticklabels([r"$\frac{1}{MT}$"])
x1, y1 = periodization(g, T, 10)
ax3.plot(x1, L*y1)
ax3.fill_between(x1, 0, L*y1, facecolor='#999999', alpha=.5)
#ax3.annotate(r"$M=2$",xy=(0, 0), xytext=(-4, 1))
if L!=1:
    ax3.annotate(r"$X_{si}(j\Omega) = \frac{L}{T}\sum_{k=-\infty}^{\infty}X_c\left[j\left(\Omega-\frac{2\pi k}{T/L}\right)\right]$",xy=(0, 0), xytext=(-5, 3))
    ax3.annotate(r"$\frac{L}{T}$",xy=(0, 0), xytext=(-.4, L+.05))
else:
    ax3.annotate(r"$X_s(j\Omega) = \frac{1}{T}\sum_{k=-\infty}^{\infty}X_c\left[j\left(\Omega-\frac{2\pi k}{T}\right)\right]$",xy=(0, 0), xytext=(-5, 3))
    ax3.annotate(r"$\frac{1}{T}$",xy=(0, 0), xytext=(-.4, L+.05))
ax3.annotate(r"$\Omega$",xy=(0, 0), xytext=(4.9, -.3))

axesCross(ax4)
ax4.set_ylim(-.2, 4)
ax4.set_xlim(-5, 5)
if L!=1:
    ax4.xaxis.set_ticks([-4, -2, 0, 1, 2, 4])
    ax4.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi/L$", r"$\pi$", r"$2\pi$"])
else:
    ax4.xaxis.set_ticks([-4, -2, 0, 2, 4])
    ax4.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
ax4.yaxis.set_ticks([])
#ax4.yaxis.set_ticklabels([r"$\frac{1}{MT}$"])
x2, y2 = periodization(g2, 4, 10)
ax4.plot(x2, L*y2)
ax4.fill_between(x2, 0, L*y2, facecolor='#999999', alpha=.5)
#ax4.annotate(r"$M=3$", xy=(0, 0), xytext=(-4, 1))
if L!=1:
    ax4.annotate(r"$X_i(e^{j\omega}) = \frac{L}{T}\sum_{k=-\infty}^{\infty}X_c\left[j\left(\frac{\omega}{T/L}-\frac{2\pi k}{T/L}\right)\right]$",xy=(0, 0), xytext=(-5, 3))
    ax4.annotate(r"$\frac{L}{T}$", xy=(0, 0), xytext=(-.4, L+.05))
    ax4.annotate(r"$\omega = T\Omega/L$", xy=(0, 0), xytext=(4.8, -.3))
else:
    ax4.annotate(r"$X(e^{j\omega}) = \frac{1}{T}\sum_{k=-\infty}^{\infty}X_c\left[j\left(\frac{\omega}{T}-\frac{2\pi k}{T}\right)\right]$",xy=(0, 0), xytext=(-5, 3))
    ax4.annotate(r"$\frac{1}{T}$", xy=(0, 0), xytext=(-.4, L+.05))
    ax4.annotate(r"$\omega = T\Omega$",xy=(0, 0), xytext=(4.8, -.3))
#ax4.plot(x2, np.full(x2.shape, 0), color='w', linewidth=2)

plt.show()
fig.savefig("UpSampling_Spectrum2.png", format='png')
