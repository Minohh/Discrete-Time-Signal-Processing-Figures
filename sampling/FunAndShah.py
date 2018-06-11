import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.where(x<=-1, 0, np.where(x<0, x+1, np.where(x<1, 1-x, 0)))
x = np.arange(-10, 10, .1)
y = f(x)

fig = plt.figure(figsize=(9,3), dpi=120)
ax1, ax2 = fig.subplots(1, 2)
ax1.set_ylim(-.2, 3)
ax1.set_xlim(-6, 6)
ax1.plot(x, y)
ax1.fill_between(x, 0, y, facecolor='#999999', alpha=.5)
ax1.xaxis.set_ticks([-1, 0, 1])
ax1.xaxis.set_ticklabels([r"$-\Omega_N$", r"$0$", r"$\Omega_N$"])
ax1.yaxis.set_ticks([1])

x2 = np.arange(-15, 15, 1.5)
y2 = np.full(x2.shape, 1)
ax2.set_ylim(-.2, 3)
ax2.set_xlim(-6, 6)
ax2.xaxis.set_ticks([-4.5, -3, -1.5, 0, 1.5, 3, 4.5])
ax2.xaxis.set_ticklabels([r"$-3\Omega_s$", r"$-2\Omega_s$", r"$-\Omega_s$", r"$0$", r"$\Omega_s$", r"$2\Omega_s$", r"$3\Omega_s$"])
ax2.yaxis.set_ticks([1])
#ax2.annotate(r"$\Omega_s - \Omega_N$", xy=(.5, 0), xytext=(-2.6, -.44), arrowprops=dict(arrowstyle='->'))
ax2.stem(x2, y2, markerfmt='^')

plt.show()
fig.savefig("FunAndShah.png")
