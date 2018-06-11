import numpy as np
import matplotlib.pyplot as plt


arrayA = np.arange(.01, 2, .01)
Xm = 1.0
f = lambda x, A: A*np.cos(1.0*x/10) 
N = 101000

variance = lambda x: 1.0/np.size(x)*np.sum(x**2)
def snr(arrayA, B): 
    retx, rety = np.array([]), np.array([])
    
    Delta = 1.0*Xm/(2**B)
    quant = lambda x: np.where(x<-Xm, -Xm, np.where(x<Xm-Delta, np.floor((x+(Delta/2))/Delta)*Delta, Xm-Delta))
    
    for A in arrayA:
        x = np.arange(N)
        y = f(x, A)
        qy = quant(y)
        e = qy-y
        vy = variance(y)
        ve = variance(e)

        retx = np.append(retx, Xm/np.sqrt(vy))
        rety = np.append(rety, 10*np.log10(vy/ve))
    return np.log10(retx), rety


fig = plt.figure(figsize=(5, 4), dpi=120)
ax = fig.subplots(1, 1)
ax.xaxis.set_ticks([0, 1, 2])
ax.xaxis.set_ticklabels([r"$10^0$", r"$10^1$", r"$10^2$"])
ax.set_ylabel("SNR (dB)")
ax.set_xlabel(r"$X_m/\sigma_x$")
plt.subplots_adjust(bottom=.2)

B = 6-1
x2, y2 = snr(arrayA, B)
ax.plot(x2, y2)
ax.text(1.8, 2.5, "B=5", color='C0')

B = 8-1
x3, y3 = snr(arrayA, B)
ax.plot(x3, y3)
ax.text(1.8, 15, "B=7", color='C1')

B = 10-1
x4, y4 = snr(arrayA, B)
ax.plot(x4, y4)
ax.text(1.8, 29, "B=9", color='C2')

B = 12-1
x5, y5 = snr(arrayA, B)
ax.plot(x5, y5)
ax.text(1.8, 43, "B=11", color='C3')

B = 14-1
x6, y6 = snr(arrayA, B)
ax.plot(x6, y6)
ax.text(1.8, 56, "B=13", color='C4')

B = 16-1
x7, y7 = snr(arrayA, B)
ax.plot(x7, y7)
ax.text(1.8, 70, "B=15", color='C5')

fig.savefig("SNR.png", format='png')
plt.show()
