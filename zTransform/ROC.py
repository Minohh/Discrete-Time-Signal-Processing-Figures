import numpy as np
from matplotlib import pyplot as plt


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True, sharey=True)


ax1.spines['left'].set_position('center')
ax1.spines['bottom'].set_position('center')
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks([1])
ax1.yaxis.set_ticks([0])

ax2.spines['left'].set_position('center')
ax2.spines['bottom'].set_position('center')
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')
ax2.xaxis.set_ticks([1])
ax2.yaxis.set_ticks([0])

ax3.spines['left'].set_position('center')
ax3.spines['bottom'].set_position('center')
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.xaxis.set_ticks_position('bottom')
ax3.yaxis.set_ticks_position('left')
ax3.xaxis.set_ticks([1])
ax3.yaxis.set_ticks([0])

ax4.spines['left'].set_position('center')
ax4.spines['bottom'].set_position('center')
ax4.spines['right'].set_color('none')
ax4.spines['top'].set_color('none')
ax4.xaxis.set_ticks_position('bottom')
ax4.yaxis.set_ticks_position('left')
ax4.xaxis.set_ticks([1])
ax4.yaxis.set_ticks([0])

ax1.set_aspect(1)
ax1.set_ylim(-3, 3)
ax1.set_xlim(-3, 3)


circle1_1 = plt.Circle((0, 0), 4.5, color='#445566')
ax1.add_artist(circle1_1)
circle1_2 = plt.Circle((0, 0), 1.5, color='w')
ax1.add_artist(circle1_2)
circle1_0 = plt.Circle((0, 0), 1, color='r', fill=False)
ax1.add_artist(circle1_0)

circle2 = plt.Circle((0, 0), 1.5, color='#445566')
ax2.add_artist(circle2)
circle2_0 = plt.Circle((0, 0), 1, color='r', fill=False)
ax2.add_artist(circle2_0)

circle3_1 = plt.Circle((0, 0), 1.5, color='#445566')
ax3.add_artist(circle3_1)
circle3_2 = plt.Circle((0, 0), 0.8, color='w')
ax3.add_artist(circle3_2)
circle3_0 = plt.Circle((0, 0), 1, color='r', fill=False)
ax3.add_artist(circle3_0)

circle4_0 = plt.Circle((0, 0), 1, color='r', fill=False)
ax4.add_artist(circle4_0)


plt.figtext(0.45, 0.67, '$\mathcal{R}e$')
plt.figtext(0.31, 0.88, '$\mathcal{I}m$')
plt.figtext(0.88, 0.67, '$\mathcal{R}e$')
plt.figtext(0.73, 0.88, '$\mathcal{I}m$')
plt.figtext(0.45, 0.25, '$\mathcal{R}e$')
plt.figtext(0.31, 0.45, '$\mathcal{I}m$')
plt.figtext(0.88, 0.25, '$\mathcal{R}e$')
plt.figtext(0.73, 0.45, '$\mathcal{I}m$')

plt.show()
fig.savefig("ROC.png")
