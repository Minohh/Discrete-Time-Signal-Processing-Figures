import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.where(x<=-1, 0, np.where(x<0, x+1, np.where(x<1, 1-x, 0)))
x = np.arange(-10, 10, .1)
y = f(x)

fig = plt.figure(figsize=(12,4), dpi=60)
ax1, ax2 = fig.subplots(1, 2)
ax1.set_ylim(-.2, 3)
ax1.set_xlim(-6, 6)
ax1.plot(x, y)

def periodization(f, T, times):
    limit = np.floor(T*times/2)
    x = np.arange(-limit, limit, .1)
    sumY = 0
    for n in np.arange(times):
        sumY = sumY + f(x-T*n)
        if n != 0:
            sumY = sumY + f(x+T*n)
    return x, sumY

x, y = periodization(f, 1.5, 10)
ax2.set_ylim(-.2, 3)
ax2.set_xlim(-6, 6)
ax2.plot(x, y)


plt.show()
fig.savefig("periodization.png")
