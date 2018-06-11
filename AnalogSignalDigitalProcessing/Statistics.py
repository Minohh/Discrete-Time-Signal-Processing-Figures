import numpy as np
import matplotlib.pyplot as plt


B = 16-1
Xm = 1
Delta = 1.0*Xm/(2**B)
f = lambda x: 0.99*np.cos(1.0*x/10)
quant = lambda x: np.where(x<-Xm, -Xm, np.where(x<Xm-Delta, np.floor((x+(Delta/2))/Delta)*Delta, Xm-Delta))

fig = plt.figure(figsize=(9, 2.5), dpi=120)
ax = fig.subplots(1, 1)
ax.set_ylim(0, 1200)

x = np.arange(101000)
y = f(x)
qy = quant(y)
ax.hist(qy-y, 101, rwidth=.66, color='#999999')
#ax.text(-.0041, 1090, r"$B+1=8$", color='k')
ax.text(-.000016, 1090, r"$B+1=16$", color='k')

#fig.savefig("Stastics8.png", format='png')
fig.savefig("Stastics16.png", format='png')
plt.show()
