import matplotlib.pyplot as plt
import numpy as np

def dummyStem(ax, x, y, clr):
    i = 0
    for xi in x:
        if y[i]>=0 :
            ax.annotate("", xy=(xi, y[i]), xytext=(xi, -.01), arrowprops=dict(arrowstyle='->', color=clr), color=clr)
        if y[i]<0 :
            ax.annotate("", xy=(xi, y[i]), xytext=(xi, .01), arrowprops=dict(arrowstyle='->', color=clr), color=clr)
        i += 1

def axesLNoAxis(ax):
    #ax.spines['left'].set_color('none')
    #ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_position('zero')
    ax.spines['right'].set_color('none')
    #ax.spines['top'].set_color('none')
    ax.yaxis.set_ticks([])
    ax.set_xlim(-7, 7)
    ax.set_ylim(-Xm-.2, Xm)

def axesL(ax):
    axesLNoAxis(ax)
    ax.xaxis.set_ticks([-6,-4, -2, 0, 2, 4, 6])
    ax.xaxis.set_ticklabels(["-3T", "-2T", "-T", "0", "T", "2T", "3T"])
    ax.yaxis.set_ticks([-Xm,-Xm+Delta, -Xm+2*Delta, -Xm+3*Delta, -Xm+4*Delta, -Xm+5*Delta, -Xm+6*Delta, -Xm+7*Delta])
    ax.yaxis.set_ticklabels([r"$-4\Delta$", r"$-3\Delta$", r"$-2\Delta$", r"$-\Delta$", r"$0$", r"$\Delta$", r"$2\Delta$", r"$3\Delta$"])

fig = plt.figure(figsize=(13, 3), dpi=120)
ax1, ax2, ax3 = fig.subplots(1, 3)

T = 2
f = lambda x: np.sin(.1*x+.8)+np.sin(.5*x)
hold = lambda x: np.floor(x/T)*T
g = lambda x: f(hold(x))
Xm = 2
Delta = 2.0*Xm/8
quant = lambda x: np.where(x<-Xm, -Xm, np.where(x<Xm-Delta, np.floor((x+(Delta/2))/Delta)*Delta, Xm-Delta))

x1 = np.arange(-10, 10, .02)
x2 = np.arange(-10, 10, 2)

holdy1 = g(x1)
quanty1 = quant(holdy1)
holdy2 = g(x2)
quanty2 = quant(holdy2)

axesLNoAxis(ax1)
markers1, stemlines1, baseline1 = ax1.stem(x2, quanty2)
plt.setp(markers1, 'markersize', 3)
plt.setp(stemlines1, 'linewidth', 1)
plt.setp(baseline1, 'linewidth', 1)
ax1.xaxis.set_ticklabels(["-3", "-2", "-1", "0", "1", "2", "3"])
ax1.yaxis.set_ticks([-Xm,-Xm+Delta, -Xm+2*Delta, -Xm+3*Delta, -Xm+4*Delta, -Xm+5*Delta, -Xm+6*Delta, -Xm+7*Delta])
ax1.yaxis.set_ticklabels([r"$-4\Delta$", r"$-3\Delta$", r"$-2\Delta$", r"$-\Delta$", r"$0$", r"$\Delta$", r"$2\Delta$", r"$3\Delta$"])
ax1.text(-6, 1.7, r"$\hat{x}[n]$", color='C0')

axesLNoAxis(ax2)
dummyStem(ax2, x2, quanty2, clr='r')
#plt.setp(markers2)
ax2.xaxis.set_ticks([-6,-4, -2, 0, 2, 4, 6])
ax2.xaxis.set_ticklabels(["-3T", "-2T", "-T", "0", "T", "2T", "3T"])
ax2.text(-6, 1.7, "impulses", color='r')

axesLNoAxis(ax3)
ax3.xaxis.set_ticks([-6,-4, -2, 0, 2, 4, 6])
ax3.xaxis.set_ticklabels(["-3T", "-2T", "-T", "0", "T", "2T", "3T"])
ax3.plot(x1, quanty1, linestyle='--', color='r')
ax3.text(-6, 1.7, r"$x_{DA}(t)$", color='r')

fig.savefig("DA.png", format='png')
plt.show()
