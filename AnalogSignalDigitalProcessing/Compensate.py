import numpy as np
import matplotlib.pyplot as plt

def axesCross(ax):
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.yaxis.set_ticks([])
    ax.xaxis.set_ticks([-2*np.pi/T, -np.pi/T, 0, np.pi/T, 2*np.pi/T])
    ax.xaxis.set_ticklabels([r"$-\frac{2\pi}{T}$", r"$-\frac{\pi}{T}$", 0, r"$\frac{\pi}{T}$", r"$\frac{2\pi}{T}$"])
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 2.5)
    ax.text(3.8, -.2, r"$\Omega$")

T = 2
f = lambda x: np.where(np.abs(x)<np.pi/T, T, 0)
g = lambda x: np.abs(2*np.sin(x*T/2)/x*np.exp(-1j*x*T/2))

x = np.arange(-3*np.pi, 3*np.pi, np.pi/100)
y1 = f(x)
y2 = g(x)

fig = plt.figure(figsize=(9, 2.5), dpi=120)
ax1, ax2 = fig.subplots(1, 2)

axesCross(ax1)
ax1.plot(x, y1)
ax1.plot(x, y2)
ax1.text(-.5, T+.1, "T")
ax1.annotate(r"$|H_0(j\Omega)|$", xy=(-2.2, .8), xytext=(-3.6, 1.2), arrowprops=dict(arrowstyle='->', color='C1'), color='C1')
ax1.annotate(r"$H_r(j\Omega)$", xy=(-np.pi/T+.1, 1.8), xytext=(-3.6, 2.1), arrowprops=dict(arrowstyle='->', color='C0'), color='C0')

axesCross(ax2)
ax2.plot(x, y1/y2, color='r')
ax2.text(-.5, 1.1, "1")
ax2.annotate(r"$|\tilde{H}_r(j\Omega)|$", xy=(-1.6, .8), xytext=(-3.5, 1.2), arrowprops=dict(arrowstyle='->', color='r'), color='r')

fig.savefig("Compensate.png", format='png')
plt.show()
