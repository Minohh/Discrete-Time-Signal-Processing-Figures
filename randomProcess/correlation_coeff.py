import numpy as np
import matplotlib.pyplot as plt

def axesCross(ax):
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

fig = plt.figure(figsize=(6, 6), dpi=120)
ax = fig.subplots(1, 1)

ax.set_xlim(-5, 5)
ax.set_ylim(-1, 5)
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

axesCross(ax)

f = lambda x: .4*(x-1)**2+.3
x = np.arange(-6, 6, .1)
y = f(x)

ax.plot(x, y)
ax.text(-.6, -.3, r"$0$")
ax.text(-.6, 4.7, r"$\sigma_Z^2$")
ax.text(4.8, -.3, r"$\alpha$")
ax.text(-5, .7, r"$a = \sigma_X^2$", color='C0')
ax.text(-5, .4, r"$b = 2\beta \sigma_{X,Y}$", color='C0')
ax.text(-5, .1, r"$c = \beta^2 \sigma_Y^2$", color='C0')
ax.annotate(r"$(\frac{-b}{2a}, \frac{-(b^2-4ac)}{4b})$", arrowprops=dict(arrowstyle='->', color='r'), xy=(1.1, .29), xytext=(1.5, -.8), color='r')
ax.annotate(r"$\sigma_Z^2 = a\alpha^2+b\alpha+c$", arrowprops=dict(arrowstyle='->', color='C0'), xy=(-.85, 1.6), xytext=(-5, 1), color='C0')
ax.scatter([1], [.3], color='r')

fig.savefig("correlation_coeff.png", format='png')
plt.show()
