from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import cmath
from scipy import special


g = lambda x: 1+.3*(np.cos(x)+np.sin(3*x)+np.cos(5*x)+np.sin(x*x))
x = np.arange(-1*np.pi, 1*np.pi, np.pi/32)
y = g(x)


fig = plt.figure(figsize=(9,3), dpi=120)
ax1, ax2 = fig.subplots(1, 2)
ax1.set_ylim(0, 3)
ax1.xaxis.set_ticks([-3, -2, -1, 0, 1, 2, 3])
ax1.xaxis.set_ticklabels(["-3T", "-2T", "-T", "0", "T", "2T", "3T"])
ax1.yaxis.set_ticks([])
ax1.plot(x, y, 'r', linewidth=1)
#ax.fill(x, y, '#993333')

x2= np.arange(-3, 4, 1)
y2= g(x2)
ax1.stem(x2, y2, markerfmt='^')

#plt.figtext(0.6, 0.6, '$x_s(t)$', color='b')
#plt.figtext(0.2, 0.6, '$x_c(t)$', color='r')
#ax.set_xlabel("frequency")
#ax.set_ylabel("fourier transform")

ax1.annotate(r'$x_c(t)$', xy=(-1.6, 1.4), xytext=(-2.5, 1.9), color='r', arrowprops=dict(arrowstyle='->', color='r'))
ax1.annotate(r'$x_s(t)$', xy=(0, 1.2), xytext=(.7, 1.9), color='C0', arrowprops=dict(arrowstyle='->', color='C0'))

ax2.set_ylim(0,3)
ax2.xaxis.set_ticks([-3, -2, -1, 0, 1, 2, 3])
ax2.xaxis.set_ticklabels(["-3T", "-2T", "-T", "0", "T", "2T", "3T"])
ax2.yaxis.set_ticks([])
ax2.plot(x, y, 'r', linestyle=':')
ax2.scatter(x2, y2, color='k')
ax2.annotate('x[n]', xy=(.02, 1.63), xytext=(.7, 2.2), arrowprops=dict(arrowstyle='->', color='k'))

plt.show()
fig.savefig("sampling.png", format='png')
