import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt

mpl.rcParams.update({'font.size': 20})

fig = plt.figure(figsize=(8,6), dpi=60)
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks([-.333, 0, .1, .5, 1])
ax.xaxis.set_ticklabels([r"$-\frac{1}{3}$", "0", r'$\frac{1}{12}$', r"$\frac{1}{2}$", "1"])
ax.yaxis.set_ticks([])

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

ax.set_aspect(1)
circle_out = plt.Circle((0,0), 4.5, color='grey')
circle_in  = plt.Circle((0,0), .5, color='w')
circle_std = plt.Circle((0,0), 1, color='r', fill=False)
ax.add_artist(circle_out)
ax.add_artist(circle_in)
ax.add_artist(circle_std)

plt.plot([-.333, .5], [0, 0], marker='x', markersize=8, color='k')
plt.plot([0, .1], [0, 0], marker='o', markersize=8, color='k')

plt.figtext(.77, .45, "$\mathcal{R}e$")
plt.figtext(.53, .85, "$\mathcal{I}m$")

plt.show()
fig.savefig("Exp.png")
