from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import cmath
from scipy import special


g = lambda x: 1+.3*(np.cos(x)+np.sin(3*x)+np.cos(5*x)+np.sin(x*x))
x = np.arange(-1*np.pi, 1*np.pi, np.pi/32)
y = g(x)


fig = plt.figure(figsize=(11,4), dpi=60)
ax1, ax2 = fig.subplots(1, 2)
ax1.set_ylim(0, 3)
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
ax1.annotate(r'$x_s(t)$', xy=(0, 1.2), xytext=(.7, 1.9), color='b', arrowprops=dict(arrowstyle='->', color='b'))

ax2.set_ylim(0,3)
ax2.plot(x, y, 'r', linestyle=':')
ax2.scatter(x2, y2, color='k')
ax2.annotate('x[n]', xy=(.02, 1.63), xytext=(.7, 2.2), arrowprops=dict(arrowstyle='->', color='k'))

plt.show()
fig.savefig("sampling.png")
