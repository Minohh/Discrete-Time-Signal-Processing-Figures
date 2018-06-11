import numpy as np
import matplotlib.pyplot as plt

def DownsamplingRestruct(samples_x, samples_y, f, T, M, ax=None):
    x = np.arange(-20, 20, .1)
    sumY = 0
    n = 0
    for sample_x in samples_x:
        y1 = f(x-sample_x, 1.0/(T*M))*samples_y[n]
        sumY = sumY + y1
        n += 1
        if ax is not None:
            if sample_x==0:
                ax.plot(x, y1, color='k')
            else:
                ax.plot(x, y1, color='#888888', linestyle=':')
            ax.fill_between(x, 0, y1, facecolor='#999999', alpha=1.0/M)

    return x, sumY

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


fsinc = lambda x, rate: np.sinc(x*rate)
f = lambda x: .4*np.sin(.12*(x-3)+1)+np.sin(.2*(x-2))+np.cos(.5*x)+np.sin(.7*x+3)+1
T = 1
M = 2
# g for downsampling, M is the down rate
g = lambda x,M: np.where(x<=-M, 0, np.where(x<0, 1.0/(M**2)*x+1.0/M, np.where(x<M, 1.0/M-1.0/(M**2)*x, 0)))
g2 = lambda x:g(x, 2)
g3 = lambda x:g(x, 3)
lowpass = lambda x: np.where(abs(x)>2, 0, 1)

x = np.arange(-20, 20, T)
y = f(x)

fig = plt.figure(figsize=(9,6), dpi=120)
ax1, ax2= fig.subplots(2, 1)

xs = np.arange(-20, 20, .1)
ys = f(xs)
axesCross(ax1)
ax1.set_ylim(-2, 5)
ax1.set_xlim(-6, 6)
ax1.xaxis.set_ticks([-4, -2, 0, 2, 4])
ax1.xaxis.set_ticklabels([r"$-4T$", r"$-2T$", r"$0$", r"$2T$", r"$4T$"])
ax1.yaxis.set_ticks([])
markers, stemlines, baseline = ax1.stem(x, y)
#plt.setp(markers, 'markerfacecolor', 'r')
plt.setp(baseline, 'color', 'k', 'linewidth', 1)
ax1.plot(xs, ys, color='k')
ax1.annotate(r"$x_c(t)$",xy=(-2.5, 1.8), xytext=(-4, 4), arrowprops=dict(arrowstyle='->', color='k'), color='k')
ax1.annotate(r"$x[n]$",xy=(-1.05, 2.4), xytext=(-2.3, 4), arrowprops=dict(arrowstyle='->', color='C0'), color='C0')
#ax1.annotate(r"$X_d(e^{j\omega})$",xy=(0, 0), xytext=(-4, 1.3))
#ax1.annotate(r"$\frac{1}{MT}$",xy=(0, 0), xytext=(-.7, 1.0/2+.05))

axesCross(ax2)
ax2.set_ylim(-2, 5)
ax2.set_xlim(-6, 6)
ax2.xaxis.set_ticks([-4, -2, 0, 2, 4])
ax2.xaxis.set_ticklabels([r"$-2MT$", r"$-MT$", r"$0$", r"$MT$", r"$2MT$"])
ax2.yaxis.set_ticks([])
#ax1.yaxis.set_ticklabels([r"$\frac{1}{MT}$"])
#x1, y1 = periodization(g2, 2*2, 10)
markers, stemlines, baseline = ax2.stem(x, y)
plt.setp(baseline, 'color', 'k', 'linewidth', 1)
x1, y1 = DownsamplingRestruct(x, y, fsinc, T, M, ax2)
ax2.plot(x1, y1, color='C1')
ax2.plot(x1, y1/M, color='r')
ax2.annotate(r"$M=2$",xy=(0, 0), xytext=(-5.9, 5))
ax2.annotate(r"$M\tilde{x}_d(t)=\sum_{k=-\infty}^{\infty}x[k]\frac{sin[\pi(t-kT)/MT]}{\pi(t-kT)/MT}$",xy=(1, 3), xytext=(2, 3), color='C1', arrowprops=dict(arrowstyle='->', color='C1'))
ax2.annotate(r"$\tilde{x}_d(t)=\sum_{k=-\infty}^{\infty}x[k]\frac{sin[\pi(t-kT)/MT]}{\pi(t-kT)/MT}/M$",xy=(-2, 2.2), xytext=(-5.9, 3.5), color='r', arrowprops=dict(arrowstyle='->', color='r'))
ax2.annotate(r"$x[0]\frac{sin[\pi(t-0T)/MT]}{\pi(t-0T)/MT}$",xy=(2.7, -.7), xytext=(.2, -1.9), color='k', arrowprops=dict(arrowstyle='->', color='k'))
#ax1.annotate(r"$\frac{1}{MT}$",xy=(0, 0), xytext=(-.7, 1.0/2+.05))

plt.show()
fig.savefig("Downsampling_Restruction.png", format='png')
