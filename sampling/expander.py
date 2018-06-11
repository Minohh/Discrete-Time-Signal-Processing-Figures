import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(9, 3), dpi=120)
ax1, ax2 = fig.subplots(1, 2)

f = lambda x:.3*np.sin(.3*x+1)+.6*np.sin(.1*(x+1))+2+.02*x
g = lambda x: np.where(x%3==0, 1, 0)
x1 = np.arange(-30, 30, 1)
x2 = np.arange(-30, 30, 3)

x3 = np.arange(-6, 7, 1)

ax1.set_xlim(-20, 20)
ax1.set_ylim(0, 4)
#ax1.xaxis.set_ticks()
markers1, stemlines1, baseline1 = ax1.stem(x1, f(x1))
markers2, stemlines2, baseline2 = ax1.stem(x3, f(x3))
plt.setp(markers1, 'markersize', 3)
plt.setp(markers2, 'color', 'r', 'markersize', 3)
plt.setp(stemlines2, 'color', 'r', 'linewidth', 1)
ax1.annotate(r"$x[n]$", xy=(0, 0), xytext=(-18, 3.5))

ax2.set_xlim(-20, 20)
ax2.set_ylim(0, 4)
#ax1.xaxis.set_ticks()
markers2, stemlines2, baseline2 = ax2.stem(x1, f(x1/3)*g(x1))
plt.setp(markers2, 'color', 'r', 'markersize', 3)
plt.setp(stemlines2, 'color', 'r', 'linewidth', 1)
ax2.annotate(r"$x_e[n]$", xy=(0, 0), xytext=(-18, 3.5))

plt.show()
fig.savefig("expander.png", format='png')
