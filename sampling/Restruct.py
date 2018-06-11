import numpy as np
import matplotlib.pyplot as plt


def NyquistRestruct(samples_x, samples_y, f, T, ax=None):
    x = np.arange(-10, 10, .1)
    sumY = 0
    n = 0
    for sample_x in samples_x:
        y1 = f(x-sample_x, 1.0/T)*samples_y[n]
        sumY = sumY + y1
        n += 1
        if ax is not None:
            ax.plot(x, y1, color='C0', linestyle=':')
            ax.fill_between(x, 0, y1, facecolor='#999999', alpha=.5)

    return x, sumY

f = lambda t, rate: np.sinc(t*rate)
T=2

samplex = np.arange(-6, 8, T)
sampley = np.random.rand(*samplex.shape)+1

fig = plt.figure(figsize=(9,3), dpi=120)
ax1, ax2 = fig.subplots(1, 2)

ax1.set_ylim(-.2, 3)
ax1.set_xlim(-6, 6)
ax1.xaxis.set_ticks([-3*T, -2*T, -1*T, 0, 1*T, 2*T, 3*T])
ax1.xaxis.set_ticklabels(["-3T", "-2T", "-T", "0", "T", "2T", "3T"])
ax1.yaxis.set_ticks([])
ax1.stem(samplex, sampley, markerfmt='^')
print sampley
x1, y1 = NyquistRestruct(samplex, sampley, f, T)
ax1.plot(x1, y1)
ax1.fill_between(x1, 0, y1, facecolor='#999999', alpha=.5)

ax2.set_ylim(-.2, 3)
ax2.set_xlim(-6, 6)
ax2.xaxis.set_ticks([-3*T, -2*T, -1*T, 0, 1*T, 2*T, 3*T])
ax2.xaxis.set_ticklabels(["-3T", "-2T", "-T", "0", "T", "2T", "3T"])
ax2.yaxis.set_ticks([])
x2, y2 = NyquistRestruct(samplex, sampley, f, T, ax2)
ax2.plot(x2, y2)
#ax2.annotate(r"$\Omega_s < 2\Omega_N$", xy=(0, 0), xytext=(-1, 2))

plt.show()
fig.savefig("Restruct.png", format='png')
