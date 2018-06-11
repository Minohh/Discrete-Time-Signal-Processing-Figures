import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

limit = 2

fig = plt.figure(figsize=(10, 4), dpi=120)
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax1.set_xlim(-limit, limit)
ax1.set_ylim(-limit, limit)
ax1.set_zlim(0, 1)
ax2.set_xlim(-limit, limit)
ax2.set_ylim(-limit, limit)
ax2.set_zlim(0, 1)

ax1.xaxis.set_ticks([-1, 0, 1])
ax1.yaxis.set_ticks([-1, 0, 1])
ax1.zaxis.set_ticks([0, .5, 1])
ax2.xaxis.set_ticks([-1, 0, 1])
ax2.yaxis.set_ticks([-1, 0, 1])
ax2.zaxis.set_ticks([0, .25, 1])

pdf = lambda x, y: np.where(np.abs(x)<1 ,np.where(np.abs(y)<1, .25, 0), 0)
cdf = lambda x, y: .25*(np.clip(x, -1, 1)+1)*(np.clip(y, -1, 1)+1)
f = lambda x: np.where(x<-1, 0, np.where(x<1, .5*x+.5, 1))
g = lambda x: np.where(np.abs(x)<1, .25, 0)

x = np.arange(-limit, limit, .02)
y = np.arange(-limit, limit, .02)
X, Y = np.meshgrid(x, y)
ZPDF = pdf(X, Y)
ZCDF = cdf(X, Y)

static = np.full(np.size(y), limit)
zpdf = g(x)
zcdf = f(x)

ax1.plot_surface(X, Y, ZCDF, cmap=cm.copper)
ax1.plot(x, -static, zcdf)
ax1.plot(-static, y, zcdf)

ax2.plot_surface(X, Y, ZPDF, cmap=cm.copper)
ax2.plot(x, -static, zpdf)
ax2.plot(-static, y, zpdf)

fig.text(.26, .03, "CDF")
fig.text(.73, .03, "PDF")

fig.savefig("Uniform3D.png", format='png')
plt.show()
