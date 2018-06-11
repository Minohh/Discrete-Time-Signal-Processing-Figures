import numpy as np
import matplotlib.pyplot as plt

def normalizeAxis(ax,  (xLeft, xRight), (yCeil, yFloor)):
    ax.set_xlim(xLeft, xRight)
    ax.set_ylim(yCeil, yFloor)

def drawStem(ax, x, y, color):
    markers, stemlines, baseline = ax.stem(x, y)
    plt.setp(markers, 'color', color, 'markersize', 3)
    plt.setp(stemlines, 'color', color, 'linewidth', 1)
    plt.setp(baseline, 'color', 'k', 'linewidth', 1)

B = 8-1
Xm = 1
Delta = 1.0*Xm/(2**B)
f = lambda x: 0.99*np.cos(1.0*x/10)
quant = lambda x: np.where(x<-Xm, -Xm, np.where(x<Xm-Delta, np.floor((x+(Delta/2))/Delta)*Delta, Xm-Delta))

fig = plt.figure(figsize=(9, 5), dpi=120)
ax1, ax2 = fig.subplots(2, 1)
normalizeAxis(ax1, (0, 150), (-1.1, 1.1))
normalizeAxis(ax2, (0, 150), (-1.3*Delta, 1.3*Delta))

x = np.arange(151)
y = f(x)
qy = quant(y)
drawStem(ax1, x, qy, 'C1')
drawStem(ax2, x, qy-y, 'C2')
ax1.text(17, .85, r"$\hat{x}[n]$", color='C1')
ax2.text(1, Delta, r"$e[n]$", color='C2')

fig.savefig("QExp8.png", format='png')
plt.show()
