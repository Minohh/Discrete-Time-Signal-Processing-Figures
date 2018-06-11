import numpy as np
import matplotlib.pyplot as plt

Delta = 2.0
f = lambda x: np.where(np.abs(x)>Delta/2, 0, 1.0/Delta)

fig = plt.figure(figsize=(6, 2), dpi=120)
ax = fig.subplots(1, 1)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xlim(-2, 2)
ax.set_ylim(-.1, 1.1)
x = np.arange(-2, 2, .01)
y = f(x)

ax.xaxis.set_ticks([-Delta/2, 0, Delta/2])
ax.yaxis.set_ticks([])
ax.xaxis.set_ticklabels([r"$-\frac{\Delta}{2}$", r"$0$", r"$\frac{\Delta}{2}$"])
ax.plot(x, y)
ax.fill_between(x, 0, y, color='#999999', alpha=.5)
ax.text(-.2, 1.0/Delta+.1, r"$\frac{1}{\Delta}$")
ax.text(-2, .7, "Uniform Distribution")


fig.savefig("UniformDistribution.png", format='png')
plt.show()
