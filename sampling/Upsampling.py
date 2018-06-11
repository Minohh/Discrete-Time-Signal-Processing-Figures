import numpy as np
import matplotlib.pyplot as plt

def UpsamplingRestruct(samples_x, samples_y, f, T, L, ax=None):
    x = np.arange(-20, 20, .1)
    sumY = 0
    n = 0
    for sample_x in samples_x:
        y1 = f(x-sample_x, 1.0/T)*samples_y[n]
        sumY = sumY + y1
        n += 1
        if ax is not None:
            if sample_x==0:
                ax.plot(x, y1, color='k')
            else:
                ax.plot(x, y1, color='#888888', linestyle=':')
            ax.fill_between(x, 0, y1, facecolor='#999999', alpha=1.0/4)

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
f = lambda x: .4*np.sin(1.2*(x-3)+1)+.7*np.sin(.2*(x-2))+np.cos(.5*x)-np.sin(.7*x+3)+3
T = 2
L = 2

x = np.arange(-20, 20, T)
y = f(x)

fig = plt.figure(figsize=(9,6), dpi=120)
ax1, ax2= fig.subplots(2, 1)

xs = np.arange(-20, 20, .1)
ys = f(xs)
axesCross(ax1)
ax1.set_ylim(-2, 5)
ax1.set_xlim(-6, 6)
ax1.xaxis.set_ticks([-2*T, -T, 0, T, 2*T])
ax1.xaxis.set_ticklabels([r"$-2T$", r"$-T$", r"$0$", r"$T$", r"$2T$"])
ax1.yaxis.set_ticks([])
markers1, stemlines1, baseline1 = ax1.stem(x, y)
#plt.setp(markers, 'markerfacecolor', 'r')
plt.setp(baseline1, 'color', 'k', 'linewidth', 1)
ax1.plot(xs, ys, color='r')
x1, y1 = UpsamplingRestruct(x, y, fsinc, T, L, ax1)
ax1.annotate(r"$x[n]$",xy=(-2.05, 2.45), xytext=(-3.5, 2.5), arrowprops=dict(arrowstyle='->', color='C0'), color='C0')
ax1.annotate(r"$x_c(t)=\sum_{k=-\infty}^{\infty}x[k]\frac{sin[\pi(t-kT)/T]}{\pi(t-kT)/T}$",xy=(-1, 3.2), xytext=(-5.5, 4), color='r', arrowprops=dict(arrowstyle='->', color='r'))
ax1.annotate(r"$x[0]\frac{sin[\pi(t-0T)/T]}{\pi(t-0T)/T}$",xy=(2.7, -.7), xytext=(.2, -1.9), color='k', arrowprops=dict(arrowstyle='->', color='k'))
#ax1.annotate(r"$X_d(e^{j\omega})$",xy=(0, 0), xytext=(-4, 1.3))
#ax1.annotate(r"$\frac{1}{MT}$",xy=(0, 0), xytext=(-.7, 1.0/2+.05))

axesCross(ax2)
ax2.set_ylim(-2, 5)
ax2.set_xlim(-6, 6)
ax2.xaxis.set_ticks([-4*T/L, -2*T/L, 0, 2*T/L, 4*T/L])
ax2.xaxis.set_ticklabels([r"$-4T/L$", r"$-2T/L$", r"$0$", r"$2T/L$", r"$4T/L$"])
ax2.yaxis.set_ticks([])
#ax1.yaxis.set_ticklabels([r"$\frac{1}{MT}$"])
#x1, y1 = periodization(g2, 2*2, 10)
x2 = np.arange(-20, 20, 1.0*T/L)
y2 = f(x2)
markers2, stemlines2, baseline2 = ax2.stem(x2, y2)
plt.setp(baseline2, 'color', 'k', 'linewidth', 1)
#plt.setp(markers2, 'markerfacecolor', 'r')
#plt.setp(stemlines2, 'color', 'r')
ax2.plot(xs, ys, color='r')
ax2.annotate(r"$L=2$",xy=(0, 0), xytext=(-5.9, 5))
ax2.annotate(r"$x_c(t)$",xy=(-3.5, 1.6), xytext=(-5, 2.5), arrowprops=dict(arrowstyle='->', color='r'), color='r')
ax2.annotate(r"$x_i[n]$",xy=(-2, 2.7), xytext=(-3, 4), arrowprops=dict(arrowstyle='->', color='C0'), color='C0')

plt.show()
fig.savefig("Upsampling.png", format='png')
