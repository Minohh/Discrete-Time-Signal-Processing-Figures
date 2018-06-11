from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import cmath
from scipy import special


g = lambda x: np.where(abs(x)<1.5, 1, 0)
x = np.arange(-np.pi, np.pi, np.pi/32)
y = g(x)

fig = plt.figure(figsize=(6,4), dpi=60)
ax = fig.subplots()
plt.ylim(-.3, 1.3)
plt.plot(x, y, 'r', linewidth=1)
ax.fill(x, y, '#993333')
plt.figtext(0.9, 0.05, '$\omega$')
plt.figtext(0.1, 0.9, '$\mathcal{F}f$')
ax.set_xlabel("frequency")
ax.set_ylabel("fourier transform")

#plt.show()
fig.savefig("2D.png")
