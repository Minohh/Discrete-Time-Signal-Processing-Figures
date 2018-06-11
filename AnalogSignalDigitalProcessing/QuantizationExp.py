import numpy as np
import matplotlib.pyplot as plt

def normalizeAxis(ax):
    ax.set_xlim(0, 150)
    ax.set_ylim(-1.2, 1.2)

def drawStem(ax, x, y, color):
    markers, stemlines, baseline = ax.stem(x, y)
    plt.setp(markers, 'color', color, 'markersize', 3)
    plt.setp(stemlines, 'color', color, 'linewidth', 1)
    plt.setp(baseline, 'color', 'k', 'linewidth', 1)


f = lambda x: 0.99*np.cos(1.0*x/10)

fig = plt.figure(figsize=(9, 2.5), dpi=120)
ax = fig.subplots(1, 1)
normalizeAxis(ax)

x = np.arange(151)
y = f(x)

drawStem(ax, x, y, 'C0')
ax.text(1, 1, r"$x[n]$", color='C0')

fig.savefig("QExp.png", format='png')
plt.show()
