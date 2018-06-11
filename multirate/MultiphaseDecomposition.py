import numpy as np
import matplotlib.pyplot as plt

def axesOnlyX(ax):
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.yaxis.set_ticks([])

def normalizeStem(ax, x, y, markerstyle='.', color='C0', alpha=1.0):
    markers, stemlines, baseline = ax.stem(x, y, markerfmt=markerstyle)
    plt.setp(markers, 'markersize', 3, 'color', color, 'alpha', alpha)
    plt.setp(stemlines, 'linewidth', 1, 'color', color, 'alpha', alpha)
    plt.setp(baseline, 'linewidth', 1, 'color', 'r')
    return markers, stemlines, baseline


fig = plt.figure(figsize=(9,9), dpi=120)
ax1, ax2, ax3, ax4, ax5 = fig.subplots(5, 1)

f = lambda x: np.sin(.2*x)+1.3
mod = lambda x: np.where(x%4==0, 1, 0)
x = np.arange(-40, 40, 4)
x2 = np.arange(-40, 40, 1)
x3 = np.arange(-3, 4, 1)

axesOnlyX(ax1)
ax1.set_xlim(-12, 12)
normalizeStem(ax1, x2, f(x2), color='C0')
normalizeStem(ax1, x+3, f(x+3), color='C3')
ax1.annotate(r"$h[n]$", xy=(0, 0), xytext=(-12, 2), color='C0')

axesOnlyX(ax2)
ax2.set_xlim(-12, 12)
normalizeStem(ax2, x2-3, f(x2), color='C0')
normalizeStem(ax2, x, f(x+3), color='C3')
ax2.annotate(r"$h[n+3] = h[n]\delta[n+3]$", xy=(0, 0), xytext=(-12, 2), color='C0')

ax3.set_xlim(-12, 12)
axesOnlyX(ax3)
normalizeStem(ax3, x2, f(x2*4+3), color='C3', alpha=.3)
normalizeStem(ax3, x3, f(x3*4+3), color='C3')
ax3.annotate(r"$e_3[n] = compress\ h[n+3]\ with\ M$", xy=(0, 0), xytext=(-12, 2), color='C3')

axesOnlyX(ax4)
ax4.set_xlim(-12, 12)
normalizeStem(ax4, x2, f(x2+3)*mod(x2), color='C3')
ax4.annotate(r"$h_3[n] = expand\ e_3[n]\ with\ M$", xy=(0, 0), xytext=(-12, 2), color='C3')

axesOnlyX(ax5)
ax5.set_xlim(-12, 12)
normalizeStem(ax5, x2+3, f(x2+3)*mod(x2), color='C3')
ax5.annotate(r"$h_3[n-3] = h_3[n]\delta[n-3]$", xy=(0, 0), xytext=(-12, 2), color='C3')

fig.savefig("MultiphaseDecomposition.png", format='png')
plt.show()
