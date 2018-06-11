import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.where(np<-2, 0, np.where(x<-2, 0, np.where(x<-1, 1, np.where(x<0, .33*x+1.33, np.where(x<1, 1.33-.33*x, np.where(x<2, 1, 0))))))
block1 = lambda x: np.where(x<-1, 1, 0)
block2 = lambda x: np.where(abs(x)<1, 1, 0)
block3 = lambda x: np.where(x>1, 1, 0)

fig = plt.figure(figsize=(5,3), dpi=120)
ax = fig.subplots(1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xlim(-6, 6)
ax.set_ylim(-.6, 6)
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

x = np.arange(-10, 10, .02)
y = f(x)
ax.plot(x, y)
ax.fill_between(x, 0, block1(x)*y, color='#999999')
ax.fill_between(x, 0, block3(x)*y, color='#999999')
ax.fill_between(x, 0, block2(x)*y, color='r')
ax.annotate(r"the same spectrum as the original signal", xy=(-.5, 1.2), xytext=(-5.9, 4), arrowprops=dict(arrowstyle='->', color='r'))

plt.show()
fig.savefig("DownSampling_alise.png", fmt='png')
