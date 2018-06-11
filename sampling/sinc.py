import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5, 3), dpi=120)
ax = fig.subplots()

f = lambda x, rate: np.sinc(x*rate)
x = np.arange(-10, 10, .1)
T = 1
y = f(x, 1.0/T)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xlim(-3.5, 3.5)
ax.xaxis.set_ticks([-3, -2, -1, 0, 1, 2, 3])
ax.xaxis.set_ticklabels(["-3T", "-2T", "-T", "0", "T", "2T", "3T"])
ax.yaxis.set_ticks([1])
ax.plot(x, y)
ax.annotate(r"$sinc = \frac{sin(\pi x/T)}{\pi x/T}$", xy=(0, 0), xytext=(1.5, .6))

plt.show()
fig.savefig("sinc.png", fmt='png')

