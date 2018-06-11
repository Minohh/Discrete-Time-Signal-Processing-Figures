import numpy as np
import matplotlib.pyplot as plt

def axesOnlyX(ax):
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.yaxis.set_ticks([])

def normalizeStem(ax, x, y, markerstyle='.', color='C0'):
    markers, stemlines, baseline = ax.stem(x, y, markerfmt=markerstyle)
    plt.setp(markers, 'markersize', 3, 'color', color)
    plt.setp(stemlines, 'linewidth', 1, 'color', color)
    plt.setp(baseline, 'linewidth', 1, 'color', 'r')
    return markers, stemlines, baseline


fig = plt.figure(figsize=(9,9), dpi=120)
ax1, ax2, ax3, ax4, ax5 = fig.subplots(5, 1)

f = lambda x: np.sin(.2*x)+1.3
mod = lambda x: np.where(x%4==0, 1, 0)
x = np.arange(-40, 40, 4)

axesOnlyX(ax1)
ax1.set_xlim(-12, 12)
normalizeStem(ax1, x, f(x), color='C0')
normalizeStem(ax1, x+1, f(x+1), color='C1')
normalizeStem(ax1, x+2, f(x+2), color='C2')
normalizeStem(ax1, x+3, f(x+3), color='C3')
ax1.annotate(r"$h[n] =\sum_{k=0}^{M-1}h_k[n-k] = \sum_{k=0}^{M-1} h_k[n]\delta[n-k]$", xy=(0, 0), xytext=(-12, 2))

x2 = np.arange(-40, 40, 1)
ax2.set_xlim(-12, 12)
axesOnlyX(ax2)
normalizeStem(ax2, x2, f(x2)*mod(x2), color='C0')
ax2.annotate(r"$h_0[n] = h_0[n]\delta[n-0]$", xy=(0, 0), xytext=(-12, 2), color='C0')

axesOnlyX(ax3)
ax3.set_xlim(-12, 12)
normalizeStem(ax3, x2+1, f(x2+1)*mod(x2), color='C1')
ax3.annotate(r"$h_1[n-1] = h_1[n]\delta[n-1]$", xy=(0, 0), xytext=(-12, 2), color='C1')

axesOnlyX(ax4)
ax4.set_xlim(-12, 12)
normalizeStem(ax4, x2+2, f(x2+2)*mod(x2), color='C2')
ax4.annotate(r"$h_2[n-2] = h_2[n]\delta[n-2]$", xy=(0, 0), xytext=(-12, 2), color='C2')

axesOnlyX(ax5)
ax5.set_xlim(-12, 12)
normalizeStem(ax5, x2+3, f(x2+3)*mod(x2), color='C3')
ax5.annotate(r"$h_3[n-3] = h_3[n]\delta[n-3]$", xy=(0, 0), xytext=(-12, 2), color='C3')

fig.savefig("multiphase.png", format='png')
plt.show()
