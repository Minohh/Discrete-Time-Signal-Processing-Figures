import numpy as np
import matplotlib.pyplot as plt

def axesCross(ax):
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

def periodization(f, T, times, ax=None):
    limit = np.floor(T*times/2)
    x = np.arange(-limit, limit, .05)
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

#f = lambda x: np.where(np.abs(x)<=1, 1, 0)
#T and L tipical value is (2, 1) or (4, 2)
# T is period in spectrum
T = 4
# g for upsampling, L is the down rate
g = lambda x: np.where(x<=-1, 0, np.where(x<0, x+1, np.where(x<1, 1-x, 0)))
L = 2
g1 = lambda x:2*g(2*x)
g2 = lambda x:1.0/2*g(1.0/2*x)
g22 = lambda x:g2(x-4)
g23 = lambda x:g2(x-8)
g24 = lambda x:g2(x-12)
lowpass = lambda x: np.where(abs(x)>2, 0, 1)

fig = plt.figure(figsize=(9,6), dpi=120)

(ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)

f = lambda x:.3*np.sin(.3*x+1)+.6*np.sin(.1*(x+1))+2+.01*x
mod = lambda x: np.where(x%4==0, 1, 0)
x1 = np.arange(-30, 30, 1)
x2 = np.arange(-5, 6, 1)

ax1.set_xlim(-20, 20)
ax1.set_ylim(0, 4)
#ax1.xaxis.set_ticks()
markers1, stemlines1, baseline1 = ax1.stem(x1, f(x1))
markers2, stemlines2, baseline2 = ax1.stem(x1, f(x1)*mod(x1))
plt.setp(markers1, 'markersize', 3)
plt.setp(markers2, 'color', 'r', 'markersize', 3)
plt.setp(stemlines2, 'color', 'r', 'linewidth', 1)
ax1.annotate(r"$x[n]$", xy=(0, 0), xytext=(-18, 3.5))

ax2.set_xlim(-20, 20)
ax2.set_ylim(0, 4)
#ax1.xaxis.set_ticks()
markers21, stemlines21, baseline21 = ax2.stem(x1, f(x1*4))
plt.setp(markers21, 'color', 'r', 'markersize', 3, 'alpha', .3)
plt.setp(stemlines21, 'color', 'r', 'linewidth', 1, 'alpha', .3)
markers22, stemlines22, baseline22 = ax2.stem(x2, f(x2*4))
plt.setp(markers22, 'color', 'r', 'markersize', 3)
plt.setp(stemlines22, 'color', 'r', 'linewidth', 1)
ax2.annotate(r"$x_d[n]$", xy=(0, 0), xytext=(-18, 3.5))


axesCross(ax3)
ax3.set_ylim(-.2, 4)
ax3.set_xlim(-5, 5)
ax3.yaxis.set_ticks([])
ax3.xaxis.set_ticks([-4, -2, 0, 2, 4])
ax3.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
x3, y3 = periodization(g1, 4, 10)
ax3.plot(x3, y3)
ax3.fill_between(x3, 0, y3, facecolor='C0', alpha=.5)
ax3.annotate(r"$\frac{1}{T}$", xy=(0, 0), xytext=(-.3, 2.05))
ax3.annotate(r"$X(e^{j\omega})$", xy=(0, 0), xytext=(-5, 3))

axesCross(ax4)
ax4.set_ylim(-.2, 4)
ax4.set_xlim(-5, 5)
ax4.yaxis.set_ticks([])
ax4.xaxis.set_ticks([-4, -2, 0, 2, 4])
ax4.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
x41, y41 = periodization(g2, 16, 10)
ax4.plot(x41, y41)
ax4.fill_between(x41, 0, y41, facecolor='C0', alpha=.5)
x42, y42 = periodization(g22, 16, 10)
ax4.plot(x42, y42)
ax4.fill_between(x42, 0, y42, facecolor='C1', alpha=.5)
x43, y43 = periodization(g23, 16, 10)
ax4.plot(x43, y43)
ax4.fill_between(x43, 0, y43, facecolor='C2', alpha=.5)
x44, y44 = periodization(g24, 16, 10)
ax4.plot(x44, y44)
ax4.fill_between(x44, 0, y44, facecolor='C3', alpha=.5)
ax4.annotate(r"$\frac{1}{MT}$", xy=(0, 0), xytext=(-.7, .6))
ax4.annotate(r"$X_d(e^{j\omega}) = \frac{1}{M}\sum_{i=0}^{M-1}X(e^{j(\omega-2\pi i)/M })$", xy=(0, 0), xytext=(-5, 3))

fig.savefig("compressor.png", format='png')
plt.show()
