from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import cmath
from scipy import special

#angle coordinate
f = lambda z: np.where(abs(z)==1 and cmath.phase(z)>-1.5 and cmath.phase(z)<1.5, 1, 0)
#f = lambda z: abs(special.ndtr(z))

fig = plt.figure(figsize=(6,4), dpi=80)
ax = fig.add_subplot(111, projection='3d')
#ax = fig.gca(projection='3d')

r = np.arange(0, 2, 0.03125)
omega = np.arange(-np.pi, np.pi, np.pi/32)
R,Omega = np.meshgrid(r,omega)
xn,yn = R.shape
W = R*0
X = R*0
Y = R*0
for xk in range(xn):
    for yk in range(yn):
        try:
            z = R[xk,yk]*cmath.exp(Omega[xk,yk]*1j)
            X[xk,yk] = z.real
            Y[xk,yk] = z.imag
            w = float(f(z))
            if w!=w:
                raise ValueError
            W[xk,yk] = w
        except (ValueError, TypeError, ZeroDivisionError):
            pass
#    print xk, xn

ax.text(2.5, 0, 0, "$\mathcal{R}e$", color='red')
ax.text(0, 2.5, 0, "$\mathcal{I}m$", color='red')
ax.text(2.1, 2.1, 1.2, "$\mathcal{Z}$", color='red')
ax.plot_surface(X, Y, W, rstride=1, cstride=1, cmap=cm.coolwarm)
#ax.plot_wireframe(X, Y, W, rstride=5, cstride=5)
#ax.contourf(X, Y, W, zdir='z', offset=1.3)


#plot line
g = lambda omega: np.where(abs(omega)<1.5, 1, 0)
line_complex = np.e**(omega*1j)
ax.plot3D(line_complex.real, line_complex.imag, g(omega))

#plot omega arrow line
omegaline = np.arange(-1.5, 1.5, 0.1)
omegalineHigh = [1.3]*len(omegaline)
omegaline_complex = np.e**(omegaline*1j)
ax.plot3D(omegaline_complex.real, omegaline_complex.imag, omegalineHigh, linewidth=2, color='k')

endpoint = cmath.exp(1.4*1j)
ax.plot([0.3, endpoint.real], [0.87, endpoint.imag], [1.3, 1.3], linewidth=2, color='k')
ax.plot([0.23, endpoint.real], [1.1, endpoint.imag], [1.3, 1.3], linewidth=2, color='k')
ax.text(0.18, 1.3, 1.3, "$\omega$", color='k')

#plt.show()
fig.savefig("3D.png")
