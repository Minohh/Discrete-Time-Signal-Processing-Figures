import matplotlib.pyplot as plt
import numpy as np

def axesL(ax):
    #ax.spines['left'].set_color('none')
    #ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_position('zero')
    ax.spines['right'].set_color('none')
    #ax.spines['top'].set_color('none')
    ax.yaxis.set_ticks([])
    ax.set_xlim(-7, 7)
    ax.set_ylim(-Xm-.2, Xm)
    ax.xaxis.set_ticks([-6,-4, -2, 0, 2, 4, 6])
    ax.xaxis.set_ticklabels(["-3T", "-2T", "-T", "0", "T", "2T", "3T"])
    ax.yaxis.set_ticks([-Xm,-Xm+Delta, -Xm+2*Delta, -Xm+3*Delta, -Xm+4*Delta, -Xm+5*Delta, -Xm+6*Delta, -Xm+7*Delta])
    ax.yaxis.set_ticklabels([r"$-4\Delta$", r"$-3\Delta$", r"$-2\Delta$", r"$-\Delta$", r"$0$", r"$\Delta$", r"$2\Delta$", r"$3\Delta$"])

fig = plt.figure(figsize=(9, 3), dpi=120)
ax = fig.subplots(1, 1)

T = 2
f = lambda x: np.sin(.1*x+.8)+np.sin(.5*x)
hold = lambda x: np.floor(x/T)*T
g = lambda x: f(hold(x))
Xm = 2
Delta = 2.0*Xm/8
quant = lambda x: np.where(x<-Xm, -Xm, np.where(x<Xm-Delta, np.floor((x+(Delta/2))/Delta)*Delta, Xm-Delta))

x = np.arange(-10, 10, .02)
y = f(x)

holdy = g(x)
quanty = quant(holdy)

axesL(ax)
ax.plot(x, y)
ax.annotate(r"$x_a(t)$", xy=(1, 1.26), xytext=(-2, 1.7), arrowprops=dict(arrowstyle='->', color='C0'), color='C0')
ax.plot(x, holdy)
ax.annotate(r"$x_0(t)$", xy=(0, .4), xytext=(-3, 1), arrowprops=dict(arrowstyle='->', color='C1'), color='C1')
ax.plot(x, quanty, linestyle='--', color='r')
ax.annotate(r"$\hat{x}(t)$", xy=(-1, -.57), xytext=(-3, -2), arrowprops=dict(arrowstyle='->', color='r'), color='r')

fig.savefig("QuantizationOutput.png", format='png')
plt.show()
